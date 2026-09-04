# 三维医学影像报告生成 · 相关文献

> **范围**：CT/MRI 体积影像 ×（报告生成 / 视觉-语言模型 / 数据集 / 综述）。   
> **口径**：期刊/会议名、年份、DOI、卷期与中科院分区均经 Crossref、PubMed 或出版社官网核实；条目含更正/待核实提示时以提示为准，正式引用前请以 DOI 复核。

---

## 一、数据集（3D 图像–报告配对）

| 论文 | 期刊 / 会议 | 年份 | 备注 |
|---|---|---|---|
| [**CT-RATE**（胸部 CT 图文语料库）](https://www.nature.com/articles/s41551-025-01599-y) | Nature Biomedical Engineering（随 CT-GEN 论文发表；一区 TOP） | 2026（在线 2026-02-12） | 50,188 例体积 + 25,692 份报告，标签与 MIMIC-CXR 对齐；3D 报告生成的标准数据基座 |
| [**RadGenome-Chest CT**](https://www.nature.com/articles/s41597-025-05922-9) | Scientific Data（Nature 系数据期刊，一区） | 2025 | 基于 CT-RATE 扩展：197 类器官分割掩码、66.5 万句级定位报告、120 万定位 VQA 对 |
| [**MIMIC-CT**](https://arxiv.org/abs/2409.04489) | NeurIPS 2024 Datasets & Benchmarks（CCF-A） | 2024 | 33,676 项检查 / 109,213 个体积 / 195,245 份报告；[PhysioNet](https://physionet.org/content/mimic-ct/)；病人与 MIMIC-CXR 重合，3D CTRG 评测基准起源 |
| [**M3D-Data**](https://arxiv.org/abs/2404.00578) | NeurIPS 2024 Datasets & Benchmarks（CCF-A；BAAI + 港中文） | 2024 | 120 万图像-文本对、24.3 万条文本、9 类 3D 任务；[GitHub](https://github.com/baai-dcai/m3d) |

## 二、3D 报告生成 · 期刊论文（正式发表）

| 论文 | 期刊 / 会议 | 年份 | 备注 |
|---|---|---|---|
| [**CT-GEN / CT-CLIP**：Generalist foundation models from a multimodal dataset for 3D computed tomography](https://www.nature.com/articles/s41551-025-01599-y) | Nature Biomedical Engineering（一区 TOP），10:1610–1628 | 2026（在线 2026-02-12） | 3D 对比预训练（CT-CLIP）+ LLM 报告生成（CT-GEN），统一分类/报告/异常检测；期刊正式版为 **2026-02**，网上常误标 2025；早期 arXiv:2312.09083 |
| [**Reg2RG**：Large Language Model With Region-Guided Referring and Grounding for CT Report Generation](https://pubmed.ncbi.nlm.nih.gov/40215158/) | IEEE TMI（一区 TOP） | 2025 | DOI: 10.1109/TMI.2025.3559923；[项目页](https://hkustsmartlab.github.io/2025/05/21/reg2rg/)；区域引导 referring+grounding，首次在 MIMIC-CT 上系统评测 3D 报告生成 |
| **MvKeTR**：Chest CT Report Generation With Multi-View Perception and Knowledge Enhancement | IEEE JBHI（一区） | 2025 | DOI: [10.1109/JBHI.2025.3581289](https://doi.org/10.1109/jbhi.2025.3581289)；多视图感知 + 知识增强的胸部 CT 报告生成 |
| [**Abn-BLIP**：Abnormality-aligned Bootstrapping Language-Image Pre-training for pulmonary embolism diagnosis and report generation from CTPA](https://doi.org/10.1016/j.media.2025.103786) | Medical Image Analysis（一区 TOP） | 2026（2025 在印） | CTPA 异常对齐图文预训练：肺栓塞诊断 + 报告生成 |
| [**Feature Decomposition（S-LMR+CSE）**：Feature Decomposition via Shared Low-rank Matrix Recovery for CT Report Generation](https://doi.org/10.1109/TMI.2025.3628159) | IEEE TMI（一区 TOP），45(4):1501–1512 | 2026（2025 在线） | 共享低秩矩阵恢复分解"共享解剖模式 + 病灶特征"，连续切片编码建模层间连续性 |
| [**CTPA Vision-Language Model**：Vision-language model for report generation and outcome prediction in CT pulmonary angiogram](https://doi.org/10.1038/s41746-025-01807-8) | npj Digital Medicine（一区） | 2025 | 首个面向 CTPA 的视觉-语言模型：报告生成 + 临床结局预测（JHU 团队） |
| [**MG-3D**：Multi-grained knowledge-enhanced vision-language pre-training for 3D medical image analysis](https://www.sciencedirect.com/science/article/abs/pii/S1361841526000964) | Medical Image Analysis（一区 TOP） | 2026 | [PubMed](https://pubmed.ncbi.nlm.nih.gov/41846145/)；多粒度知识增强的三维视觉-语言预训练（报告/问答/分类） |
| [**Enhancing 3D Medical Image Understanding With Pretraining Aided by 2D Multimodal Large Language Models**](https://doi.org/10.1109/jbhi.2025.3609739) | IEEE JBHI（一区） | 2026 | 2D MLLM 预训练增强三维影像理解；会议版 ICASSP 2025（DOI: 10.1109/icassp49660.2025.10889731） |
| **SegReg-Rep**：Region-Aware Vision-Language Alignment for Fine-Grained Radiology Report Generation from 3D Medical Images | IEEE TPRMS | 2026 | 区域感知（分割区域引导）的视觉-语言对齐实现 3D 细粒度报告生成（B 档；DOI 见 IEEE 11520942） |
| Integrating clinical indications and patient demographics for multilabel abnormality classification and automated report generation in 3D chest CT | Frontiers in Radiology（新刊） | 2025 | 融合临床指征与人口学信息改进 3D 胸部 CT 多标签异常分类与报告生成（B 档补充） |

## 三、3D 报告生成 · 会议论文

| 论文 | 期刊 / 会议 | 年份 | 备注 |
|---|---|---|---|
| **CT-AGRG**：Automated Abnormality-Guided Report Generation from 3D Chest CT Volumes | ISBI 2025（CCF-B） | 2025 | DOI: [10.1109/ISBI60581.2025.10981073](https://doi.org/10.1109/ISBI60581.2025.10981073)；异常引导报告生成（Philips + Lyon） |
| [**3D MLLM Design Space**：Exploring the Design Space of 3D MLLMs for CT Report Generation](https://papers.miccai.org/miccai-2025/0316-Paper2261.html) | MICCAI 2025（CCF-B） | 2025 | [DOI](https://doi.org/10.1007/978-3-032-04978-0_23) · [arXiv:2506.21535](https://arxiv.org/abs/2506.21535)；系统探索 3D MLLM 设计选择 |
| [**CT2Rep**（自动化 3D 报告生成早期方法）](https://arxiv.org/abs/2403.06801) | MICCAI 2024（CCF-B） | 2024 | DOI: [10.1007/978-3-031-72390-2_45](https://doi.org/10.1007/978-3-031-72390-2_45)；CT-RATE 体系早期方法（TUM/Hamamci 组；奠基必引） |
| **CTGLM**：A Vision-Language Model for Automated Chinese Chest CT Report Generation | CHIP 2025（Springer CCIS，国内会议） | 2025 | DOI: [10.1007/978-981-96-3755-3_11](https://doi.org/10.1007/978-981-96-3755-3_11)；中文胸部 CT 报告生成 |

## 四、通用基础模型 / 视觉-语言预训练

| 论文 | 期刊 / 会议 | 年份 | 备注 |
|---|---|---|---|
| [**RadFM**：Towards generalist foundation model for radiology by leveraging web-scale 2D&3D medical data](https://www.nature.com/articles/s41467-025-62385-7) | Nature Communications（一区 TOP） | 2025 | Web 规模 2D&3D 放射通用模型，原生支持 3D CT 报告生成与 VQA（C 档：写综述时作"大模型时代"背景引用） |
| [**M3D / M3D-CLIP / M3D-LaMed**：M3D: Advancing 3D Medical Image Analysis with Multi-Modal Large Language Models](https://arxiv.org/abs/2404.00578) | NeurIPS 2024 Datasets & Benchmarks（CCF-A） | 2024 | [GitHub](https://github.com/baai-dcai/m3d)；首个多功能三维医学多模态大模型：报告生成/VQA/分类/分割/定位（奠基必引） |
| **Med-PaLM M**：Towards Generalist Biomedical AI | NEJM AI（新刊，暂无分区） | 2024 | DOI: [10.1056/AIoa2300138](https://doi.org/10.1056/AIoa2300138)；14 种生物医学模态通用模型；3D 体积能力有限——引用时注意定位 |
| **BTB3D**：Better Tokens for Better 3D: Advancing Vision-Language Modeling in 3D Medical Imaging | NeurIPS 2025（CCF-A） | 2025 | 面向 3D 医学影像的视觉 token 优化（TUM）（B 档补充） |
| **fVLM**：Large-scale and Fine-grained Vision-language Pre-training for Enhanced CT Image Understanding | ICLR 2025（CCF-A） | 2025 | 大规模细粒度（组织/病灶级）CT 预训练，下游支持 3D CT 报告生成（阿里巴巴）（B 档补充） |
| **RadCLIP** | IEEE TNNLS（一区 TOP） | 2025（10 月卷期） | DOI: [10.1109/tnnls.2025.3568036](https://doi.org/10.1109/tnnls.2025.3568036)；期刊版为 **2025-10**，非 2024（arXiv 2024-03 先行） |
| [**Decipher-MR**：a vision-language foundation model for 3D MRI representations](https://www.nature.com/articles/s41746-026-02596-4) | npj Digital Medicine（一区） | 2026 | MRI 专用三维视觉-语言基础模型（跨模态对照/迁移参考） |
| [**ViSD-Boost**](https://arxiv.org/abs/2508.03742) | ICCV 2025（CCF-A） | 2025 | 解剖正常性建模提升医学 VLP 的视觉语义密度（阿里；评估含 3D 医学任务） |
| **RadZero3D** | ICCV 2025 Workshop | 2025 | 自监督视频桥接医学视觉-语言对齐，零样本胸部 CT 解读（IEEE 11375501） |

## 五、脑 / 脊柱 MRI·CT 与相邻任务（跨部位参考）

| 论文 | 期刊 / 会议 | 年份 | 备注 |
|---|---|---|---|
| [**Interpretable Brain MRI Report Generation Anchored by Lesion Topography**](https://ieeexplore.ieee.org/abstract/document/11309731) | IEEE JBHI（一区） | 2026 | DOI: [10.1109/JBHI.2025.3646647](https://doi.org/10.1109/JBHI.2025.3646647)；病灶地形图锚定的可解释脑 MRI 报告生成 |
| **Co-Occurrence Relationship Driven Hierarchical Attention Network for Brain CT Report Generation** | IEEE TETCI，8(5):3643–3653（二区） | 2024 | DOI: [10.1109/TETCI.2024.3413002](https://doi.org/10.1109/TETCI.2024.3413002)；共现关系驱动的层次注意力脑 CT 报告生成 |
| [**From segmentation to explanation: Generating textual reports from MRI with LLMs**](https://pubmed.ncbi.nlm.nih.gov/40633400/) | Computer Methods and Programs in Biomedicine（二区） | 2025 | DOI: [10.1016/j.cmpb.2025.108922](https://doi.org/10.1016/j.cmpb.2025.108922)；分割→LLM 的 MRI 文本报告流程 |
| **SPINE**：Segmentation-guided Processing and Integration of Multimodal Spinal MRI for Natural-Language Enhanced Report Generation | Applied Artificial Intelligence | 2026 | DOI: [10.1080/08839514.2026.2626117](https://doi.org/10.1080/08839514.2026.2626117)；分割引导的多模态脊柱 MRI 报告生成 |
| **MEPNet**（医学实体均衡提示网络，脑 CT 报告生成） | AAAI 2025（CCF-A） | 2025 | 实体均衡提示：脑 CT 报告生成 |
| [**Weakly Guided Hierarchical Encoder-Decoder Network for Brain CT Report Generation**](https://ieeexplore.ieee.org/document/9669626) | IEEE BIBM 2021 | 2021 | 脑 CT 报告生成较早工作 |

## 六、综述与展望

| 论文 | 期刊 / 会议 | 年份 | 备注 |
|---|---|---|---|
| [**Vision-language foundation model for 3D medical imaging**](https://www.nature.com/articles/s44387-025-00015-9) | npj Artificial Intelligence（Nature 系新刊，暂无分区） | 2025 | 分析 23 项三维医学影像视觉-语言基础模型：架构/能力/训练数据/评估指标（JHU） |
| [**Vision-language foundation models for 3D neuroradiological interpretation: A systematic review**](https://www.sciencedirect.com/science/article/pii/S3050577126000423) | European Journal of Radiology AI（新刊） | 2026 | 三维神经影像（脑 MRI/CT）VLM 系统综述——迄今仅有的三维专题综述之一 |
| [**Multimodal generative AI for interpreting 3D medical images and videos**](https://www.nature.com/articles/s41746-025-01649-4) | npj Digital Medicine（一区） | 2025 | 三维医学影像与视频的多模态生成式 AI 展望（NYU） |   
| Foundation Models for Volumetric Medical Imaging: Opportunities, Challenges, and Future Directions | Electronics 15(6):1245（Q2） | 2026 | 体积影像基础模型综述（补充参考） |

## 七、预印本 / 追踪中（写稿前追新）

| 论文 | 载体 | 年份 | 备注 |
|---|---|---|---|
| [**Astra**](https://arxiv.org/abs/2605.31437) | arXiv | 2026 | 面向 3D CT 的可泛化报告生成基础模型（Ma 等） |
| [**SliceWorld**](https://arxiv.org/abs/2605.24371) | arXiv | 2026 | CT 报告生成的预测性可控"世界状态"模型 |
| Template Collapse in 3D CT Report Generation | arXiv（待核实） | 2026 | arXiv:2605.30984；测量并缓解 3D CT 报告生成模板崩塌——与综述"评估与语言重复"讨论直接相关 |
| [**MedVista3D**](https://arxiv.org/abs/2509.03800) | arXiv | 2025 | 3D CT 病灶检测 + 理解 + 报告一体化 VLM |
| [**COLIPRI**](https://arxiv.org/abs/2510.15042) | arXiv | 2025 | 微软 + TUM：大规模 3D 医学影像语言-图像预训练 |
| **Percival** | medRxiv | 2025 | 泛器官 3D CT 视觉-语言模型 |
| [**Med-2E3**](https://arxiv.org/abs/2411.12783) | arXiv | 2024 | 2D 增强的 3D 医学多模态大模型（CT-RATE / M3D-Data 上评测） |
| [**CT-GLIP**](https://arxiv.org/abs/2404.15272) | arXiv | 2024 | 全身 3D CT 图文预训练（grounded），覆盖多器官 |
| [**Med-Flamingo**](https://arxiv.org/abs/2307.15189) | ML4H@NeurIPS 2023（workshop） | 2023 | 常被引为 npj Digital Medicine 2024 的期刊版**未能核实**，引用前请自行确认 |
| [**GenerateCT**](https://arxiv.org/abs/2305.16037) | arXiv | 2023 | 文本→3D 胸部 CT 生成——报告生成的**反向任务** |
| [**Imitating Radiological Scrolling**：A Global-Local Attention Model for 3D Chest CT Volumes Multi-Label Anomaly Classification](https://arxiv.org/abs/2503.20652) | arXiv | 2025 | 3D CT 异常分类——报告生成的视觉前端 |
| [**AI-Driven Radiology Report Generation for Traumatic Brain Injuries**](https://arxiv.org/abs/2510.08498) | arXiv | 2025 | 创伤性脑损伤（CT）报告生成 |
| HLIP / SCALE-VLP / SigVLP / OKA-CT / OCP-CT / Jolia / GLINT 等 | arXiv | 2025–2026 | 批量 3D CT 视觉-语言预训练工作（比对自 Awesome-Volumetric-Radiology-AI 清单，2026-07 版） |

---

## 维护说明

- **新增一篇**：在对应分类表末尾复制一行 → 填「论文名（英文全称或简称）」→ 把标题/链接贴上 → 填「期刊/会议 + 年份」与备注 → 点 *Preview* 确认表格不错位 → *Commit changes*。
- **字段口径**：期刊/会议列建议带**中科院分区简注**（参考口径见文末）；备注列写一句话要点与更正提示；每个单元格不要出现裸的 `|` 字符（会破坏表格）。
- **追溯源**：本仓库内容整理自本地调研文档《三维影像报告生成_3D文献清单》（检索核实日期见本地文档），其完整档位（A/B/C）与查漏说明未全部搬入本表，需要时可对照。
- **自动候选区（第八节）**：由 GitHub Actions（weekly-paper-check）每周自动检索 arXiv/PubMed 生成并开 PR 供审阅——Merge 即上传；候选条目未经人工核实，请及时核实后移入正式分类或删除（不想要直接 Close PR 即可）。
- **检索方式（自动脚本 `scripts/paper_check.py`，由 Actions 工作流 weekly-paper-check 驱动）**
    - **数据源与周期**：arXiv（预印本）+ PubMed（期刊正式发表）；每周一 02:20 UTC 自动运行，也可在 Actions 页面手动 Run workflow。
    - **arXiv 检索式**：分类 cs.CV / eess.IV 中检索 `"report generation" OR "report generator" OR "report synthesis"`，按提交时间倒序取前 60 条。
    - **PubMed 检索式**：报告类词（report generation / report generator / radiology report generation / automated report generation / report synthesis）× 3D 影像类词（3D / 3-D / volumetric / three-dimensional / computed tomography / magnetic resonance / chest CT / MIMIC-CT / CT-RATE）× 最近 35 天时间窗。
    - **相关性过滤**：标题或摘要需同时含「报告生成」类词与「3D/体积影像」类词；明显噪音（综述句式、纯 2D 主题等）自动剔除。
    - **去重**：自动比对 README 已有条目的 arXiv 号 / PMID / DOI，以及 `candidates/seen.json` 的历史记录——同一篇论文不会重复推送。
    - **产物**：命中即把候选行追加进「八、自动检索候选」区（按检索日期分节）并自动开 PR；无命中则静默结束、不开 PR。
    - **自动清理**：候选被移入正式分类或整行删除后，下次运行自动从八区移除；八区清空则整节自动删除。
    - **本地手动运行**：`python scripts/paper_check.py --repo .`（联网正式模式）；`--dry-run`（只预览不写文件）；`--offline`（只做清理、不联网）。

## 引用前必读

1. **中科院分区**为参考标注，以最新《中科院文献情报中心分区表（升级版）》为准；npj AI、NEJM AI、EJR AI 为 2024–2026 新刊，暂未入分区表（但均为 Nature/NEJM 系）。
2. 会议与期刊并存条目（M3D、RadFM、Enhancing 3D…）：正式期刊版优先引用，会议版作补充。
3. 所有 DOI/链接均为整理时实测可访问；卷期页码等细节请在正式引用前用 DOI 复核。

## 更新记录


- **2026-09-03**：初始收录。自本地调研清单去重整理：6 类正式条目（数据集 4 / 期刊 10 / 会议 4 / 通用模型 9 / 跨部位 6 / 综述 4）+ 预印本追踪 13；引用优先级沿用原清单 A/B/C 档位口径（记录于本地调研文档）。
- **2026-09-03（修订）**：按需求移除各表状态列与页面装饰图标，表列统一为「论文 / 期刊·会议 / 年份 / 备注」。
