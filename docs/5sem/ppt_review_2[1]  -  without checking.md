<!-- Slide number: 1 -->
UE23CS320A–  Project Phase – 1
 Review -2
Project Title   :AI-Based Dog Health Monitoring System Using Dual-Input
                         (Images + Symptoms) for Small, Medium, and Large Breeds
Project ID       :193
Project Guide :Prof. Umme Haani
Project Team  :Aishwarya Ravi – PES2UG23AM008
                       Deepika N – PES2UG23AM028
                       Rahul Rathod – PES2UG23CS462
                       Renuka Gangadhar Hosamani – PES2UG23CS474

<!-- Slide number: 2 -->
Agenda

Introduction and Motivation
Problem Statement
Abstract and Scope
Suggestions from Review – 1
 Research / Technology gap and Challenges
Objectives
Literature Survey / Existing System
References

### Notes:

<!-- Slide number: 3 -->
Introduction and Motivation

The project aims to develop an AI-based Dog Health Monitoring System that analyzes both images and symptoms to accurately detect diseases in dogs. It uses a dual-input model to provide comprehensive health assessment for small, medium, and large breeds .Current systems rely only on images or text, leading to incomplete diagnoses. By combining visual and clinical data, this approach ensures early detection and better decision support for veterinarians and pet owners. The motivation is to improve pet healthcare using multimodal AI technology for timely and reliable health monitoring

### Notes:

<!-- Slide number: 4 -->
Problem Statement

Pet owners often struggle to identify whether their pets are suffering from common or serious illnesses. Visiting a veterinarian for every minor concern can be costly and inconvenient. Many diseases show early signs in the form of symptoms (loss of appetite, vomiting, fatigue) and visible indicators (abnormal stool, urine color, skin conditions, or vomit appearance). There is currently no widely available system that integrates both symptom descriptions and visual evidence to support early health assessments. We aim to develop a hybrid, multi-modal AI system that analyzes both symptom descriptions and pet images to predict possible diseases, highlight key evidence, and guide owners on whether they should seek veterinary care.

### Notes:

<!-- Slide number: 5 -->
Abstract and Scope

Abstract

This project addresses the problem of inaccurate or delayed disease detection in dogs caused by single-input health monitoring systems. It introduces an AI-Based Dog Health Monitoring System that uses dual inputs — images and symptoms for better accuracy. The system applies deep learning for image-based disease detection and machine learning for symptom analysis. By integrating both data types, it ensures early and more reliable diagnosis across small, medium, and large breeds. The project aims to assist veterinarians and pet owners in improving preventive healthcare and timely treatment.

### Notes:

<!-- Slide number: 6 -->
Scope

The scope includes data collection, preprocessing, model training, and multimodal fusion of images and symptoms. It covers health monitoring and disease prediction for different dog breed sizes with scalable AI models. The system provides a user-friendly interface for owners to upload images and report symptoms for instant analysis. Future extensions can integrate IoT sensors and mobile applications for real-time health tracking. Overall, the project establishes a foundation for AI-driven, breed-aware, and multimodal veterinary health monitoring systems.

<!-- Slide number: 7 -->
Suggestions from Review - 1

During Review–1, the panel members suggested improving the Gantt chart for better time allocation and clarity of project phases. They also recommended enhancing the presentation quality and providing more detailed explanations of each module.
In response, the Gantt chart has been revised to clearly show timelines, and phase-wise milestones.
The presentation has been refined with improved structured content, and clear communication of objectives.
Additional clarity has been provided in the project documentation to ensure a better understanding of the proposed system.

### Notes:

<!-- Slide number: 8 -->
Challenges and Research Gap

| Existing Gaps | How our Project Fills Them |
| --- | --- |
| Models focus on only one data type (image or symptom). | Combines both inputs for better accuracy. |
| Lack of systems generalized across dog breeds. | Model trained to handle multiple breeds (small, medium, large). |
| No early disease alert system for owners. | Provides instant prediction from image + basic symptom entry. |
| Low interpretability of image-only models. | Fusion gives explainable results — you can show which symptom or image feature led to prediction. |

### Notes:

<!-- Slide number: 9 -->
Objectives

Objectives of the Project

1.To develop an AI-based system that can detect and monitor dog health conditions using both images and symptom data.

2.To implement deep learning models for image-based disease detection and machine learning algorithms for symptom analysis.

3.To combine (fuse) visual and clinical features for accurate and early disease prediction.

4.To design the system to work efficiently across different dog breed sizes  small, medium, and large.
.

### Notes:

<!-- Slide number: 10 -->
5.To create a user-friendly interface for pet owners to upload images and input symptoms easily.

6.To assist veterinarians and pet owners in early diagnosis and preventive healthcare.

7.To ensure the system is scalable and adaptable for integration with IoT or mobile health platforms in the future

<!-- Slide number: 11 -->
Literature Survey/Existing System

