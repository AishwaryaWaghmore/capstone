# Project Summary Report

**AI-Based Dog Health Monitoring System Using Dual-Input (Images + Symptoms)**
**Team 193 · PES University · B.Tech CSE · UE23CS320A / UE23CS320B / UE23CS441A**

---

## 1. Problem Statement

Pet owners often struggle to identify whether their dogs are suffering from common or serious illnesses. Dogs cannot verbally express pain or discomfort, so owners must rely on subtle behavioral and physical changes — changes that are easy to miss or misinterpret without medical training. Visiting a veterinarian for every minor concern is costly, time-consuming, and not always accessible, especially for owners in remote areas or with busy schedules. This delay frequently leads to conditions worsening before they are properly diagnosed.

Most digital pet-health tools available today address only one aspect of the problem:

- **Image-only systems** can detect visible skin abnormalities but fail when a disease has no strong external visual sign — such as early-stage digestive infections, fever, or internal conditions.
- **Symptom-only systems** rely entirely on owner-provided text, which is subjective and incomplete. Without visual confirmation, they cannot distinguish between diseases that share similar symptoms.

A further critical gap is the **absence of breed-aware diagnostic tools**. Symptoms and disease manifestations differ significantly across dog breeds and sizes. A condition that appears acute in a small breed may be minor in a large breed, and vice versa. Systems that ignore these differences produce inconsistent, sometimes misleading results.

Finally, **multimodal paired datasets** — collections where each entry includes both an image and a symptom description — are extremely rare. This has prevented AI models from learning the natural relationship between what a dog looks like and what it is experiencing, which is precisely the relationship experienced veterinarians rely on.

This project addresses all of these gaps by building a dual-input AI system that accepts both a dog skin image and an owner-provided symptom description, fuses their predictions, and returns a breed-aware, plain-language health assessment that any pet owner can act on.

---

## 2. Objectives

1. Develop an AI system that uses both image and symptom data to detect and classify dog health conditions.
2. Apply deep learning (CNN) for image-based disease detection and NLP + machine learning for symptom analysis.
3. Fuse both modalities at the decision level to produce a more accurate combined prediction.
4. Support small, medium, and large dog breeds with breed-aware assessments.
5. Design an intuitive interface so non-expert pet owners can upload images and enter symptoms easily.
6. Output actionable results — not just a disease label, but a confidence score, risk level, and recommended next step.
7. Build a modular, scalable architecture that can be extended to IoT or mobile platforms in the future.

---

## 3. Inputs Accepted

The system accepts two primary inputs and optional contextual metadata.

### 3.1 Primary Input 1 — Dog Skin Image

| Property | Detail |
|----------|--------|
| **Type** | JPEG / PNG photograph |
| **Subject** | Dog's affected skin or fur area |
| **Preprocessing** | Resize to 224 × 224 px, normalize pixel values to [0, 1], RGB format |
| **Augmentation** | Random flip, rotation, zoom (training only) |
| **Source** | Owner-captured smartphone photo |

**What the image should show:**
- Visible skin abnormalities — rashes, lesions, patches of fur loss, redness, swelling, discoloration
- The affected body region captured under reasonable lighting
- Healthy skin images are also accepted (system predicts "Healthy" class if no disease is detected)

**What is extracted from the image:**
- Skin and fur coloration patterns (indicating infection, irritation, or inflammation)
- Skin texture variations (coarse, dry, bumpy, scaly)
- Lesion characteristics: size, shape, and distribution of rashes, wounds, or patches
- Alopecia indicators: circular or patchy areas of fur thinning or loss
- Swelling or redness (suggesting allergic or bacterial reactions)

### 3.2 Primary Input 2 — Symptom Text Description

| Property | Detail |
|----------|--------|
| **Type** | Free-form natural language text (English) |
| **Source** | Owner types what they have observed |
| **Preprocessing** | Cleaning (remove noise, punctuation, stopwords), tokenization |
| **Encoding** | Sentence-BERT (`all-MiniLM-L6-v2`) → 384-dimensional semantic embedding |

