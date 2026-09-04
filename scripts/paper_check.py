#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
paper_check.py v1.1 — 三维医学影像报告生成方向论文定期检索脚本

功能：
  1. 检索 arXiv（预印本）与 PubMed（期刊正式发表）上与
     「三维（CT/MRI 体积）影像报告生成」相关的新论文；
  2. 与 README 已有条目及历史候选（candidates/seen.json）去重；
  3. 把候选行写入 README「八、自动检索候选」区并生成 PR 素材；
  4. 自动清理：已被用户移入正式分类（一~七）或删除的候选行，
     下次运行时自动从八区移除；八区清空后整节自动删除。

用法：
    python scripts/paper_check.py --repo <仓库路径>             # 正式模式
    python scripts/paper_check.py --repo <仓库路径> --dry-run   # 只预览
    python scripts/paper_check.py --repo <仓库路径> --offline   # 不联网（仅清理）

依赖：仅 Python 3 标准库。
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

USER_AGENT = "paper-check/1.1 (3D medical imaging report generation tracking)"
ARXIV_API = "https://export.arxiv.org/api/query"
PUBMED_SEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
LOOKBACK_DAYS = 21
ARXIV_MAX = 60
PUBMED_MAX = 50
SECTION_TITLE = "八、自动检索候选（机器生成，待人工审阅整理）"
SECTION_NOTE = (
    "> 本区由 GitHub Actions 每周自动检索（arXiv/PubMed）生成，未经人工核实；"
    "请在审阅后自行把条目移入上方正式分类，或整行删除。已整理/删除的条目会在下次运行时自动清出本区。"
)
MAINTENANCE_HEAD = "## 维护说明"

# 常见期刊名规范化（PubMed 全称 → 简写/规范名）
VENUE_MAP = {
    "ieee transactions on medical imaging": "IEEE TMI",
    "ieee journal of biomedical and health informatics": "IEEE JBHI",
    "ieee transactions on neural networks and learning systems": "IEEE TNNLS",
    "medical image analysis": "Medical Image Analysis",
    "npj digital medicine": "npj Digital Medicine",
    "npj artificial intelligence": "npj Artificial Intelligence",
    "nature communications": "Nature Communications",
    "nature biomedical engineering": "Nature Biomedical Engineering",
    "scientific data": "Scientific Data",
    "european journal of radiology": "European Journal of Radiology",
    "radiology": "Radiology",
    "european radiology": "European Radiology",
    "computer methods and programs in biomedicine": "Computer Methods and Programs in Biomedicine",
}

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

