# 胸部三维影像报告生成 · 综述文献

本仓库整理胸部三维影像报告生成综述的相关文献，按数据集、评价方法、三维方法与二维相关方法组织。三维按影像来源划分，包括完整体积、切片和多平面输入；同时涉及二维与三维来源的研究单独列出。当前展示初筛保留的模型候选，后续随全文筛选更新。

## 目录

- [一、数据集与基准](#datasets)
- [二、评价指标与评估方法](#evaluation)
- [三、三维影像报告生成方法](#methods-3d)
- [四、二维相关方法](#methods-2d)
- [自动检索候选](#automatic-candidates)

<a id="datasets"></a>

## 一、数据集与基准

待补充。

<a id="evaluation"></a>

## 二、评价指标与评估方法

待补充。

<a id="methods-3d"></a>

## 三、三维影像报告生成方法

本次导入 104 条“保留模型候选”：三维影像来源 73 条，二维及三维来源 31 条。保留筛选表中的候选记录与版本，不将其计作 104 个独立模型；同题名的不同来源或版本暂未合并。

年份沿用筛选表的多版本口径，可能对应最早版本；发表渠道按关联题录补充，未统一为正式发表年份。arXiv 条目展示预印本版本，不据此断言其尚未正式发表。

### 三维影像来源（73 条）

| 论文标题 | 年份 | 发表渠道 |
|---|---|---|
| [A Multimodal Contrastive Learning Framework for Automated Pulmonary Fibrosis Report Generation from Chest HRCT](https://doi.org/10.1109/icce-taiwan71481.2026.11652790) | 2026 | IEEE International Conference on Consumer Electronics |
| [A SAM2 and VLM-Based Automatic Radiological Reporting System for Pneumothorax Detection.](https://pubmed.ncbi.nlm.nih.gov/42940118/) | 2026 | Biomedicines |
| [ALTER: Modeling Longitudinal Changes via Regional Differencing for 3D CT Report Generation](https://arxiv.org/abs/2608.05615) | 2026 | arXiv（预印本） |
| [An Explainable AI Pipeline for Lung CT Analysis: Segmentation, Uncertainty Quantification, and Automated Vision–Language Reporting](https://doi.org/10.1109/ic-icns68863.2026.11537587) | 2026 | International Conference on Intelligent Computing, Networks, and Security (IC-ICNS) |
| [An Explainable Transformer-Based Framework for Lung Cancer Classification and Automated Radiology Report Generation from Multi-Slice CT Images.](https://pubmed.ncbi.nlm.nih.gov/42193426/) | 2026 | Biomedicines |
| [An Integrated Computational Framework for Lung Cancer Detection: Combining Deep Learning, Interactive Visualization, and Diagnostic Reporting from CT Imaging](https://doi.org/10.70917/ijcisim-2026-5116) | 2026 | International Journal of Computer Information Systems and Industrial Management Applications |
| [ASAP: Advancing Medical Volumetric Representation Learning with Anatomy-aware Semantically-adaptive Pre-training](https://arxiv.org/abs/2606.00602) | 2026 | arXiv（预印本） |
| [Astra: a generalizable report generation foundation model for 3D computed tomography](https://doi.org/10.21203/rs.3.rs-10034289/v1) | 2026 | Research Square（预印本） |
| [Astra: a generalizable report generation foundation model for 3D computed tomography](https://arxiv.org/abs/2605.31437) | 2026 | arXiv（预印本） |
| [Beyond the Embedding Bottleneck: Adaptive Retrieval-Augmented 3D CT Report Generation](https://arxiv.org/abs/2603.15822) | 2026 | arXiv（预印本） |
| [CT‑RetrievR: fine‑grained retrieval‑based report generation for 3D CT imaging](https://doi.org/10.1117/12.3083423) | 2026 | Medical Imaging |
| [Curriculum-Driven 3D CT Report Generation via Language-Free Visual Grafting and Zone-Constrained Compression](https://arxiv.org/abs/2603.23308) | 2026 | arXiv（预印本） |
| [Disease-Centric Vision-Language Pretraining with Hybrid Visual Encoding for 3D Computed Tomography](https://arxiv.org/abs/2606.25546) | 2026 | arXiv（预印本） |
| [End-to-End PET/CT Interpretation and Quantification with an LLM-Orchestrated AI Agent: A Real-World Pilot Study](https://doi.org/10.64898/2026.02.21.26346798) | 2026 | medRxiv（预印本） |
| [End-to-End PET/CT Interpretation and Quantification with an LLM-Orchestrated AI Agent: A Real-World Pilot Study.](https://pubmed.ncbi.nlm.nih.gov/42315314/) | 2026 | Journal of Nuclear Medicine |
| [Enhancing Fine-Grained Spatial Grounding in 3D CT Report Generation via Discriminative Guidance](https://arxiv.org/abs/2604.10437) | 2026 | arXiv（预印本） |
| [EXACT: an explainable anomaly-aware vision foundation model for analysis of 3D chest CT](https://arxiv.org/abs/2604.24146) | 2026 | arXiv（预印本） |
| [Explainable Multimodal Vision–Language Foundation Models for Automated Rib Fracture Detection, Anatomical Reasoning, and Clinically Faithful Radiology Report Generation](https://doi.org/10.68339/jaims.v1i1.6) | 2026 | Journal of Agentic Intelligence in Medical Sciences |
| [FZ-VLM: A Two Stage Florence-Zephyr Vision Language Model Framework for Pulmonary Nodule Characterization and Clinical Decision Making](https://arxiv.org/abs/2608.15004) | 2026 | arXiv（预印本） |
| [Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning](https://arxiv.org/abs/2606.24570) | 2026 | arXiv（预印本） |
| [MedScribe: Clinically Grounded CT Reporting through Agentic Workflows](https://arxiv.org/abs/2605.01779) | 2026 | arXiv（预印本） |
| [MonteRET: AI Agent Enhancing Multimodal LLMs with Multi-granularity Knowledge Retrieval for Chest CT Report Generation](https://arxiv.org/abs/2607.14264) | 2026 | arXiv（预印本） |
| [NV-Reason-CT: 3D Visual Language Model for CT Analysis](https://arxiv.org/abs/2609.27511) | 2026 | arXiv（预印本） |
| [OmniCT: Towards a Unified Slice-Volume LVLM for Comprehensive CT Analysis](https://arxiv.org/abs/2602.16110) | 2026 | arXiv（预印本） |
| [ORCA: ORgan-Centroid Aggregation for Training-Free 3D CT Visual Token Compression](https://arxiv.org/abs/2608.00345) | 2026 | arXiv（预印本） |
| [Performance validation of a closed loop fully automated AI model for lung nodule stratification in screening cases.](https://pubmed.ncbi.nlm.nih.gov/41564843/) | 2026 | Respiratory Investigation |
| [RadAgent: A tool-using AI agent for stepwise interpretation of chest computed tomography](https://arxiv.org/abs/2604.15231) | 2026 | arXiv（预印本） |
| [ReadCT: Parameter-Efficient 3D Chest CT Findings Generation Using Low- Rank Adaptation.](https://pubmed.ncbi.nlm.nih.gov/42983219/) | 2026 | Current Medical Imaging |
| [Resolution Meets Reduction: Efficient Visual Context for 3D Radiology Report Generation](https://arxiv.org/abs/2608.08713) | 2026 | arXiv（预印本） |
| [SegReg-Rep: Region-Aware Vision-Language Alignment for Fine-Grained Radiology Report Generation from 3D Medical Images](https://doi.org/10.1109/trpms.2026.3693637) | 2026 | IEEE Transactions on Radiation and Plasma Medical Sciences |
| [SelfCue: Making a 3D CT Report Generator Say What It Already Knows](https://arxiv.org/abs/2609.31788) | 2026 | arXiv（预印本） |
| [SliceWorld: A Predictive and Controllable World-State Model for CT Report Generation](https://arxiv.org/abs/2605.24371) | 2026 | arXiv（预印本） |
| [TNM-Accountable Whole-Body 3-Dimensional Fluorodeoxyglucose Positron Emission Tomography/Computed Tomography Report Drafting in Lung Cancer Cohorts via Structured Impressions and Organ-wise Exemplar Synthesis.](https://pubmed.ncbi.nlm.nih.gov/42483403/) | 2026 | Research |
| [Towards a Radiologist Imitation Framework for 3D CT Diagnosis with Multimodal LLMs](https://doi.org/10.18653/v1/2026.bionlp-1.85) | 2026 | BioNLP 2026 |
| [U-VLM: Hierarchical Vision Language Modeling for Report Generation](https://arxiv.org/abs/2603.00479) | 2026 | arXiv（预印本） |
| [Visual question answering-based image-finding generation for pulmonary nodules on chest CT from structured annotations.](https://pubmed.ncbi.nlm.nih.gov/41894071/) | 2026 | International Journal of Computer Assisted Radiology and Surgery |
| [VLI-Agent: Vision-Language-Interpretation Agents for Automated 3D CT Understanding](https://doi.org/10.3724/2096-7004.di.2026.0097) | 2026 | Data Intelligence |
| [Volumetric Chest CT Report Generation via State-Space Visual Prompting and Clinical-Fact Alignment.](https://pubmed.ncbi.nlm.nih.gov/42976478/) | 2026 | Physics in Medicine &amp; Biology |
| [A Multimodal Vision-Language framework for pulmonary embolism detection: integrating 3D CT analysis with medical LLM report generation](https://hdl.handle.net/11071/16377) | 2025 | Strathmore University 机构库 |
| [Abn-BLIP: Abnormality-aligned Bootstrapping Language-Image Pre-training for pulmonary embolism diagnosis and report generation from CTPA.](https://pubmed.ncbi.nlm.nih.gov/40945174/) | 2025 | Medical Image Analysis |
| [ClearView: A Quality-aware Cross-modal Alignment Framework for CT Report Generation](https://doi.org/10.1145/3731715.3733287) | 2025 | ACM ICMR 2025 |
| [Convolutional neural network application for automated lung cancer detection on chest CT using Google AI Studio.](https://pubmed.ncbi.nlm.nih.gov/40903384/) | 2025 | Radiography (London, England : 1995) |
| [CT-GRAPH: Hierarchical Graph Attention Network for Anatomy-Guided CT Report Generation](https://arxiv.org/abs/2508.05375) | 2025 | arXiv（预印本） |
| [CTGLM: A Vision-Language Model for Automated Chinese Chest CT Report Generation](https://doi.org/10.1007/978-981-96-3755-3_11) | 2025 | Springer CCIS |
| [From image to report: automating lung cancer screening interpretation and reporting with vision-language models.](https://pubmed.ncbi.nlm.nih.gov/41083099/) | 2025 | Journal of Biomedical Informatics |
| [Integrating clinical indications and patient demographics for multilabel abnormality classification and automated report generation in 3D chest CT scans.](https://pubmed.ncbi.nlm.nih.gov/41209490/) | 2025 | Frontiers in Radiology |
| [LungNoduleAgent: A Collaborative Multi-Agent System for Precision Diagnosis of Lung Nodules](https://arxiv.org/abs/2511.21042) | 2025 | arXiv（预印本） |
| [Multimodal Large Language Model for Medical Report Generation](https://doi.org/10.14711/thesis-hdl152429) | 2025 | 香港科技大学学位论文 |
| [OrthoInsight: Rib Fracture Diagnosis and Report Generation Based on Multi-Modal Large Models](https://arxiv.org/abs/2507.13993) | 2025 | arXiv（预印本） |
| [Preliminary Study on Image-Finding Generation and Classification of Lung Nodules in Chest CT Images Using Vision-Language Models](https://doi.org/10.3390/computers14110489) | 2025 | Computers |
| [Retrieval-based adaptive fusion strategy for medical report generation.](https://pubmed.ncbi.nlm.nih.gov/40639153/) | 2025 | Computer Methods and Programs in Biomedicine |
| [Vision-language model for report generation and outcome prediction in CT pulmonary angiogram.](https://pubmed.ncbi.nlm.nih.gov/40652098/) | 2025 | npj Digital Medicine |
| [3D-CT-GPT: Generating 3D Radiology Reports through Integration of Large Vision-Language Models](https://arxiv.org/abs/2409.19330) | 2024 | arXiv（预印本） |
| [CT-AGRG: Automated Abnormality-Guided Report Generation from 3D Chest CT Volumes](https://arxiv.org/abs/2408.11965) | 2024 | arXiv（预印本） |
| [CT2Rep: Automated Radiology Report Generation for 3D Medical Imaging](https://arxiv.org/abs/2403.06801) | 2024 | arXiv（预印本） |
| [Development of automatic generation system for lung nodule finding descriptions.](https://pubmed.ncbi.nlm.nih.gov/38512860/) | 2024 | PLOS ONE |
| [Dia-LLaMA: Towards Large Language Model-driven CT Report Generation](https://arxiv.org/abs/2403.16386) | 2024 | arXiv（预印本） |
| [E3D-GPT: Enhanced 3D Visual Foundation for Medical Vision-Language Model](https://arxiv.org/abs/2410.14200) | 2024 | arXiv（预印本） |
| [Large Language Model With Region-Guided Referring and Grounding for CT Report Generation.](https://pubmed.ncbi.nlm.nih.gov/40215158/) | 2024 | IEEE Transactions on Medical Imaging |
| [MvKeTR: Chest CT Report Generation With Multi-View Perception and Knowledge Enhancement.](https://pubmed.ncbi.nlm.nih.gov/40536849/) | 2024 | IEEE Journal of Biomedical and Health Informatics |
| [Read like a radiologist: Efficient vision-language model for 3D medical imaging interpretation.](https://pubmed.ncbi.nlm.nih.gov/41990528/) | 2024 | Medical Image Analysis |
| [Symbiotic Fusion of Evolving Anatomical Landscapes for Intelligent Diagnostic Narratives](https://doi.org/10.1109/bibm62325.2024.10822272) | 2024 | IEEE International Conference on Bioinformatics and Biomedicine |
| [TGMT: A Terminology-Guided Multi-Task Approach for Lung Cancer CT Report Generation.](https://pubmed.ncbi.nlm.nih.gov/40039464/) | 2024 | IEEE EMBC |
| [Medical Report Generation and Chatbot for COVID_19 Diagnosis Using Open-AI](https://doi.org/10.21203/rs.3.rs-2563448/v1) | 2023 | Research Square（预印本） |
| [AI-Supported Comprehensive Detection and Quantification of Biomarkers of Subclinical Widespread Diseases at Chest CT for Preventive Medicine.](https://pubmed.ncbi.nlm.nih.gov/36360507/) | 2022 | Healthcare |
| [Deep Multi-Objective Learning from Low-Dose CT for Automatic Lung-RADS Report Generation.](https://pubmed.ncbi.nlm.nih.gov/35330417/) | 2022 | Journal of Personalized Medicine |
| [Artificial intelligence to codify lung CT in Covid-19 patients.](https://pubmed.ncbi.nlm.nih.gov/32367319/) | 2020 | La Radiologia Medica |
| [Automatic Detection and Classification of Rib Fractures on Thoracic CT Using Convolutional Neural Network: Accuracy and Feasibility.](https://pubmed.ncbi.nlm.nih.gov/32524787/) | 2020 | Korean Journal of Radiology |
| [Lung-Wise Tuberculosis Analysis and Automatic CT Report Generation with Hybrid Feature and Ensemble Learning](https://www.semanticscholar.org/paper/b4733a72cbab0e28df14b502a067452981b5d59a) | 2020 | Conference and Labs of the Evaluation Forum |
| [A deep learning system that generates quantitative CT reports for diagnosing pulmonary Tuberculosis](https://arxiv.org/abs/1910.02285) | 2019 | arXiv（预印本） |
| [Feature and Deep Learning Based Approaches for Automatic Report Generation and Severity Scoring of Lung Tuberculosis from CT Images](https://www.semanticscholar.org/paper/4f2e7d41677c16ba5ea3958ab61f6f6a87369d3f) | 2019 | Conference and Labs of the Evaluation Forum |
| [Lung Graph-Model Classification with SVM and CNN for Tuberculosis Severity Assessment and Automatic CT Report Generation](https://www.semanticscholar.org/paper/772834c11bfeaf940800181ec332e2e67f35b07e) | 2019 | Conference and Labs of the Evaluation Forum |
| [Integration of Chest CT CAD into the Clinical Workflow and Impact on Radiologist Efficiency.](https://pubmed.ncbi.nlm.nih.gov/30097402/) | 2018 | Academic Radiology |

### 二维及三维来源（31 条）

本组同时涉及原生二维与三维检查来源；三维实验的部位和任务仍需结合全文确认。

| 论文标题 | 年份 | 发表渠道 |
|---|---|---|
| [Automatic CT image report generation based on parallel independent encoding and reverse cross-attention](https://doi.org/10.1049/icp.2025.4651) | 2026 | IET Conference Proceedings |
| [Computer Vision System and Transformer-Based Multimodal Fusion of Medical Images for Enhanced Diagnostic Decision Making](https://doi.org/10.31185/wjcms.543) | 2026 | Wasit Journal of Computer and Mathematics Science |
| [Graph-Supervised Hierarchical Clinical Alignment for Radiology Report Generation with Large Language Models](https://arxiv.org/abs/2608.24121) | 2026 | arXiv（预印本） |
| [MediFusionNet: A Hybrid CNN-Based Multi-Disease Diagnostic Web Platform](https://doi.org/10.36548/jitdw.2026.4.005) | 2026 | Journal of Information Technology and Digital World |
| [Personalized Medicine and Process Optimization: Analysis and Implementation of Intelligent Tools to Support the Clinical Process](https://doi.org/10.15167/wehbe-alaa_phd2026-03-10) | 2026 | University of Genoa 学位论文 |
| [RVLM: Recursive Vision-Language Models with Adaptive Depth](https://arxiv.org/abs/2603.24224) | 2026 | arXiv（预印本） |
| [TriPACT: A Causality-Motivated Multimodal Framework With Active Counterfactual Testing for Radiology Report Generation](https://doi.org/10.1109/access.2026.3701619) | 2026 | IEEE Access |
| [A Medical Multimodal Large Language Model for Pediatric Pneumonia.](https://pubmed.ncbi.nlm.nih.gov/40354198/) | 2025 | IEEE Journal of Biomedical and Health Informatics |
| [A vision attention driven Language framework for medical report generation.](https://pubmed.ncbi.nlm.nih.gov/40155699/) | 2025 | Scientific Reports |
| [Automatic Radiology Report Generation Based on State-Space Model.](https://pubmed.ncbi.nlm.nih.gov/40522799/) | 2025 | IEEE Journal of Biomedical and Health Informatics |
| [Chikitsak 1.0 AI medical Assistant](https://doi.org/10.22541/au.174249329.92063634/v1) | 2025 | 预印本（Wiley） |
| [Comparative evaluation of generative AI models for chest radiograph report generation in the emergency department.](https://pubmed.ncbi.nlm.nih.gov/42268300/) | 2025 | European Radiology |
| [Deep Disease Label-guided Graph Convolutional Network for Medical Report Generation](https://doi.org/10.1145/3722226) | 2025 | ACM Transactions on Knowledge Discovery from Data |
| [Describe Anything in Medical Images](https://arxiv.org/abs/2505.05804) | 2025 | arXiv（预印本） |
| [LACFNet: Locality Aware Cross Modal Fusion Network for Automatic Medical Image Report Generation](https://doi.org/10.1109/acait67930.2025.11522656) | 2025 | 2025 Asian Conference on Artificial Intelligence Technology (ACAIT) |
| [Medical semantic knowledge-integrated multitask learning network for report generation and neoadjuvant chemotherapy response prediction.](https://pubmed.ncbi.nlm.nih.gov/40660946/) | 2025 | Medical Physics |
| [Pneumonia Diagnosis using Deep Learning Optimized with Generative AI for Analysis, Intelligent Report Generation and Recommendations](https://doi.org/10.1109/icscn67106.2025.11308282) | 2025 | 2025 International Conference on Sustainable Communication Networks and Application (ICSCN) |
| [Privacy-Preserving Federated Vision Transformers for Automated Medical Image Analysis and Clinical Report Generation: A Multi-Institutional Healthcare Intelligence Framework](https://doi.org/10.22259/2637-5591.0701004) | 2025 | Research Journal of Nanoscience and Engineering |
| [Soft label-guided transformer for radiology report generation.](https://pubmed.ncbi.nlm.nih.gov/41093123/) | 2025 | Journal of Biomedical Informatics |
| [Advancing Multimodal Medical Capabilities of Gemini](https://arxiv.org/abs/2405.03162) | 2024 | arXiv（预印本） |
| [An End-to-End Pipeline Integrating Segmentation, Anomaly Detection, and Report Generation for Medical Imaging Analysis](https://doi.org/10.1109/icdcc62744.2024.10960883) | 2024 | 2024 First International Conference on Data, Computation and Communication (ICDCC) |
| [An End-to-End Pipeline Integrating Segmentation, Anomaly Detection, and Report Generation for Medical Imaging Analysis](https://doi.org/10.1109/icdcc62744.2024.10961096) | 2024 | International Conference on Data, Computation and Communication (ICDCC) |
| [Bootstrapping Chest CT Image Understanding by Distilling Knowledge from X-ray Expert Models](https://arxiv.org/abs/2404.04936) | 2024 | arXiv（预印本） |
| [Expert-level vision-language foundation model for real-world radiology and comprehensive evaluation](https://arxiv.org/abs/2409.16183) | 2024 | arXiv（预印本） |
| [Hierarchical medical image report adversarial generation with hybrid discriminator.](https://pubmed.ncbi.nlm.nih.gov/38547777/) | 2024 | Artificial Intelligence in Medicine |
| [MedImageInsight: An Open-Source Embedding Model for General Domain Medical Imaging](https://arxiv.org/abs/2410.06542) | 2024 | arXiv（预印本） |
| [Self-improving generative foundation model for synthetic medical image generation and clinical applications.](https://pubmed.ncbi.nlm.nih.gov/39663467/) | 2024 | Nature Medicine |
| [A Novel Deep Learning Model for Medical Report Generation by Inter-Intra Information Calibration.](https://pubmed.ncbi.nlm.nih.gov/37018727/) | 2023 | IEEE Journal of Biomedical and Health Informatics |
| [Clinical-BERT: Vision-Language Pre-training for Radiograph Diagnosis and Reports Generation](https://doi.org/10.1609/aaai.v36i3.20204) | 2022 | AAAI Conference on Artificial Intelligence |
| [Medical-VLBERT: Medical Visual Language BERT for COVID-19 CT Report Generation With Alternate Learning.](https://pubmed.ncbi.nlm.nih.gov/34370672/) | 2021 | IEEE Transactions on Neural Networks and Learning Systems |
| [Auxiliary signal-guided knowledge encoder-decoder for medical report generation.](https://pubmed.ncbi.nlm.nih.gov/36060430/) | 2020 | World Wide Web |

<a id="methods-2d"></a>

## 四、二维相关方法

待完成代表性文献筛选后补充。

<!-- 已展示候选的关联标识，供自动检索去重；不代表独立研究数量。
DOI:10.1109/icce-taiwan71481.2026.11652790
PMID:42940118 ; DOI:10.3390/biomedicines14102312 ; https://pubmed.ncbi.nlm.nih.gov/42940118/
arXiv:2608.05615 ; DOI:10.48550/arxiv.2608.05615
DOI:10.1109/ic-icns68863.2026.11537587
PMID:42193426 ; DOI:10.3390/biomedicines14051103 ; https://pubmed.ncbi.nlm.nih.gov/42193426/
DOI:10.70917/ijcisim-2026-5116
arXiv:2606.00602 ; DOI:10.48550/arxiv.2606.00602
DOI:10.21203/rs.3.rs-10034289/v1
arXiv:2605.31437 ; DOI:10.48550/arxiv.2605.31437
arXiv:2603.15822 ; DOI:10.48550/arxiv.2603.15822
DOI:10.1117/12.3083423
arXiv:2603.23308 ; DOI:10.48550/arxiv.2603.23308
arXiv:2606.25546 ; DOI:10.48550/arxiv.2606.25546
DOI:10.64898/2026.02.21.26346798
PMID:42315314 ; DOI:10.2967/jnumed.126.272362 ; https://pubmed.ncbi.nlm.nih.gov/42315314/
arXiv:2604.10437 ; DOI:10.48550/arxiv.2604.10437
arXiv:2604.24146 ; DOI:10.48550/arxiv.2604.24146
DOI:10.68339/jaims.v1i1.6
arXiv:2608.15004
arXiv:2606.24570 ; DOI:10.48550/arxiv.2606.24570
arXiv:2605.01779 ; DOI:10.48550/arxiv.2605.01779
arXiv:2607.14264 ; DOI:10.48550/arxiv.2607.14264
arXiv:2609.27511 ; DOI:10.48550/arxiv.2609.27511
arXiv:2602.16110
arXiv:2608.00345
PMID:41564843 ; DOI:10.1016/j.resinv.2026.101373 ; https://pubmed.ncbi.nlm.nih.gov/41564843/
arXiv:2604.15231 ; DOI:10.48550/arxiv.2604.15231
PMID:42983219 ; DOI:10.2174/0115734056498625261015050759 ; https://pubmed.ncbi.nlm.nih.gov/42983219/
arXiv:2608.08713 ; DOI:10.48550/arxiv.2608.08713
DOI:10.1109/trpms.2026.3693637
arXiv:2609.31788
arXiv:2605.24371
PMID:42483403 ; DOI:10.34133/research.1343 ; https://pubmed.ncbi.nlm.nih.gov/42483403/
DOI:10.18653/v1/2026.bionlp-1.85
arXiv:2603.00479 ; DOI:10.48550/arxiv.2603.00479
PMID:41894071 ; DOI:10.1007/s11548-026-03608-0 ; arXiv:2601.11075 ; https://pubmed.ncbi.nlm.nih.gov/41894071/
DOI:10.3724/2096-7004.di.2026.0097
PMID:42976478 ; DOI:10.1088/1361-6560/aebd60 ; https://pubmed.ncbi.nlm.nih.gov/42976478/
OpenAlex:W7214809670
PMID:40945174 ; DOI:10.1016/j.media.2025.103786 ; DOI:10.48550/arxiv.2503.02034 ; arXiv:2503.02034 ; https://pubmed.ncbi.nlm.nih.gov/40945174/
DOI:10.1145/3731715.3733287
PMID:40903384 ; DOI:10.1016/j.radi.2025.103152 ; https://pubmed.ncbi.nlm.nih.gov/40903384/
arXiv:2508.05375 ; DOI:10.1109/iccvw69036.2025.00706
DOI:10.1007/978-981-96-3755-3_11
PMID:41083099 ; DOI:10.1016/j.jbi.2025.104931 ; https://pubmed.ncbi.nlm.nih.gov/41083099/
PMID:41209490 ; DOI:10.3389/fradi.2025.1672364 ; https://pubmed.ncbi.nlm.nih.gov/41209490/
arXiv:2511.21042 ; DOI:10.1609/aaai.v40i35.40225 ; DOI:10.48550/arxiv.2511.21042
DOI:10.14711/thesis-hdl152429
arXiv:2507.13993 ; DOI:10.48550/arxiv.2507.13993
DOI:10.3390/computers14110489
PMID:40639153 ; DOI:10.1016/j.cmpb.2025.108907 ; https://pubmed.ncbi.nlm.nih.gov/40639153/
PMID:40652098 ; DOI:10.1038/s41746-025-01807-8 ; https://pubmed.ncbi.nlm.nih.gov/40652098/
arXiv:2409.19330 ; DOI:10.48550/arxiv.2409.19330
arXiv:2408.11965 ; DOI:10.1109/isbi60581.2025.10981073
arXiv:2403.06801 ; DOI:10.1007/978-3-031-72390-2_45 ; DOI:10.48550/arxiv.2403.06801
PMID:38512860 ; DOI:10.1371/journal.pone.0300325 ; https://pubmed.ncbi.nlm.nih.gov/38512860/
arXiv:2403.16386 ; DOI:10.48550/arxiv.2403.16386
arXiv:2410.14200 ; DOI:10.48550/arxiv.2410.14200
PMID:40215158 ; DOI:10.1109/tmi.2025.3559923 ; arXiv:2411.15539 ; https://pubmed.ncbi.nlm.nih.gov/40215158/
PMID:40536849 ; DOI:10.1109/jbhi.2025.3581289 ; DOI:10.48550/arxiv.2411.18309 ; arXiv:2411.18309 ; https://pubmed.ncbi.nlm.nih.gov/40536849/
PMID:41990528 ; DOI:10.1016/j.media.2026.104077 ; DOI:10.48550/arxiv.2412.13558 ; arXiv:2412.13558 ; https://pubmed.ncbi.nlm.nih.gov/41990528/
DOI:10.1109/bibm62325.2024.10822272
PMID:40039464 ; DOI:10.1109/embc53108.2024.10781518 ; https://pubmed.ncbi.nlm.nih.gov/40039464/
DOI:10.21203/rs.3.rs-2563448/v1
PMID:36360507 ; DOI:10.3390/healthcare10112166 ; https://pubmed.ncbi.nlm.nih.gov/36360507/
PMID:35330417 ; DOI:10.3390/jpm12030417 ; https://pubmed.ncbi.nlm.nih.gov/35330417/
PMID:32367319 ; DOI:10.1007/s11547-020-01195-x ; https://pubmed.ncbi.nlm.nih.gov/32367319/
PMID:32524787 ; DOI:10.3348/kjr.2019.0651 ; https://pubmed.ncbi.nlm.nih.gov/32524787/
Semantic Scholar:b4733a72cbab0e28df14b502a067452981b5d59a
arXiv:1910.02285 ; DOI:10.1007/s10489-020-02051-1
Semantic Scholar:4f2e7d41677c16ba5ea3958ab61f6f6a87369d3f
Semantic Scholar:772834c11bfeaf940800181ec332e2e67f35b07e
PMID:30097402 ; DOI:10.1016/j.acra.2018.07.006 ; https://pubmed.ncbi.nlm.nih.gov/30097402/
DOI:10.1049/icp.2025.4651
DOI:10.31185/wjcms.543
arXiv:2608.24121 ; DOI:10.1145/3767308.3835881 ; DOI:10.48550/arxiv.2608.24121
DOI:10.36548/jitdw.2026.4.005
DOI:10.15167/wehbe-alaa_phd2026-03-10
arXiv:2603.24224 ; DOI:10.48550/arxiv.2603.24224
DOI:10.1109/access.2026.3701619
PMID:40354198 ; DOI:10.1109/jbhi.2025.3569361 ; https://pubmed.ncbi.nlm.nih.gov/40354198/
PMID:40155699 ; DOI:10.1038/s41598-025-95666-8 ; https://pubmed.ncbi.nlm.nih.gov/40155699/
PMID:40522799 ; DOI:10.1109/jbhi.2025.3579888 ; https://pubmed.ncbi.nlm.nih.gov/40522799/
DOI:10.22541/au.174249329.92063634/v1
PMID:42268300 ; DOI:10.1007/s00330-026-12648-8 ; arXiv:2512.00271 ; https://pubmed.ncbi.nlm.nih.gov/42268300/
DOI:10.1145/3722226
arXiv:2505.05804
DOI:10.1109/acait67930.2025.11522656
PMID:40660946 ; DOI:10.1002/mp.17925 ; https://pubmed.ncbi.nlm.nih.gov/40660946/
DOI:10.1109/icscn67106.2025.11308282
DOI:10.22259/2637-5591.0701004
PMID:41093123 ; DOI:10.1016/j.jbi.2025.104924 ; https://pubmed.ncbi.nlm.nih.gov/41093123/
arXiv:2405.03162 ; DOI:10.48550/arxiv.2405.03162
DOI:10.1109/icdcc62744.2024.10960883
DOI:10.1109/icdcc62744.2024.10961096
arXiv:2404.04936 ; DOI:10.1109/cvpr52733.2024.01068
arXiv:2409.16183 ; DOI:10.48550/arxiv.2409.16183
PMID:38547777 ; DOI:10.1016/j.artmed.2024.102846 ; https://pubmed.ncbi.nlm.nih.gov/38547777/
arXiv:2410.06542 ; DOI:10.48550/arxiv.2410.06542
PMID:39663467 ; DOI:10.1038/s41591-024-03359-y ; https://pubmed.ncbi.nlm.nih.gov/39663467/
PMID:37018727 ; DOI:10.1109/jbhi.2023.3236661 ; https://pubmed.ncbi.nlm.nih.gov/37018727/
DOI:10.1609/aaai.v36i3.20204
PMID:34370672 ; DOI:10.1109/tnnls.2021.3099165 ; arXiv:2108.05067 ; https://pubmed.ncbi.nlm.nih.gov/34370672/
PMID:36060430 ; DOI:10.1007/s11280-022-01013-6 ; arXiv:2006.03744 ; https://pubmed.ncbi.nlm.nih.gov/36060430/
-->

<a id="automatic-candidates"></a>

## 自动检索候选（机器生成，待人工审阅整理）

> 本区由 GitHub Actions 每周检索 arXiv / PubMed 生成。候选经审阅后再移入相应章节。

## 维护说明

- 本轮模型条目来自 2026-11-20 当前筛选表中“三维影像来源”“二维及三维”两张工作表，仅导入“保留模型候选”；数据集、评价、背景、待核及纯二维条目未在本轮导入。
- 新增或更新文献时填写标题链接、年份和发表渠道。年份与发表渠道应注明所对应的版本；后续统一正式发表信息时，再逐条核对。
- 自动检索保留每周一 02:20 UTC（北京时间 10:20）运行、生成候选 PR 并由人工审阅的方式；本轮仅适配章节结构，现有 CT / MRI 检索范围暂时沿用，后续再按胸部主题调整。
- 自动候选移入上方章节后，脚本依据 arXiv、PMID、DOI 清理重复项；删除候选表示放弃本次候选，历史记录仍用于避免重复推送。

## 更新记录

- **2026-11-20**：按综述章节重建页面，以本轮筛选表中的 104 条模型候选替换旧文献列表；数据集、评价与纯二维相关方法待后续补充。
