# AI-Based Dog Health Monitoring System
### Using Dual-Input (Images + Symptoms) for Small, Medium, and Large Breeds

**Team 193 · PES University · B.Tech CSE**
**Guide:** Prof. Umme Haani | **Project ID:** 193

---

## Problem Statement

Pet owners often struggle to identify whether their dogs are suffering from common or serious illnesses. Dogs cannot verbally express pain or discomfort, so owners must rely on subtle behavioral and physical changes — changes that are easy to miss or misinterpret without medical training. Visiting a veterinarian for every minor concern is costly, time-consuming, and not always accessible, especially for owners in remote areas or with busy schedules. This delay in seeking medical attention often leads to conditions worsening before they are properly diagnosed.

Most digital pet-health tools available today address only one aspect of the problem. Image-based systems can detect visible abnormalities like skin lesions or rashes, but fail entirely when the disease has no strong external visual sign — such as digestive infections, fever, or early-stage internal conditions. Symptom-based tools, on the other hand, rely solely on the owner's text description, which is inherently subjective and incomplete; without visual confirmation, they cannot distinguish between diseases that share similar symptoms.

A further limitation is the absence of breed-aware diagnostic tools. Symptoms and disease manifestations differ significantly across dog sizes and breeds. A condition that appears acute in a small breed may be minor in a large breed, and vice versa. Single-input systems that do not account for these differences produce inconsistent and sometimes misleading results.

Finally, multimodal datasets that pair both images and symptom descriptions together are extremely rare. This separation has prevented AI models from learning the natural relationship between what a dog looks like and what it is experiencing — a relationship that experienced veterinarians routinely use when making diagnoses.

**This project addresses all of these gaps** by building a dual-input AI system that accepts both a dog's skin image and an owner-provided symptom description. The image is analyzed through a fine-tuned deep learning model (ResNet50), and the symptom text is encoded semantically and classified using machine learning (SBERT + XGBoost). The outputs of both models are combined through a weighted late fusion strategy to produce a more accurate, holistic health assessment than either modality could achieve alone. The system is designed to work across small, medium, and large dog breeds, and presents results in plain language — including disease prediction, confidence score, risk level, and recommended next steps — so that everyday pet owners can make informed decisions without needing veterinary expertise.

---

## Team

| Name | SRN |
|------|-----|
| Aishwarya R | PES2UG23AM008 |
| Deepika N | PES2UG23AM028 |
| Rahul Rathod | PES2UG23CS462 |
| Renuka Gangadhar Hosamani | PES2UG23CS474 |

---

> For full project context, architecture, results, and repository structure see [CONTEXT.md](CONTEXT.md).