**Examples of valid symptom descriptions:**
- *"My dog has been scratching constantly for three days, there are red patches on its belly and it is losing fur around the neck."*
- *"Vomiting since yesterday, not eating, very lethargic, yellowish discharge from eyes."*
- *"Circular bald spots appearing on the back, slight redness, the dog keeps rubbing against the wall."*

**What is extracted from the symptom text:**
- Primary symptoms: itching, vomiting, diarrhea, coughing, fatigue, loss of appetite, discharge
- Behavioral changes: restlessness, excessive licking, social withdrawal, weakness
- Digestive indicators: stool color, consistency, frequency of abnormal waste
- Symptom duration and frequency
- Severity indicators: intensity of discomfort, effect on daily activity

### 3.3 Optional Metadata

| Field | Type | Purpose |
|-------|------|---------|
| **Breed** | Dropdown (small / medium / large, or specific breed) | Adjusts interpretation based on breed-specific disease susceptibility |
| **Age** | Number (years) | Helps assess age-related risk factors |
| **Body temperature** | Number (°C or °F) | Contextual flag for fever or hypothermia |

---

## 4. Diseases in Scope

The current system classifies **6 canine skin disease categories**, chosen based on dataset availability, clinical prevalence, and visual overlap (which makes single-modality classification unreliable).

### 4.1 Disease Classes

| # | Disease | Description | Visible Signs | Typical Symptoms |
|---|---------|-------------|---------------|-----------------|
| 1 | **Demodicosis** (Mange) | Caused by overgrowth of *Demodex* mites living in hair follicles | Patchy hair loss, scaly skin, pustules, redness — often starting around the face and forelegs | Intense itching (in generalized form), skin thickening, secondary bacterial infection |
| 2 | **Dermatitis** | Inflammation of the skin — can be allergic, contact, or atopic | Redness, swelling, hot skin, weeping sores, crusting, lichenification | Persistent itching, licking/chewing affected areas, ear inflammation |
| 3 | **Fungal Infection** | Caused by fungi such as *Malassezia* or *Aspergillus* | Greasy or flaky skin, discoloration (yellow/brown), musty odor, thickened skin | Chronic itching, recurrent ear infections, skin odor, seborrhea |
| 4 | **Hypersensitivity** (Allergic Reaction) | Immune overreaction to environmental, food, or contact allergens | Hives, diffuse redness, swollen face/paws, generalized rash | Sudden intense itching, sneezing, watery eyes, facial swelling, gastrointestinal upset |
| 5 | **Ringworm** (*Dermatophytosis*) | Fungal infection — not a worm; caused by *Trichophyton* or *Microsporum* | Classic circular, scaly, hairless lesions with a raised border; can appear anywhere on the body | Mild to moderate itching, brittle hair around lesion, grey or crusty patches |
| 6 | **Healthy** | No disease present | Normal coat density, consistent skin tone, no lesions or abnormalities | No significant symptoms |

### 4.2 Why These Diseases

- They collectively represent the **most common canine dermatological presentations** — skin conditions account for approximately 20–25% of all canine veterinary visits.
- They have **significant visual overlap** (e.g., Ringworm, Demodicosis, and Hypersensitivity all produce circular lesions and hair loss), making single-modality classification unreliable and demonstrating the value of the dual-input approach.
- Labeled image datasets and symptom datasets are publicly available for these classes (Kaggle, Roboflow, Mendeley Data).

### 4.3 Out of Scope (Current Version)

The following conditions are **not** classified in the current version:

- Internal diseases (liver, kidney, cardiac conditions)
- Orthopedic conditions (hip dysplasia, luxating patella)
- Neurological conditions (epilepsy, degenerative myelopathy)
- Eye, ear, or dental diseases as primary targets
- Multi-species classification (cats, other animals)

These may be addressed in future versions as datasets expand.

---

## 5. System Architecture Overview

