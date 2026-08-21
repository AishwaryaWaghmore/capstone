# Project Context — AI-Based Dog Health Monitoring System

## Identity

| Field | Value |
|-------|-------|
| **Project Title** | AI-Based Dog Health Monitoring System Using Dual-Input (Images + Symptoms) for Small, Medium, and Large Breeds |
| **Project ID** | Team 193 |
| **University** | PES University, Electronic City, Bengaluru — 560 100 |
| **Department** | Computer Science & Engineering |
| **Guide** | Prof. Umme Haani (Assistant Professor, Dept. CSE) |
| **Chairperson** | Dr. Sandesh B J |

## Team

| Name | SRN |
|------|-----|
| Aishwarya R | PES2UG23AM008 |
| Deepika N | PES2UG23AM028 |
| Rahul Rathod | PES2UG23CS462 |
| Renuka Gangadhar Hosamani | PES2UG23CS474 |

---

## Phase Timeline

| Phase | Course Code | Semester | Period | Status |
|-------|-------------|----------|--------|--------|
| Phase 1 | UE23CS320A | 5th sem | Aug – Dec 2025 | Completed |
| Phase 2 | UE23CS320B | 6th sem | Jan – May 2026 | Completed |
| Phase 3 | UE23CS441A | 7th sem | Aug 2026 → | In Progress |

---

## Problem Statement

Pet owners cannot reliably identify dog illnesses early because:
- Most AI tools are **single-modality** — either image-based OR symptom-text-based, never both
- No **breed-aware** (small / medium / large) diagnostic tools exist
- **Multimodal paired datasets** (image + symptom text together) are extremely rare
- Existing tools are too technical for non-expert pet owners

**Goal**: A hybrid multimodal AI system that fuses dermoscopic skin images and owner-described symptom text to classify canine skin diseases more accurately than any single-modality approach, while being practical for everyday pet owners.

---

## What the System Does

1. User uploads a dog skin image and types a symptom description
2. Image branch classifies the image using ResNet50
3. Text branch encodes symptoms with SBERT and classifies using XGBoost
4. Both probability vectors are fused via weighted late fusion
5. System outputs: **disease class + confidence score + risk level + recommended action**

---

## Disease Classes (6 total)

Demodicosis · Dermatitis · Fungal Infections · Hypersensitivity · Ringworm · (6th class)

---

## System Architecture

```
                    ┌─────────────────────────────────────┐
                    │       DATA INGESTION & PREPROCESSING │
       Dog Image ──►│  Resize 224×224 | Normalize | Augment│
  Symptom Text  ──►│  Clean | Tokenize | SBERT Encode      │
                    └───────────┬─────────────┬────────────┘
                                │             │
                    ┌───────────▼──┐  ┌───────▼─────────────┐
                    │  IMAGE BRANCH │  │    TEXT BRANCH       │
                    │  ResNet50 CNN │  │  SBERT + XGBoost     │
                    │  (TF/Keras)   │  │  (HuggingFace + XGB) │
                    │  6-class prob │  │  6-class prob vector │
                    └───────────┬──┘  └───────┬─────────────┘
                                │             │
                    ┌───────────▼─────────────▼────────────┐
                    │     WEIGHTED LATE FUSION LAYER        │
                    │  Grid-searched image:text weight ratio│
                    └───────────────────┬──────────────────┘
                                        │
                    ┌───────────────────▼──────────────────┐
                    │              OUTPUT                   │
                    │  Disease Class | Confidence Score     │
                    │  Risk Level (Low/Med/High)            │
                    │  Recommended Action                   │
                    └──────────────────────────────────────┘
```

---

## Model Details

### Image Branch — ResNet50
- Pretrained on ImageNet, fine-tuned for 6-class canine skin disease
- Input: 224 × 224 RGB images
- Augmentation: random flip, rotation, zoom
- Output: 6-class softmax probability vector
- Saved as: `best_model.keras` (ModelCheckpoint — best validation accuracy)
- Framework: TensorFlow 2.x / Keras

### Text Branch — SBERT + XGBoost
- Encoder: `sentence-transformers/all-MiniLM-L6-v2` → 384-dimensional embeddings
- Classifier: XGBoost with L1/L2 regularization, early stopping (patience=25)
- Evaluation: Multi-variant protocol (5 symptom description variants per disease class — prevents single-phrase memorization)
- Saved as: `xgb_model.pkl`, `label_encoder.pkl` (joblib)

### Late Fusion
- Strategy: Weighted probability averaging at decision level
- Weight selection: Grid search across 9 image-text combinations
- Dynamic weighting: Image weighted higher when visual evidence is strong; text weighted higher when symptom description is more informative

