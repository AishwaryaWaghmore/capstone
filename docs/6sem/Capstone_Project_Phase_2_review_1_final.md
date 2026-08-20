<!-- Slide number: 1 -->
UE23CS320B–  Project Phase – 2
Capstone Project –Phase 2 –review 1
Project Title	: AI-Based Dog Health Monitoring System Using Dual-Input        (Images + Symptoms)
Project ID  	:193
Project Guide : Prof. Umme Haani
Project Team	: Aishwarya Ravi	– PES2UG23AM008
Deepika N – PES2UG23AM028
Rahul Rathod – PES2UG23CS462
Renuka Gangadhar Hosamani  - PES2UG23CS474

<!-- Slide number: 2 -->
Agenda

Problem Statement
Abstract and Scope
Suggestions from Phase-1
Requirements Specification
Data set and requirements
Design Approach
Design Constraints, Assumptions & Dependencies
Proposed System / Approach
Architecture
Design Description
Project Progress
References

### Notes:

<!-- Slide number: 3 -->
Problem Statement

Pet owners often struggle to identify whether their pets are suffering from common or serious illnesses. Visiting a veterinarian for every minor concern can be costly and inconvenient. Many diseases show early signs in the form of symptoms (loss of appetite, vomiting, fatigue) and visible indicators (abnormal stool, urine color, skin conditions, or vomit appearance). There is currently no widely available system that integrates both symptom descriptions and visual evidence to support early health assessments. We aim to develop a hybrid, multi-modal AI system that analyzes both symptom descriptions and pet images to predict possible diseases, highlight key evidence, and guide owners on whether they should seek veterinary care.

### Notes:

<!-- Slide number: 4 -->
Abstract

This project addresses the problem of inaccurate or delayed disease detection in dogs caused by single-input health monitoring systems. It introduces an AI-Based Dog Health Monitoring System that uses dual inputs — images and symptoms for better accuracy. The system applies deep learning for image-based disease detection and machine learning for symptom analysis. By integrating both data types, it ensures early and more reliable diagnosis among breeds. The project aims to assist veterinarians and pet owners in improving preventive healthcare and timely treatment.

### Notes:

<!-- Slide number: 5 -->
Scope

The scope includes data collection, preprocessing, model training, and multimodal fusion of images and symptoms. It covers health monitoring and disease prediction for different dog breed sizes with scalable AI models. The system provides a user-friendly interface for owners to upload images and report symptoms for instant analysis. Future extensions can integrate IoT sensors for real-time health tracking. Overall, the project establishes a foundation for AI-driven, breed-aware, and multimodal veterinary health monitoring systems.

### Notes:

<!-- Slide number: 6 -->
Suggestions from Phase-1

During Phase–1 review, the panel suggested integrating IOT sensors for continuous health monitoring. After evaluation, it was found that IOT sensors increase cost and hardware dependency, reducing accessibility for users. Hence, the current system focuses on a user-friendly, software-based approach using images and symptom descriptions. Optional inputs such as age and temperature are included to add contextual health information. The system remains scalable, allowing IOT sensor integration as a future enhancement.

### Notes:

<!-- Slide number: 7 -->
Requirements Specification

Functional Requirements
Upload pet image
Enter symptoms
Select breed category
Generate disease prediction
Classify severity
Display home care suggestion
Show nearby veterinary clinics
Allow appointment booking request

### Notes:

<!-- Slide number: 8 -->
Requirements Specification

Non-Functional Requirements
Response time < 5 seconds
Prediction accuracy > 80% (prototype goal)
Secure user data handling
Scalable architecture
User-friendly interface

### Notes:

<!-- Slide number: 9 -->
Requirements Specification

Technologies Used
Python
TensorFlow / PyTorch (CNN)
Scikit-Learn (Random Forest / XGBoost)
Flask (Backend)
MySQL (Database)
HTML/CSS/Bootstrap (Frontend)

### Notes:

<!-- Slide number: 10 -->
Data set and requirements

Image Dataset
Type:
Dog skin diseases
Eye infections
Wounds
Healthy samples
Features Extracted:
Redness detection
Fur loss patches
Lesion shape
Texture variation
Model Used : CNN-based image classifier
B. Symptom Dataset
Structured dataset format:
| Vomiting | Fever | Itching | Duration | Disease Label |
Features Considered:
Vomiting
Diarrhea
Lethargy
Loss of appetite
Fever
Itching

Model Used: Random Forest / XGBoost

### Notes:

<!-- Slide number: 11 -->
Data set and requirements

C. Severity Features
Derived using:
Symptom frequency
Duration
Image confidence score
Severity Output:
Mild
Moderate
Severe

### Notes:

<!-- Slide number: 12 -->
Design Approach

We followed a Modular Multimodal Architecture with Late Fusion Approach.
The system is divided into two independent modules:
Image Processing Module (CNN)
Symptom Analysis Module (ML Model)
The outputs of both modules are combined using a fusion layer to generate the final health prediction.

### Notes:

<!-- Slide number: 13 -->
Design Approach

Why this approach?
Allows independent development and testing of each module.
Improves accuracy by combining visual and symptom-based features.
Suitable for prototype development within limited time.
Easy to scale and extend in future

### Notes:

