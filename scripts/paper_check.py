#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
paper_check.py — 三维医学影像报告生成方向论文定期检索脚本

用途：检索 arXiv（预印本）与 PubMed（期刊正式发表）上与
      「三维（CT/MRI 体积）影像报告生成」相关的新论文，
      与 README 已有条目及历史候选去重后，把候选行写入
      README「八、自动检索候选」区并生成 PR 素材（.pr-title.txt / .pr-body.md）。

用法：
    python scripts/paper_check.py --repo <仓库路径>            # 正式模式（修改 README）
    python scripts/paper_check.py --repo <仓库路径> --dry-run  # 只预览，不修改任何文件

依赖：仅 Python 3 标准库（urllib / xml / json / re）。
"""
import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from pathlib import Path

USER_AGENT = "paper-check/1.0 (3D medical imaging report generation tracking)"
ARXIV_API = "https://export.arxiv.org/api/query"
PUBMED_SEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
LOOKBACK_DAYS = 21           # 每次回溯天数（漏跑一周也不会漏）
ARXIV_MAX = 60               # arXiv 每源拉取上限
PUBMED_MAX = 50              # PubMed 每源拉取上限
SECTION_HEAD = "八、自动检索候选（机器生成，待人工审阅整理）"

# ---------- 相关性过滤词表 ----------
REPORT_PAT = re.compile(
    r"report\s+(generation|generating|generator|synthesis)|"
    r"(generate|generating|generated|generation)\w*\s+reports?|"
    r"radiology\s+reports?|automated\s+reports?|"
    r"reporting\s+(system|framework|model|network|approach)",
    re.IGNORECASE,
)
IMAGING_3D_PAT = re.compile(
    r"\b3[- ]?d\b|three[- ]dimensional|volumetric|volume[- ]level|"
    r"whole[- ]volume|volume\s+(ct|mri|imaging)|computed\s+tomography|"
    r"\bct\s+(volume|volumes|report)|mri\s+volume|magnetic\s+resonance|"
    r"tomography|\bctpa\b|mimic[- ]?ct|ct[- ]?rate|radgenome|m3d",
    re.IGNORECASE,
)
REVIEW_NOISE_PAT = re.compile(
    r"^(review of|a review of|survey of|towards a standard)",
    re.IGNORECASE,
)

# ---------- 工具 ----------
def http_get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8", "replace"))


def http_get_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def is_relevant(title: str, abstract: str) -> bool:
    text = f"{title} {abstract}"
    if REVIEW_NOISE_PAT.search(title.strip()):
        return False
    return bool(REPORT_PAT.search(text) and IMAGING_3D_PAT.search(text))


# ---------- arXiv ----------
def fetch_arxiv(since: date, known: set) -> list:
    """arXiv API：report generation 相关条目（cs.CV + eess.IV，按提交时间倒序）"""
    query = 'all:"report generation" OR all:"report generator" OR all:"report synthesis"'
    params = {
        "search_query": query,
        "start": 0,
        "max_results": ARXIV_MAX,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    text = http_get_text(url)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(text)
    found = []
    for entry in root.findall("a:entry", ns):
        title = re.sub(r"\s+", " ", entry.findtext("a:title", "").strip())
        abstract = re.sub(r"\s+", " ", entry.findtext("a:summary", "").strip())
        aid = ""
        for link in entry.findall("a:link", ns):
            if link.get("title") == "abs":
                aid = link.get("href", "").rsplit("/", 1)[-1]
                break
        if not aid:
            continue
        published = entry.findtext("a:published", "")
        if published[:10] < since.isoformat():
            continue
        if aid in known:
            continue
        if not is_relevant(title, abstract):
            continue
        year = published[:4]
        found.append({
            "kind": "arxiv",
            "id": aid,
            "title": title,
            "venue": "arXiv",
            "year": year,
            "url": f"https://arxiv.org/abs/{aid}",
            "remark": f"arXiv 预印本 · 自动检索候选（{published[:10]} 提交）",
        })
    return found


# ---------- PubMed ----------
def fetch_pubmed(since: date, known: set) -> list:
    """PubMed：期刊正式发表的报告生成论文（按发表时间检索近期）"""
    dp_from = since.isoformat()
    dp_to = date.today().isoformat()
    term = (
        '("report generation"[tiab] OR "report generator"[tiab] OR '
        '"radiology report generation"[tiab] OR "automated report generation"[tiab] OR '
        '"report synthesis"[tiab]) AND '
        '("3D"[tiab] OR "3-D"[tiab] OR volumetric[tiab] OR "three-dimensional"[tiab] OR '
        '"computed tomography"[tiab] OR "magnetic resonance"[tiab] OR "chest CT"[tiab] OR '
        'MIMIC-CT[tiab] OR CT-RATE[tiab]) AND '
        f'("{dp_from}"[dp] : "{dp_to}"[dp])'
    )
    qs = urllib.parse.urlencode({
        "db": "pubmed", "term": term, "retmode": "json",
        "retmax": PUBMED_MAX, "sort": "pub_date", "tool": "paper-check",
    })
    res = http_get_json(f"{PUBMED_SEARCH}?{qs}")
    ids = res.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    time.sleep(0.4)  # NCBI 限速礼貌
    summ = http_get_json(
        f"{PUBMED_SUMMARY}?db=pubmed&retmode=json&tool=paper-check&id={','.join(ids)}"
    )
    docs = summ.get("result", {})
    found = []
    for pmid in ids:
        d = docs.get(pmid)
        if not d:
            continue
        title = re.sub(r"\s+", " ", d.get("title", "")).strip()
        abstract = re.sub(r"\s+", " ", d.get("abstract", "") or "").strip()
        if pmid in known or not title or not is_relevant(title, abstract):
            continue
        journal = d.get("fulljournalname") or d.get("source") or "期刊"
        pubdate = d.get("pubdate", "")
        year = pubdate[:4]
        doi = ""
        for aid in d.get("articleids", []) or []:
            if aid.get("idtype") == "doi":
                doi = aid.get("value", "")
        remark = f"{journal} · PubMed 收录"
        if doi:
            remark += f" · DOI {doi}"
        remark += " · 自动检索候选"
        found.append({
            "kind": "pubmed",
            "id": pmid,
            "title": title,
            "venue": journal,
            "year": year,
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            "remark": remark,
        })
    return found


# ---------- README 操作 ----------
def known_ids_from_readme(text: str) -> set:
    known = set()
    for m in re.finditer(r"arXiv[:/]?(\d{4}\.\d{4,5})", text, re.IGNORECASE):
        known.add(m.group(1))
    for m in re.finditer(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", text, re.IGNORECASE):
        known.add(m.group(1))
    for m in re.finditer(r"10\.\d{4,9}/[A-Za-z0-9._\-()/:]+", text):
        known.add(m.group(0).rstrip(".;,)]"))
    return known


def ensure_candidates_section(text: str, nl: str, rows: list, today: str) -> str:
    """把某次检索结果以小表形式并入「八、自动检索候选」区（不存在则新建）。"""
    sub = (
        f"### {today}（新增 {len(rows)} 篇）{nl}"
        f"| 论文 | 载体 | 年份 | 备注 |{nl}"
        f"|---|---|---|---|{nl}"
    )
    for r in rows:
        cell = r["remark"].replace("|", "/")
        sub += f"| [{r['title']}]({r['url']}) | {r['venue'].replace('|','/')} | {r['year']} | {cell} |{nl}"
    anchor = f"## 维护说明"
    sec_header = f"## {SECTION_HEAD}"
    if sec_header in text:
        # 插入到该区末尾（该区后是分隔线与「## 维护说明」）
        idx = text.index(anchor)
        head_idx = text.index(sec_header)
        # 找到区内容的结束：最后一个表格行后
        zone = text[head_idx:idx]
        # 在维护说明之前补一个小节
        return text[:idx] + sub + nl + text[idx:]
    else:
        block = (
            f"## {SECTION_HEAD}{nl}{nl}"
            f"> 本区由 GitHub Actions 每周自动检索（arXiv/PubMed）生成，未经人工核实；"
            f"请在审阅后自行把条目移入上方正式分类，或整行删除。{nl}{nl}"
        )
        # 插到「--- 与 ## 维护说明」之前
        idx = text.index(anchor)
        pre = text[:idx]
        if pre.rstrip().endswith("---"):
            pre = pre.rstrip() + nl
        return pre + block + sub + nl + text[idx:]


def bump_changelog(text: str, nl: str, n: int, today: str) -> str:
    marker = "## 更新记录"
    idx = text.index(marker)
    bullet = f"- **{today}（自动检索）**：新增候选 {n} 篇（arXiv/PubMed），经 PR 审阅合并后生效。{nl}"
    return text[:idx] + marker + nl + nl + bullet + text[idx + len(marker):].lstrip(nl)


def main() -> int:
    ap = argparse.ArgumentParser(description="三维影像报告论文定期检索")
    ap.add_argument("--repo", default=".", help="仓库根目录")
    ap.add_argument("--days", type=int, default=LOOKBACK_DAYS, help="回溯天数")
    ap.add_argument("--dry-run", action="store_true", help="仅预览，不写文件")
    args = ap.parse_args()

    root = Path(args.repo).resolve()
    readme = root / "README.md"
    if not readme.exists():
        print(f"[错误] 找不到 README.md：{readme}")
        return 2

    since = date.today() - timedelta(days=args.days)
    today = date.today().isoformat()
    print(f"检索窗口：{since} ~ {today}")

    # 历史记录
    seen_file = root / "candidates" / "seen.json"
    seen = {"arxiv": [], "pubmed": [], "doi": []}
    if seen_file.exists():
        try:
            seen = json.loads(seen_file.read_text(encoding="utf-8"))
        except Exception:
            seen = {"arxiv": [], "pubmed": [], "doi": []}

    text = readme.read_text(encoding="utf-8")
    known = known_ids_from_readme(text) | set(seen.get("arxiv", [])) | set(seen.get("pubmed", [])) | set(seen.get("doi", []))

    rows = []
    warnings = []
    for source, fn in (("arXiv", fetch_arxiv), ("PubMed", fetch_pubmed)):
        try:
            items = fn(since, known)
            rows.extend(items)
            print(f"{source}：命中 {len(items)} 条新候选")
        except Exception as exc:  # 单源失败不阻断整体
            warnings.append(f"{source} 检索失败：{exc}")
            print(f"[警告] {source} 检索失败：{exc}")

    rows.sort(key=lambda r: (r["year"], r["title"]), reverse=True)
    if not rows:
        print("本次未发现新候选，结束。")
        return 0

    print(f"\n共 {len(rows)} 条候选：")
    for r in rows:
        print(f"  [{r['kind']}] {r['year']} {r['title']}\n        {r['url']}")

    if args.dry_run:
        print("\n[dry-run] 以上为候选，未修改任何文件。")
        return 0

    # 1) README 写入候选区 + 更新记录
    nl = "\r\n" if "\r\n" in readme.read_bytes().decode("utf-8", "replace") else "\n"
    text = ensure_candidates_section(text, nl, rows, today)
    text = bump_changelog(text, nl, len(rows), today)
    readme.write_text(text, encoding="utf-8", newline="\n")
    print(f"已更新 {readme}")

    # 2) 记录 seen（避免重复报告）
    for r in rows:
        seen.setdefault(r["kind"], []).append(r["id"])
    seen_file.parent.mkdir(parents=True, exist_ok=True)
    seen_file.write_text(json.dumps(seen, ensure_ascii=False, indent=2), encoding="utf-8")

    # 3) PR 素材
    title = f"论文候选：新增 {len(rows)} 篇（{today}，三维影像报告方向）"
    body_lines = [
        f"## 自动检索结果（{today}）",
        "",
        f"在 arXiv / PubMed 检索到 {len(rows)} 篇可能与「三维医学影像报告生成」相关的新论文，"
        "已自动写入 README「八、自动检索候选」区。",
        "",
        "审阅方式：查看下方清单与 README diff——相关请点 Merge（条目进入仓库即上传）；"
        "无关或重复请直接 Close（仓库不会变化）。",
        "",
    ]
    for r in rows:
        body_lines.append(f"- {r['year']} [{r['title']}]({r['url']}) — {r['venue']}")
    body_lines += ["", "> 本 PR 由 weekly-paper-check 工作流自动生成。"]
    (root / ".pr-title.txt").write_text(title, encoding="utf-8")
    (root / ".pr-body.md").write_text("\n".join(body_lines), encoding="utf-8")
    print("已生成 PR 素材：.pr-title.txt / .pr-body.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