---

## Results (Phase 2)

| Model | Accuracy | Notes |
|-------|----------|-------|
| ResNet50 (image only) | **93.76%** | 433 test images — `src/resnet50.ipynb` |
| SBERT + XGBoost (text only) | ~85–88% | Multi-variant evaluation |
| **Late Fusion** | **97.2%** | Macro F1 = 0.96 |
| EfficientNetV2B3 (Phase 3 benchmark) | 88.49% val (frozen, 10 epochs) | `src/effficientnetv2.ipynb` — in progress |

### ResNet50 Per-Class Results (Final, 433 test images)

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|-----|---------|
| Dermatitis | 0.92 | 0.89 | 0.91 | 66 |
| Fungal_infections | 0.90 | 0.87 | 0.89 | 54 |
| Healthy | 0.92 | 0.96 | 0.94 | 69 |
| Hypersensitivity | 0.87 | 0.90 | 0.88 | 29 |
| demodicosis | 0.99 | 0.98 | **0.98** | 100 |
| ringworm | 0.95 | 0.96 | 0.95 | 115 |
| **macro avg** | **0.92** | **0.93** | **0.92** | 433 |
| **weighted avg** | **0.94** | **0.94** | **0.94** | 433 |

### ResNet50 Training Summary (3-stage fine-tuning)

| Stage | Config | Train Acc | Val Acc | Test Acc |
|-------|--------|-----------|---------|----------|
| Stage 1 | Frozen base, Adam, 10 epochs | 87.99% | 86.40% | 91.22% |
| Stage 2 | Last 30 layers unfrozen, lr=1e-5, 5 epochs | 90.04% | 88.37% | — |
| Stage 3 | ModelCheckpoint, lr=1e-5, 10 epochs | 94.44% | 91.28% | **93.76%** |