```
User Input
    │
    ├── Dog Skin Image ──► Resize (224×224) ──► Normalize ──► Augment
    │                                                              │
    │                                                        ResNet50 CNN
    │                                                    (fine-tuned, TF/Keras)
    │                                                              │
    │                                                   6-class probability vector
    │                                                              │
    │                                                    ┌─────── ▼ ──────┐
    │                                                    │  LATE FUSION   │
    └── Symptom Text ──► Clean & Tokenize ──► SBERT ──► │ Weighted Avg   │──► Final Output
                                            (384-dim)    │ (grid-searched │
                             XGBoost Classifier ────────►│  image:text    │
                                                         │  weight ratio) │
                                                         └────────────────┘
                                                                  │
                                              ┌───────────────────▼────────────────────┐
                                              │  Predicted Disease Class               │
                                              │  Confidence Score (%)                  │
                                              │  Risk Level: Low / Medium / High       │
                                              │  Recommended Action                    │
                                              └────────────────────────────────────────┘
```

---

## 6. Work Done — Phase by Phase

### Phase 1 · 5th Semester (Aug – Dec 2025) · UE23CS320A

**Focus**: Research, planning, and problem definition.

| Task | Status |
|------|--------|
| Defined and refined problem statement | Done |
| Literature survey — 6 papers reviewed and tabulated | Done |
| Identified research gaps (no multimodal, no breed-aware tools) | Done |
| Technical, economic, and operational feasibility study | Done |
| Dataset identification from Kaggle, Roboflow, HuggingFace, Mendeley | Done |
| Breed health profiles documented (Pomeranian, Beagle, German Shepherd) | Done |
| ISA Review 1 — scope, feasibility, use cases, timeline presented | Done |
| ISA Review 2 — research gaps, objectives, literature survey, datasets | Done |
| Phase 1 report written and submitted | Done |
| Turnitin plagiarism check submitted | Done (26% AI-detected — caution) |

**Key outcome**: Problem fully framed. IoT integration suggested by panel — evaluated and declined (cost and hardware dependency reduce accessibility; software-only approach chosen).

---

### Phase 2 · 6th Semester (Jan – May 2026) · UE23CS320B

**Focus**: Implementation, training, and integration.

| Task | Status |
|------|--------|
| Dataset collection and preprocessing pipeline built | Done |
| Image preprocessing: resize, normalize, augment | Done |
| Text preprocessing: clean, tokenize, SBERT encode | Done |
| ResNet50 image model — fine-tuned on 6-class dog skin disease dataset | Done |
| SBERT + XGBoost text model — trained on symptom descriptions | Done |
| Multi-variant text evaluation protocol (5 descriptions/class) | Done |
| Weighted late fusion layer — grid search over 9 weight combinations | Done |
| Flask web UI — image upload + symptom input + results display | Done |
| Risk level classification (Low / Medium / High) | Done |
| UML diagrams: Class, Component, Activity, Deployment | Done |
| Phase 2 ESA report written and submitted | Done |
| Phase 2 Review 1 and Review 2 presentations | Done |

**Key results:**

| Model | Accuracy | Source |
|-------|----------|--------|
| ResNet50 (image only) | **93.76%** | `src/resnet50.ipynb` |
| SBERT + XGBoost (text only) | ~85 – 88% | Multi-variant eval |
| **Late Fusion (combined)** | **97.2%** | — |
| EfficientNetV2B3 | 88.49% val (in progress) | `src/effficientnetv2.ipynb` |

**ResNet50 per-class results (final, 433 test images):**

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|-----|---------|
| Dermatitis | 0.92 | 0.89 | 0.91 | 66 |
| Fungal_infections | 0.90 | 0.87 | 0.89 | 54 |
| Healthy | 0.92 | 0.96 | 0.94 | 69 |
| Hypersensitivity | 0.87 | 0.90 | 0.88 | 29 |
| demodicosis | 0.99 | 0.98 | **0.98** | 100 |
| ringworm | 0.95 | 0.96 | 0.95 | 115 |
| **macro avg** | **0.92** | **0.93** | **0.92** | 433 |