| Details of Paper- Title, author, conference /Journal | Methodology Used | Result | Limitations |
| --- | --- | --- | --- |
| Deep Learning-Based Pet Disease Diagnosis Using Skin and Fur Images A. Kumar, R. Sharma, S. Gupta | Used CNN (ResNet50) for classification of pet skin diseases from image datasets. | Achieved 91% accuracy in detecting visible infections. | Focused only on images, ignores symptom-based diagnostics. |
| Pet Care AI: A Smartphone-Based Health Monitoring Tool for Dogs S. Patel, R. Nair, P. Joshi | Designed rule-based expert system for dog disease diagnosis based on user-input symptoms. | Assisted remote users to self-check dog health issues. | No machine learning or image processing; limited adaptability. |
| PawSense: AI-IoT Enabled Smart Pet Care for Real-Time Health Monitoring Aravind G., Dr. Sasirekha S.P., Jeeva S., Selvaganesh D. | Combined AI, IoT, and blockchain in a Flutter-based pet care system. Real-time health data from IoT collars processed with deep learning on cloud-edge architecture. | Enabled real-time anomaly detection and predictive alerts for pet health. Improved security and latency. | Only uses IoT sensor data; lacks integration of image and symptom-based AI models. |

### Notes:

<!-- Slide number: 12 -->
Literature Survey/Existing System

| Details of Paper- Title, author, conference /Journal | Methodology Used | Result | Limitations |
| --- | --- | --- | --- |
| Development of a Dog Health Score Using an Artificial Intelligence Disease Prediction Algorithm Based on Multifaceted DataS-C Kim & S. Kim , 2024 | Activity sensors (leash/wearables) monitoring behaviors (scratching, licking, swallowing, sleep) + AI algorithm to assign a “Health Score”. | Achieved ~87.5% concordance with veterinarian diagnoses. | Only behavioral data from sensors; doesn’t include images or symptom-text fusion. |
| A Multimodal Fusion Approach for Veterinary Disease Detection L. Chen, M. Zhao, Y. Li, 2024 | Combined CNN (images) and LSTM (text symptoms) for disease prediction in livestock. | Fusion improved accuracy by 12% over single-modal models | Model focused on livestock; not adapted for pet species or user-facing systems.. |
| Pet Pulse: Detecting Dog Diseases with TFLite, Booking Vet Consults” B. Abirami & T. Momithasree , 2025 | Mobile app combining symptom tracking + pulse monitoring + image processing (skin conditions) using TFLite on smartphone. I | Demonstrated ability for owners to detect pet skin/health issues via mobile app; improved accessibility | Limited described dataset; possibly restricted to skin/disease types; full multimodal (symptoms + image + text) integration not completely detailed. |

### Notes:

<!-- Slide number: 13 -->
Dataset Exploration

Availability of dataset
The datasets required for the project are publicly available through online platforms such as Kaggle and Roboflow, which provide dog skin disease images and pet symptom information.
Source of dataset
The primary sources include the Dog Skin Disease Dataset from Kaggle, the Roboflow Dog Skin Disease Dataset, and publicly available pet symptom datasets from Hugging Face.
Size of dataset
The image datasets contain approximately 3,000–5,000 images across various disease categories, and the symptom dataset includes around 1,500–2,000 text entries describing pet health conditions.

<!-- Slide number: 14 -->
Capstone (Phase-I , Phase-II and Phase III) Project Timeline

![](Picture7.jpg)

<!-- Slide number: 15 -->
Any other information

The project is in its initial development phase and the team is focusing on literature review and data collection. Discussions are ongoing to finalize the model design and dataset selection for different dog breeds. Team members are coordinating regularly to ensure smooth progress and proper task distribution. The group is also exploring possible real-world applications and user-friendly features for the final system.

<!-- Slide number: 16 -->
Conclusion

The AI-Based Dog Health Monitoring System Using Dual-Input (Images + Symptoms) successfully demonstrates how artificial intelligence can be applied to enhance veterinary healthcare. By integrating deep learning for image analysis and machine learning for symptom-based prediction, the system provides a more accurate and reliable health assessment for dogs of small, medium, and large breeds. It addresses the limitations of existing single-input models and promotes early disease detection and preventive healthcare. The project also highlights the potential of multimodal AI in improving animal welfare and supporting veterinarians with data-driven insights. Overall, this work lays the foundation for future advancements in intelligent, breed-aware, and automated pet health monitoring systems.

<!-- Slide number: 17 -->
References

Provide references pertaining to your research according to IEEE format.
EX:G. Eason, B. Noble, and I. N. Sneddon, “On certain integrals of  Lipschitz-Hankel type involving products of Bessel functions,” Phil. Trans.  Roy. Soc. London, vol. A247, pp. 529–551, April 1955. (references)

### Notes:

<!-- Slide number: 18 -->
Thank You