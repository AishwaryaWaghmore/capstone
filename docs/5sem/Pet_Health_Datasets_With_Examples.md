Pet Health Datasets for Capstone Project.

This document provides a curated list of open-source veterinary and pet-health datasets that can be used for building a capstone project on AI-powered disease prediction in pets. The datasets include structured health records, symptom data, and veterinary images (stool, vomit, urine, skin, etc.). Each dataset includes a description, link, an explanation of how it will be utilized in the project, along with a sample example (symptom+disease or image+disease).

# Animal Veterinary Health Dataset (Kaggle)

Structured dataset with records of animal health indicators, including pregnancy status and disease diagnoses.

Link: <https://www.kaggle.com/datasets/sathwiknomula/animal-veterinary-health-dataset>

Tables - [Animal\_Vet.xlsx](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fstorage.googleapis.com%2Fkagglesdsdata%2Fdatasets%2F8075077%2F12773242%2FAnimal_Vet.xlsx%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com%252F20250829%252Fauto%252Fstorage%252Fgoog4_request%26X-Goog-Date%3D20250829T050226Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3D6d74d7b8cb2f6d1947126a5f7eae9b2d18cfda715b41da839b7cc06b327589b83b2fda60cd8da681f38e3b85b2a03592e8d840237422ad13801e0803e328688eb549020ab9057990689e38cfcd34cc7f1f1b748a27f5dafd05db24b36df978239c7128e821d4d863a906b8143de32af9580038fa59c3384a055f9c940b5cd60e4f115dc72c25980753ab658fe911bbc181c1d6f61d3f8f889e3f58b2a0c64b0094e02b55dff1a4f8de8194641f4c90d9fc310da2b3d618e18fb51ab3949a2b1afc8d53162657a1f3cc247fba8adbbb23c10bc4bea3e045601347059ad25bd9940ce4fd59c4e6c5f5f7fa5ec447945baa883cedaae95f4ef74f8f8901580d972e&wdOrigin=BROWSELINK)

How We Will Use It: We will use this dataset to train models that map structured veterinary health records and symptoms to disease predictions.

Example: Example: Symptom - 'Abortion in pregnant cow' → Disease - 'Brucellosis'.

![](data:image/png;base64...)

# Pet Health Symptoms Dataset (Kaggle)

Synthetic text dataset with pet symptoms labeled by condition type.

Link: <https://www.kaggle.com/datasets/yyzz1010/pet-health-symptoms-dataset>

Tables -

How We Will Use It: This dataset will help us build an NLP model for analyzing owner-reported symptoms like 'not eating' or 'sleeping a lot'.

Example: Example: Symptoms - 'Vomiting, not eating, lethargic' → Disease - 'Gastroenteritis'.

![](data:image/png;base64...)

# Dog Poop Dataset (Kaggle)

Image dataset focusing on canine defecation behaviors and stool classification.

Link: https://www.kaggle.com/datasets/wengjiyao/dog-poop-dataset

How We Will Use It: We will use this dataset to train a CNN to classify stool images and detect abnormalities.

Example: Example: Image - 'Loose watery stool' → Possible Disease - 'Parvovirus infection'.

[Screenshot not available]

# Dog Skin Diseases Dataset (Roboflow)

Labeled images for classifying dog skin conditions like bacterial or fungal infections.

Link: https://universe.roboflow.com/pethealth/dog-skin-disease-dataset-s8tt2

How We Will Use It: This dataset will allow us to train image classification models that can detect visible dermatological diseases.

Example: Example: Image - 'Red inflamed patches on skin' → Disease - 'Fungal infection'.

[Screenshot not available]

# Dog's Diseases Image Dataset (Kaggle)

Broad dataset of images for different dog diseases.

Link: https://www.kaggle.com/datasets/amartya0roy/dogs-diseases

How We Will Use It: We will use this dataset to generalize our CNN model to recognize multiple dog diseases from images.

Example: Example: Image - 'Dog with eye discharge and dull coat' → Disease - 'Canine Distemper'.

[Screenshot not available]

# Classification of Pet Dog Skin Diseases (Mendeley Data)

Skin images of 95 dogs with bacterial, fungal, allergic conditions, and healthy controls.

Link: https://data.mendeley.com/datasets/5dbht54kw7/1

How We Will Use It: We will utilize this dataset for validating and benchmarking our CNN models.

Example: Example: Image - 'Crusty lesions around mouth' → Disease - 'Allergic Dermatitis'.

[Screenshot not available]

**Next Steps for Your Project**

* **Symptom-based model**: Use the **Animal Veterinary Health** and **Pet Health Symptoms** datasets for training an ML classifier.
* **Image-based model**: Use **Dog Skin Diseases (Roboflow)** and **Mendeley Dog Skin Diseases** datasets to develop your CNN for visual diagnosis.
* **Stool/vomit/urine images**: Start with **Dog Poop** dataset; consider collecting supplementary images if needed.
* **Data integration**: If VetDataHub hosts relevant datasets for vomiting or urine abnormalities, you can enrich your data further.

# OUR IDEA :

1. **Multi-Modal Diagnosis (Symptoms + Images Together)**
   * Most existing works use **either symptoms (text/fuzzy systems)** OR **images (CNN/deep learning)**.
   * You can **combine both**:
     + Example: If the owner reports *vomiting + lethargy*, and uploads an image of *stool/urine/skin*, your system fuses both inputs to improve accuracy.
   * This makes your approach **more reliable** than symptom-only or image-only systems.
2. **Explainable AI for Pet Owners**
   * Existing systems mostly give a disease label.
   * You can provide **reasoning/explanations**:
     + “Based on vomiting + yellowish stool + image features, there’s a 75% chance of liver infection.”
   * Adding **explainability** (via rule-based reasoning, SHAP, or decision trees alongside deep learning) will make your system **trustworthy**.
3. **Rarely Addressed Input Sources (Vomit/Urine/Stool Images)**
   * Most papers focus on **skin lesions** in pets.
   * Very few tackle internal signs like **vomit color/texture, urine shade, stool consistency**.
   * Including these image datasets (even if partially synthetic/augmented) makes your work unique.
4. **Owner-Friendly, Non-Expert Inputs**
   * Many papers assume **veterinary-quality data (scans, medical records)**.
   * You can build for **casual owners**, who only have:
     + A smartphone camera
     + Ability to describe symptoms in plain language
   * This makes your project **practical in real-world pet-owner scenarios**.
5. **Early Warning + Recommendation System**
   * Instead of just saying *“Your dog has X disease”*, your system could:
     + Predict **likelihood of multiple possible diseases**
     + Suggest **next steps** (visit vet urgently, or home care possible, or monitor symptoms).
   * This bridges the gap between **prediction and action**.
6. **Cross-Species Extension (Dogs + Cats, maybe more later)**
   * Most studies are limited to **dogs**.
   * If you build your dataset/system in a way that can be extended to **cats (and maybe other small pets)**, it increases novelty.

So in short, your differentiator could be:
A hybrid, multi-modal AI system for pets that uses both symptom descriptions and images (including less-studied data types like vomit/urine/stool), provides explainable results, and is designed specifically for non-expert pet owners.