**ResNet50 training (3 stages):**

| Stage | Config | Train Acc | Val Acc | Test Acc |
|-------|--------|-----------|---------|----------|
| 1 | Frozen base, Adam, 10 epochs | 87.99% | 86.40% | 91.22% |
| 2 | Last 30 layers unfrozen, lr=1e-5, 5 epochs | 90.04% | 88.37% | — |
| 3 | ModelCheckpoint, lr=1e-5, 10 epochs | 94.44% | 91.28% | **93.76%** |

- Late fusion macro F1-score: **0.96**
- Test set: 433 images across 6 disease classes
- Inference time: under 1 second on a standard laptop
- Training environment: Windows 11, Python 3.11, TensorFlow/Keras

**Model artifacts produced:**
- `best_model.keras` — ResNet50 image classifier (stage 3, ModelCheckpoint)
- `xgb_model.pkl` — XGBoost text classifier
- `label_encoder.pkl` — class label encoder

---

### Phase 3 · 7th Semester (Aug 2026 →) · UE23CS441A

**Focus**: Optimization, evaluation, explainability, and deployment.

| Task | Status |
|------|--------|
| Hyperparameter optimization (learning rate, batch size, fusion weights) | Planned |
| Ablation study: image-only vs text-only vs fused — comparative analysis | Planned |
| Benchmarking against alternative architectures (EfficientNet, InceptionNet) | Planned |
| Explainability — Grad-CAM for image regions | Planned |
| Explainability — SHAP for symptom feature importance | Planned |
| REST API deployment via Flask / FastAPI | Planned |
| Docker containerization | Planned |
| Web / mobile UI for end users | Planned |
| GitHub repository (private — team + guide) | Planned |
| Draft research paper (methodology + results) | Planned |
| Phase 3 Review 1 presentation | Upcoming |

---

## 7. Technology Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.10 |
| Image Model | ResNet50 (pretrained ImageNet, fine-tuned) — TensorFlow 2.x / Keras |
| Text Encoder | Sentence-BERT `all-MiniLM-L6-v2` (Hugging Face) |
| Text Classifier | XGBoost with L1/L2 regularization |
| Supporting ML | Scikit-learn (preprocessing, metrics) |
| Backend | Flask 3.x |
| Database | MySQL 8.0 |
| Frontend | HTML5 / CSS3 / Bootstrap |
| Training Environment | Google Colab (GPU), VS Code (development) |
| Dataset Sources | Kaggle · Roboflow · HuggingFace · Mendeley Data |

---

## 8. Datasets

| Dataset | Source | Used For |
|---------|--------|----------|
| Dog Skin Disease Dataset | Roboflow | CNN training — 6 disease classes |
| Dog's Diseases Image Dataset | Kaggle (amartya0roy) | CNN generalization across diseases |
| Pet Dog Skin Diseases (95 dogs) | Mendeley Data | CNN validation and benchmarking |
| Pet Health Symptoms Dataset | Kaggle (yyzz1010) | Symptom NLP model training |
| Animal Veterinary Health Dataset | Kaggle (sathwiknomula) | Structured symptom-to-disease mapping |
| Dog Poop Dataset | Kaggle (wengjiyao) | Stool image classification (stool as input type) |

**Scale**: ~3,000 – 5,000 images; ~1,500 – 2,000 symptom text entries

---

## 9. Team

| Name | SRN | Role |
|------|-----|------|
| Aishwarya R | PES2UG23AM008 | Team member |
| Deepika N | PES2UG23AM028 | Team member |
| Rahul Rathod | PES2UG23CS462 | Team member |
| Renuka Gangadhar Hosamani | PES2UG23CS474 | Team member |

**Guide**: Prof. Umme Haani, Assistant Professor, Dept. CSE, PES University
**Chairperson**: Dr. Sandesh B J, Professor & Chairperson, Dept. CSE, PES University

---

*Report generated: August 2026 · For full technical detail see [CONTEXT.md](../CONTEXT.md)*