- Inference: < 1 second on standard laptop (image ~0.3s, SBERT ~50ms, XGBoost ~1ms)
- Training: Windows 11, Python 3.11, TensorFlow/Keras (Renuka's machine)
- Fixed seed: `SEED=42` for reproducibility

---

## Technology Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.10 |
| Deep Learning (Image) | TensorFlow 2.x / Keras, PyTorch + torchvision |
| Image Model | ResNet50 (ImageNet pretrained, fine-tuned) |
| NLP / Text Model | Hugging Face `sentence-transformers` (SBERT all-MiniLM-L6-v2) |
| Text Classifier | XGBoost, Scikit-learn |
| Alternative ML | Random Forest, TF-IDF (explored) |
| Backend | Flask 3.x (FastAPI planned for Phase 3) |
| Database | MySQL 8.0 |
| Frontend | HTML5 / CSS3 / Bootstrap |
| Dev / Training | VS Code, Google Colab (GPU) |
| Dataset Sources | Kaggle, Roboflow, HuggingFace, Mendeley Data |
| Deployment (planned) | Docker, REST API |

All tools are 100% open source — no licensing cost.

---

## Source Code

| File | Description |
|------|-------------|
| `src/resnet50.ipynb` | ResNet50 training — 3-stage fine-tuning, augmentation, confusion matrix, per-class report |
| `src/effficientnetv2.ipynb` | EfficientNetV2B3 training — Phase 3 benchmarking comparison (in progress) |

## Datasets

### External Datasets (Source)

| Dataset | Source | Use |
|---------|--------|-----|
| Dog Skin Disease Dataset | Roboflow | CNN training (6 disease classes) |
| Dog's Diseases Image Dataset | Kaggle (amartya0roy) | CNN generalization |
| Classification of Pet Dog Skin Diseases (95 dogs) | Mendeley Data | CNN benchmarking |
| Pet Health Symptoms Dataset | Kaggle (yyzz1010) | Symptom NLP model |
| Animal Veterinary Health Dataset | Kaggle (sathwiknomula) | Structured health records |
| Dog Poop Dataset | Kaggle (wengjiyao) | Stool image classification |

### processed_image/ — Actual Training Data (on disk)

Split into `train/` / `valid/` / `test/` with 6 class subdirectories.

| Class | Train | Valid | Test | Total |
|-------|-------|-------|------|-------|
| demodicosis | 588 | 174 | 100 | 862 |
| Dermatitis | 546 | 175 | 66 | 787 |
| Fungal_infections | 375 | 97 | 54 | 526 |
| Healthy | 492 | 139 | 69 | 700 |
| Hypersensitivity | 230 | 63 | 29 | 322 |
| ringworm | 791 | 212 | 115 | 1118 |
| **Total** | **3022** | **860** | **433** | **4315** |

> Class imbalance: Hypersensitivity is the most underrepresented class (322 total, 29 test). Ringworm is the largest (1118 total). This should be addressed in Phase 3 fine-tuning.

---

## Features Extracted

### Image Features
- Skin/fur coloration changes (infection, irritation, inflammation)
- Skin texture variations (coarse, dry, bumpy)
- Lesion characteristics: size, shape, distribution of rashes/wounds/patches
- Alopecia: circular/patchy fur loss areas
- Swelling or redness
- Image metadata: resolution, lighting, background

### Text (Symptom) Features
- Primary symptoms: vomiting, diarrhea, itching, coughing, fatigue, loss of appetite
- Behavioral changes: restlessness, weakness, excessive licking, social withdrawal
- Digestive indicators: stool color, consistency, frequency
- Symptom duration and severity

### Breed & Metadata Features
- Breed type (Labrador, German Shepherd, Beagle, Pug, Pomeranian, …)
- Breed size: Small / Medium / Large
- Age and gender (when available)

### Ground Truth Labels
- Disease category (dermatitis, mange, ear infection, malnutrition, allergy, …)
- Health status: healthy / mildly affected / severe
- Symptom cluster mapping (for differential diagnosis)

---

## Breed Health Profiles (Reference)

| Breed | Size | Key Health Issues |
|-------|------|-------------------|
| Pomeranian | Small (1.5–3.5 kg) | Dental problems, luxating patella, tracheal collapse, hypoglycemia, skin allergies |
| Beagle | Medium (9–11 kg) | Ear infections, obesity, epilepsy, hypothyroidism, IVDD |
| German Shepherd | Large (22–40 kg) | Hip/elbow dysplasia, degenerative myelopathy, bloat, skin allergies |

---

## Phase-by-Phase Summary

### Phase 1 (5th sem, Aug–Dec 2025) — UE23CS320A
- Framed problem statement
- Conducted literature survey (6 papers)
- Identified datasets (Kaggle, Roboflow, HuggingFace)
- Feasibility study (technical, economic, operational)
- Panel Review 1 feedback: improve Gantt chart, more detailed module explanation
- Panel Review 2 feedback: suggested IoT sensors → team evaluated and declined (cost/hardware dependency; software-only approach maintained)
- Deliverables: Problem statement, literature survey, dataset plan, Phase 2 plan
- Turnitin: 26% AI-detected (submitted Nov 20, 2025)

### Phase 2 (6th sem, Jan–May 2026) — UE23CS320B
- Implemented ResNet50 image branch (TF/Keras)
- Implemented SBERT + XGBoost text branch (initially Logistic Regression, upgraded to XGBoost)
- Implemented weighted late fusion layer
- Built Flask web UI (image upload + symptom input + results display)
- Achieved 97.2% fused accuracy on 433 test images
- Designed UML diagrams: Master Class Diagram, Component Diagram, Activity Diagram, Deployment Diagram
- Deliverables: Functional multimodal prototype + full ESA report

### Phase 3 (7th sem, Aug 2026 onward) — UE23CS441A
**Planned work:**
- Hyperparameter optimization (learning rates, batch sizes, fusion weights)
- Ablation study: image-only vs text-only vs fused (comparative analysis)
- Quantitative benchmarking vs alternative architectures
- Explainability module: Grad-CAM (image regions) + SHAP (symptom importance)
- REST API deployment via Flask / FastAPI
- Docker containerization for consistent environments
- Web/mobile UI for end users
- GitHub repo with full codebase (private — team + guide only)
- Draft research paper (methodology + results)

---

## Literature Survey

| # | Paper | Year | Method | Result | Limitation |
|---|-------|------|--------|--------|------------|
| 1 | Deep Learning-Based Pet Disease Diagnosis Using Skin and Fur Images (Kumar, Sharma, Gupta) | 2023 | CNN (ResNet50) | 91% accuracy | Image-only |
| 2 | Pet Care AI: Smartphone-Based Health Monitoring Tool (Patel, Nair, Joshi) | 2021 | Rule-based expert system | Remote self-check | No ML/image |
| 3 | PawSense: AI-IoT Smart Pet Care (Aravind G., Sasirekha, Jeeva, Selvaganesh) | 2025 | AI + IoT + blockchain + Flutter | Real-time anomaly detection | IoT-only; no image+symptom fusion |
| 4 | Dog Health Score via AI (S-C Kim & S. Kim) | 2024 | Activity sensors + AI Health Score | 87.5% concordance with vet | Sensor behavioral data only |
| 5 | Multimodal Fusion for Veterinary Disease (L. Chen, M. Zhao, Y. Li) | 2024 | CNN (images) + LSTM (text) | +12% over single-modal | Livestock only; not user-facing |
| 6 | Pet Pulse: TFLite Dog Diseases (Abirami & Momithasree) | 2025 | TFLite mobile app (skin + pulse + symptoms) | Mobile accessibility | Limited dataset; partial multimodal |

**Research gaps addressed by this project**:
- No existing system combines both image AND symptom modalities for dogs
- No breed-aware (small/medium/large) models
- No multimodal paired datasets — this project creates synthetic pairing
- Existing multimodal work (Chen et al.) targets livestock, not companion animals

---

## Related Papers in Repository (`related_doc/`)

1. **PawSense** (ICAISS-2025, Aravind G. et al.) — IoT smart collars + Flutter app + blockchain security + cloud-edge architecture. Referenced for IoT integration context.
2. **AI-Enabled Safe and Scalable Pet Care** (ICICCS-2025, Aravind G. et al.) — Modular IoT-based pet health framework; 95.6% accuracy. Referenced for distributed architecture context.

---

## Functional Requirements

- Upload pet image
- Enter symptom description (text)
- Select breed category (small / medium / large)
- Generate disease prediction
- Classify severity (Mild / Moderate / Severe)
- Display home care suggestions
- Show nearby veterinary clinics
- Allow appointment booking request

## Non-Functional Requirements

- Response time < 5 seconds
- Prediction accuracy > 80% (prototype goal — **exceeded at 97.2%**)
- Secure user data handling (local processing in Phase 2; TLS + RBAC planned for Phase 3)
- Scalable modular architecture
- User-friendly interface for non-expert pet owners

---

## Design Decisions & Rationale

| Decision | Rationale |
|----------|-----------|
| Late fusion (decision-level) over early fusion | Allows independent optimization of each branch; easier to debug; modular |
| SBERT over TF-IDF/BoW | Captures semantic context, not just keyword frequency; handles diverse user input |
| XGBoost over Logistic Regression | Better regularization, interpretability via feature importance, robust with limited training data |
| ResNet50 over custom CNN | Transfer learning from ImageNet gives strong visual priors; well-established baseline |
| Software-only (no IoT) | IoT increases cost and hardware dependency; reduces accessibility — panel suggestion declined |
| Multi-variant text evaluation | Prevents artificially inflated text accuracy from single-phrase memorization |

---

## University Submission Requirements

- Format: A4, 1.5 line spacing, Times New Roman 12pt body
- Margins: Left/Right/Top/Bottom = 2.00 cm each
- Section numbers: Chapter (18pt centered) → Section (16pt bold, left) → Subsection (14pt bold, left)
- Plagiarism: Max **15%** allowed (checked at PESU library via Turnitin)
- Phase 1 Turnitin result: 26% AI-detected (caution — above threshold)

---

## Repository Structure

```
capstone/
├── README.md
├── CONTEXT.md                          ← this file
├── docs/
│   ├── 5sem/                           ← Phase 1 documents
│   │   ├── 5-sem-report/               ← Full Phase 1 report (pages 1–10+)
│   │   ├── capstone_project_review-1   ← ISA Review 1 PPT
│   │   ├── Capstone_Project_Phase-1_Review-2 ← ISA Review 2 PPT
│   │   ├── Team193_phase1_ISAReview1   ← ISA Review 1 PPT (final)
│   │   ├── Team193_phase1_ISAReview2   ← ISA Review 2 PPT (final)
│   │   ├── Team-193_capstone-phase-1   ← Turnitin submission
│   │   ├── Dog_Breeds_Health_Profile_Capstone ← Breed reference doc
│   │   └── Pet_Health_Datasets_With_Examples  ← Dataset reference doc
│   ├── 6sem/                           ← Phase 2 documents
│   │   ├── esa_report_6th_sem          ← Full Phase 2 ESA report
│   │   ├── Capstone_Project_Phase_2_review_1_final ← Phase 2 Review 1 PPT
│   │   ├── phase_2_final_review_2_ppt  ← Phase 2 Review 2 PPT
│   │   ├── Review_2_UE23CS320B_...     ← Phase 2 Review 2 template PPT
│   │   └── 6thsem_Weekly_Report        ← Weekly report template
│   └── sem7/                           ← Phase 3 documents
│       └── Capstone_Project_Phase3_Review1_UE23CS441A ← Phase 3 Review 1 template
├── images/
│   ├── image2.jpeg
│   └── report_image.jpg
└── related_doc/
    ├── PawSense_AI-IoT_Enabled_Smart_Pet_Care_... ← Related IEEE paper
    └── AI-Enabled_Safe_and_Scalable_Pet_Care_...  ← Related IEEE paper
```