<!-- Slide number: 14 -->
Design Approach

Benefits of this Approach
Better accuracy compared to single-input systems.
Clear separation of components (modular design).
Easier debugging and model improvement.
Scalable for adding more breeds or diseases.
Flexible — one module can work even if the other input is missing.

### Notes:

<!-- Slide number: 15 -->
Design Approach

Drawbacks (Limitations)
Requires separate dataset preparation for images and symptoms.
Fusion logic increases system complexity.
Performance depends heavily on dataset quality.
May require more training time.

### Notes:

<!-- Slide number: 16 -->
Design Approach

Alternate Design Approaches
Single Input System
Only image-based or only symptom-based.
Simpler but less accurate.
Early Fusion Approach
Combine image and symptom features before classification.
More complex and requires aligned multimodal datasets.
Rule-Based Expert System
Predefined symptom rules.
Less flexible and not scalable.

### Notes:

<!-- Slide number: 17 -->
Design Constraints, Assumptions & Dependencies

Design Constraints
Limited availability of multimodal datasets containing both image and symptom data together.
Variations across different dog breeds (size, coat type, disease patterns) increase model complexity.
Limited computational resources and absence of high-end GPUs for large-scale training.
Prototype-level implementation without full clinical validation.

### Notes:

<!-- Slide number: 18 -->
Design Constraints, Assumptions & Dependencies

Assumptions
Uploaded dog images are clear and properly visible.
Users provide basic and correct symptom information.
Selected breeds effectively represent small, medium, and large categories.
Public datasets are sufficiently labeled and reliable.
System output is intended only for preliminary health assessment.

### Notes:

<!-- Slide number: 19 -->
Design Constraints, Assumptions & Dependencies

Dependencies
Availability and quality of public datasets from Kaggle, Roboflow, and Stanford Dogs.
Performance of CNN for image-based analysis.
Proper preprocessing and encoding of symptom data.
Successful integration of image and symptom models.
Regular guidance and feedback from project mentor.

### Notes:

<!-- Slide number: 20 -->
Design Details

Design Details
The system is developed using a modular multimodal design, processing dog images and symptoms separately and combining them for final prediction.
Publicly available datasets are used, and the system runs on a local development environment.
The design is innovative as it integrates visual and symptom-based analysis instead of relying on a single input.
A modular structure ensures maintainability, reusability, and easy future extension.
The system is portable and compatible with standard platforms and can be extended to web or mobile applications.

### Notes:

<!-- Slide number: 21 -->
Proposed System / Approach

System Overview
Multimodal AI-based system for dog skin disease classification
Uses dual inputs:
Dog skin image
Symptom text description
Optional contextual inputs:
Age
Temperature
Combines deep learning and machine learning using a late fusion strategy
Designed to improve prediction accuracy and reliability

### Notes:

<!-- Slide number: 22 -->
Proposed System / Approach
Data Acquisition & Inputs
Collects dog skin images across six disease categories
Accepts symptom descriptions from pet owners
Optional metadata: age and body temperature
Uses publicly available datasets and user-provided inputs
Acts as the entry layer of the system

### Notes:

<!-- Slide number: 23 -->
Proposed System / Approach

Image & Text Processing Modules
    Image Processing Module
Images resized to 224 × 224
Normalization and data augmentation applied
Pretrained ResNet-18 used for feature extraction
Outputs disease probability scores
    Text Processing Module
Symptom text cleaned and tokenized
TF-IDF converts text to numerical features
Random Forest classifier predicts disease probabilities

### Notes:

<!-- Slide number: 24 -->
Proposed System / Approach

Late Fusion Strategy
Uses decision-level (late) fusion
Image-based and text-based predictions generated independently
Optional age and temperature refine predictions
Weighted fusion combines outputs from both models
Improves robustness and reduces misclassification

### Notes:

<!-- Slide number: 25 -->
Proposed System / Approach

Output & Key Features

Final output includes:
Disease category
Confidence score
Risk level
Suggested action and veterinary advice
Key features:
Multimodal input (Image + Text)
Modular and scalable design
Optional contextual refinement
Focus on early-stage skin disease detection

### Notes:

<!-- Slide number: 26 -->
Architecture

![](Picture3.jpg)

### Notes:

<!-- Slide number: 27 -->
Capstone (Phase-I ,Phase-II and phase -III) Project Timeline

![](Picture7.jpg)

<!-- Slide number: 28 -->
Conclusion

CONCLUSION
Designed a multimodal AI-based pet health assistance system.
Integrated severity prediction.
Added actionable home-care guidance.
Implemented vet recommendation module.
Built scalable modular architecture.
This system bridges the gap between AI prediction and practical veterinary assistance.

<!-- Slide number: 29 -->
References

📚 References (IEEE Format)
   1) L. Chen, M. Zhao, and Y. Li, “A Multimodal Fusion Approach for Veterinary Disease Detection,” Computers in Biology and Medicine, vol. 169, pp. 107534, 2024.
   2) A. Kumar, R. Sharma, and S. Gupta, “Deep Learning-Based Pet Disease Diagnosis Using Skin and Fur Images,” IEEE Access, vol. 11, pp. 45782–45791, 2023.

### Notes:

<!-- Slide number: 30 -->
Thank You