ARXIV_ID_PAT = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})|arXiv[:/]?(\d{4}\.\d{4,5})", re.IGNORECASE)
PMID_PAT = re.compile(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", re.IGNORECASE)
DOI_PAT = re.compile(r"10\.\d{4,9}/[A-Za-z0-9._\-()/:]+")
ROW_LINE_PAT = re.compile(r"^\| \[.*\|$")
DATE_HEAD_PAT = re.compile(r"^### (\d{4}-\d{2}-\d{2})（新增 \d+ 篇）$")


def http_get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8", "replace"))


def http_get_text(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def clean_title(title):
    t = re.sub(r"\s+", " ", title).strip()
    t = re.sub(r"\s*\.+$", "", t)  # PubMed 标题末尾常带句号
    return t.strip(":; ")


def pretty_venue(raw):
    v = raw.strip().lower()
    if v in VENUE_MAP:
        return VENUE_MAP[v]
    return re.sub(r"\b([a-z])", lambda m: m.group(1).upper(), raw.strip(), count=0) if False else " ".join(
        w if w.lower() in ("of", "and", "for", "in", "on", "the", "a", "an") else w.capitalize()
        for w in raw.strip().split()
    )


def is_relevant(title, abstract):
    text = f"{title} {abstract}"
    if REVIEW_NOISE_PAT.search(title.strip()):
        return False
    return bool(REPORT_PAT.search(text) and IMAGING_3D_PAT.search(text))


def ids_in_text(text):
    """从文本里提取 (kind, id) 集合：arxiv / pubmed / doi"""
    ids = set()
    for m in ARXIV_ID_PAT.finditer(text):
        ids.add(("arxiv", (m.group(1) or m.group(2)).lower()))
    for m in PMID_PAT.finditer(text):
        ids.add(("pubmed", m.group(1)))
    for m in DOI_PAT.finditer(text):
        ids.add(("doi", m.group(0).rstrip(".;,)]")))
    return ids


def row_id(line):
    for m in ARXIV_ID_PAT.finditer(line):
        return ("arxiv", (m.group(1) or m.group(2)).lower())
    for m in PMID_PAT.finditer(line):
        return ("pubmed", m.group(1))
    for m in DOI_PAT.finditer(line):
        return ("doi", m.group(0).rstrip(".;,)]"))
    return None


# ---------- 检索 ----------
def fetch_arxiv(since, known):
    query = 'all:"report generation" OR all:"report generator" OR all:"report synthesis"'
    params = {
        "search_query": query,
        "start": 0,
        "max_results": ARXIV_MAX,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    root = ET.fromstring(http_get_text(url))
    ns = {"a": "http://www.w3.org/2005/Atom"}
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
        if ("arxiv", aid.lower()) in known:
            continue
        if not is_relevant(title, abstract):
            continue
        found.append({
            "kind": "arxiv", "id": aid, "title": clean_title(title),
            "venue": "arXiv", "year": published[:4],
            "url": f"https://arxiv.org/abs/{aid}",
            "remark": f"arXiv 预印本 · 自动检索候选（{published[:10]} 提交）",
        })
    return found


def fetch_pubmed(since, known):
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
    time.sleep(0.4)
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
        if ("pubmed", pmid) in known or not title or not is_relevant(title, abstract):
            continue
        journal = d.get("fulljournalname") or d.get("source") or "期刊"
        pubdate = d.get("pubdate", "")
        doi = ""
        for aid in d.get("articleids", []) or []:
            if aid.get("idtype") == "doi":
                doi = aid.get("value", "")
        parts = ["PubMed 收录"]
        if doi:
            parts.append(f"DOI {doi}")
        parts.append("自动检索候选（待人工核实）")
        found.append({
            "kind": "pubmed", "id": pmid, "title": clean_title(title),
            "venue": pretty_venue(journal), "year": pubdate[:4],
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            "remark": " · ".join(parts),
        })
    return found


# ---------- 八区清理 ----------
def prune_candidates_section(text):
    """移除已被移入正式分类（一~七）或已删除的候选行；八区清空则整节删除。
    返回 (新文本, 移除行数, 是否删除整节)。"""
    head_marker = f"## {SECTION_TITLE}"
    start = text.find(head_marker)
    if start < 0:
        return text, 0, False
    notes = text.find(MAINTENANCE_HEAD, start)
    if notes < 0:
        notes = len(text)
    prefix = text[:start]           # 正式区（含八区前的分隔线）
    zone = text[start:notes]        # 八区整块（含标题/说明/各日期小节）
    head_ids = ids_in_text(prefix)

    # 逐行重组：保留表头/分隔/说明，按日期小节分组
    kept_groups = {}   # date -> [rows]
    current_date = None
    for line in zone.splitlines():
        m = DATE_HEAD_PAT.match(line.strip())
        if m:
            current_date = m.group(1)
            kept_groups.setdefault(current_date, [])
            continue
        if ROW_LINE_PAT.match(line) and current_date is not None:
            rid = row_id(line)
            if rid is not None and rid in head_ids:
                continue  # 已整理进正式分类 → 从八区移除
            kept_groups[current_date].append(line)

    kept_total = 0
    for date_lines in kept_groups.values():
        kept_total += len(date_lines)
    total_rows = 0
    cur = None
    for line in zone.splitlines():
        m = DATE_HEAD_PAT.match(line.strip())
        if m:
            cur = m.group(1)
        if ROW_LINE_PAT.match(line) and cur:
            total_rows += 1
    removed = total_rows - kept_total
    if removed == 0:
        return text, 0, False

    if not any(kept_groups.values()):
        # 整节删除：同时去掉八区前的 "---" 分隔线，恢复为 正式区 + --- + 维护说明
        core = prefix
        if core.rstrip().endswith("---"):
            core = core[: core.rfind("---")].rstrip()
        tail = text[notes:]
        return core.rstrip() + "\n\n---\n\n" + tail.lstrip("\n"), removed, True

    # 部分清理：重建八区
    new_zone = [f"## {SECTION_TITLE}", "", SECTION_NOTE, ""]
    for d in sorted(kept_groups.keys()):
        lines = kept_groups[d]
        if not lines:
            continue
        new_zone.append(f"### {d}（新增 {len(lines)} 篇）")
        new_zone.append("| 论文 | 载体 | 年份 | 备注 |")
        new_zone.append("|---|---|---|---|")
        new_zone.extend(lines)
        new_zone.append("")
    rebuilt = "\n".join(new_zone).rstrip() + "\n"
    tail = text[notes:]
    return prefix + rebuilt + "\n" + tail.lstrip("\n"), removed, False


# ---------- 候选写入 ----------
def append_candidates_section(text, rows, today):
    """并入/新建「八、自动检索候选」，返回新文本（不处理已存在同日小节的情况由调用方保证）。"""
    sub = [f"### {today}（新增 {len(rows)} 篇）", "| 论文 | 载体 | 年份 | 备注 |", "|---|---|---|---|"]
    for r in rows:
        cell = r["remark"].replace("|", "/")
        sub.append(f"| [{r['title']}]({r['url']}) | {r['venue'].replace('|','/')} | {r['year']} | {cell} |")
    sub = "\n".join(sub)
    notes = text.find(MAINTENANCE_HEAD)
    if f"## {SECTION_TITLE}" in text:
        zone_end = text.find(MAINTENANCE_HEAD)
        # 插在八区最后一行之后、维护说明之前
        before = text[:zone_end].rstrip() + "\n\n"
        return before + sub + "\n\n" + text[zone_end:]
    # 新建八区：插在维护说明前的分隔线之后
    pre = text[:notes]
    core = pre
    if core.rstrip().endswith("---"):
        core = core[: core.rfind("---")].rstrip()
    block = (
        f"## {SECTION_TITLE}\n\n{SECTION_NOTE}\n\n"
        f"{sub}\n"
    )
    return core + "\n\n---\n\n" + block + "\n" + text[notes:].lstrip("\n")


def bump_changelog(text, n, today):
    marker = "## 更新记录"
    idx = text.index(marker)
    bullet = f"- **{today}（自动检索）**：新增候选 {n} 篇（arXiv/PubMed），经 PR 审阅合并后生效。\n"
    return text[:idx] + marker + "\n\n" + bullet + text[idx + len(marker):].lstrip("\n")


def main():
    ap = argparse.ArgumentParser(description="三维影像报告论文定期检索")
    ap.add_argument("--repo", default=".", help="仓库根目录")
    ap.add_argument("--days", type=int, default=LOOKBACK_DAYS, help="回溯天数")
    ap.add_argument("--dry-run", action="store_true", help="仅预览，不写文件")
    ap.add_argument("--offline", action="store_true", help="不联网（只做八区清理/预览）")
    args = ap.parse_args()

    root = Path(args.repo).resolve()
    readme = root / "README.md"
    if not readme.exists():
        print(f"[错误] 找不到 README.md：{readme}")
        return 2

    since = date.today() - timedelta(days=args.days)
    today = date.today().isoformat()
    print(f"检索窗口：{since} ~ {today}" + ("（离线模式）" if args.offline else ""))

    seen_file = root / "candidates" / "seen.json"
    seen = {"arxiv": [], "pubmed": [], "doi": []}
    if seen_file.exists():
        try:
            seen = json.loads(seen_file.read_text(encoding="utf-8"))
        except Exception:
            seen = {"arxiv": [], "pubmed": [], "doi": []}

    orig = readme.read_text(encoding="utf-8")
    text = orig
    removed = 0
    if not args.dry_run:
        text, removed, dropped = prune_candidates_section(text)
        if removed:
            print(f"八区自动清理：移除 {removed} 条已整理/删除的候选" +
                  ("（八区已清空，整节删除）" if dropped else ""))

    rows = []
    if not args.offline:
        known = ids_in_text(text) | set(seen.get("arxiv", [])) | set(seen.get("pubmed", [])) | set(seen.get("doi", []))
        for source, fn in (("arXiv", fetch_arxiv), ("PubMed", fetch_pubmed)):
            try:
                items = fn(since, known)
                rows.extend(items)
                print(f"{source}：命中 {len(items)} 条新候选")
            except Exception as exc:
                print(f"[警告] {source} 检索失败：{exc}")
        rows.sort(key=lambda r: (r["year"], r["title"]), reverse=True)
        for r in rows:
            print(f"  [{r['kind']}] {r['year']} {r['title']}\n        {r['url']}")

    changed = removed > 0
    if rows:
        text = append_candidates_section(text, rows, today)
        text = bump_changelog(text, len(rows), today)
        changed = True

    if args.dry_run:
        if removed:
            print("[dry-run] 以上清理未写入（仅预览）。")
        print(f"\n[dry-run] 本次{'候选 ' + str(len(rows)) + ' 条' if rows else '无新候选'}，未修改任何文件。")
        return 0

    if not changed:
        print("无新增候选、无待清理条目，结束。")
        return 0

    readme.write_text(text, encoding="utf-8", newline="\n")
    print(f"已更新 {readme}")

    if rows:
        for r in rows:
            seen.setdefault(r["kind"], []).append(r["id"])
        seen_file.parent.mkdir(parents=True, exist_ok=True)
        seen_file.write_text(json.dumps(seen, ensure_ascii=False, indent=2), encoding="utf-8")
        title = f"论文候选：新增 {len(rows)} 篇（{today}，三维影像报告方向）"
        body = [
            f"## 自动检索结果（{today}）", "",
            f"在 arXiv / PubMed 检索到 {len(rows)} 篇可能与「三维医学影像报告生成」相关的新论文，"
            "已自动写入 README「八、自动检索候选」区。",
            "",
            "审阅方式：查看下方清单与 README diff——相关请点 Merge（条目进入仓库即上传）；"
            "无关或重复请直接 Close（仓库不会变化）。已整理或删除的候选会在下次运行时自动清出八区。",
            "",
        ]
        for r in rows:
            body.append(f"- {r['year']} [{r['title']}]({r['url']}) — {r['venue']}")
        body += ["", "> 本 PR 由 weekly-paper-check 工作流自动生成。"]
        (root / ".pr-title.txt").write_text(title, encoding="utf-8")
        (root / ".pr-body.md").write_text("\n".join(body), encoding="utf-8")
        print("已生成 PR 素材：.pr-title.txt / .pr-body.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
