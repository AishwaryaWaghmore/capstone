UE23CS320A – Capstone Project Approval
Project Title : AI-Based Dog Health Monitoring System Using
Dual-Input (Images + Symptoms) for Small, Medium, and
Large Breeds
Project ID :193
Project Guide: Prof.Umme haani
Project Team : Aishwarya ravi – PES2UG23AM008
Deepika N – PES2UG23AM028
Rahul rathod – PES2UG23CS462
Renuka Gangadhar Hosamani - PES2UG23CS474
Outline

Problem Statement

| Problem statement |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- |

| Pet  | owners  | often  | struggle  |     | to  identify  |     | whether  |
| ---- | ------- | ------ | --------- | --- | ------------- | --- | -------- |
their pets are suffering from common or serious
| illnesses.  |     | Visiting  | a   | veterinarian  |     | for  | every  |
| ----------- | --- | --------- | --- | ------------- | --- | ---- | ------ |
minor concern can be costly and inconvenient.
Many diseases show early signs in the form of
symptoms (loss of appetite, vomiting, fatigue)
| and     | visible  | indicators   |     | (abnormal  |        | stool,        | urine  |
| ------- | -------- | ------------ | --- | ---------- | ------ | ------------- | ------ |
| color,  | skin     | conditions,  |     | or         | vomit  | appearance).  |        |
There is currently no widely available system

that integrates both symptom descriptions and
| visual        | evidence  |     | to      | support  |          | early     |     | health   |
| ------------- | --------- | --- | ------- | -------- | -------- | --------- | --- | -------- |
| assessments.  |           | We  | aim     | to       | develop  |           | a   | hybrid,  |
| multi-modal   |           | AI  | system  | that     |          | analyzes  |     | both     |
symptom descriptions and pet images to predict
possible diseases, highlight key evidence, and
| guide  | owners  | on  | whether  |     | they  | should  |     | seek  |
| ------ | ------- | --- | -------- | --- | ----- | ------- | --- | ----- |
veterinary care.

Scope and Feasibility study

This project aims to develop an AI-based dog
| health  | monitoring  |     | system  | using  | dual-inputs:  |     |     |
| ------- | ----------- | --- | ------- | ------ | ------------- | --- | --- |
images and symptoms. The system will support
| small,  | medium,  |     | and  | large  | dog  | breeds,  |     |
| ------- | -------- | --- | ---- | ------ | ---- | -------- | --- |
identifying visible and behavioral health issues.
| Image  | analysis  | will  | detect  | physical  |     | signs  | like  |
| ------ | --------- | ----- | ------- | --------- | --- | ------ | ----- |
skin problems or injuries, while symptom input
| will   | capture  | behavioral  |       | changes.  |     | A  fusion    |     |
| ------ | -------- | ----------- | ----- | --------- | --- | ------------ | --- |
| model  | will     | process     | both  | inputs    |     | to  suggest  |     |

possible health conditions. The system will be
| accessible   |            | via                                | a  mobile     | or  | web     | interface.  |     |
| ------------ | ---------- | ---------------------------------- | ------------- | --- | ------- | ----------- | --- |
| Technically  |            | feasible using existing AI models  |               |     |         |             |     |
| and          | datasets.  |                                    | Economically  |     | viable  | for         | a   |
research or MVP phase. Operationally practical
| with    | clear     | user  | guidelines  | and  | disclaimers.  |     |      |
| ------- | --------- | ----- | ----------- | ---- | ------------- | --- | ---- |
| Offers  | valuable  |       | assistance  | to   | pet  owners   |     | and  |
can reduce unnecessary vet visits.

Feasibility study
Technical Feasibility
AI models (CNN for images, NLP for symptoms) are
•
already available and can be adapted.
Preprocessing pipelines and fusion models are well-
•
researched.
Datasets (dog images + symptom reports) can be
•
sourced or expanded.
2. Economic Feasibility

Development cost is manageable at research / prototype
•
level.
Open-source AI tools reduce cost.
•
Commercial scalability possible through premium
•
features.
3. Operational Feasibility
Simple mobile/web app ensures easy
•
adoption by pet owners.
Clear guidelines and disclaimers prevent misuse.
•
Reduces unnecessary vet visits, saving time and
•
expenses.

Applications/Use cases
•Early Disease Detection – Identifies common illnesses (e.g.,
skin infections, eye issues) in dogs through image and
symptom analysis.
•Breed-Specific Health Monitoring – Offers tailored insights
based on breed size (small, medium, large) and common health
risks.
•Remote Health Checks – Assists pet owners in rural or remote
areas where access to veterinary services is limited.
•Pet Care Guidance – Suggests home care tips or alerts when
veterinary attention is necessary.

•Veterinary Pre-Screening Tool – Helps clinics triage
nonemergency cases and prioritize urgent ones.
•Educational Tool for Pet Owners – Informs owners about
symptoms and breed-specific health concerns.
•Telehealth Integration – Can be extended to support remote
consultations with veterinarians.
•Pet Wellness Apps – Integrates into pet care apps to track
ongoing health and alerts.
•AI Research in Veterinary Medicine – Contributes to the
development of intelligent systems for animal healthcare.

Objectives:
-Develop an AI model capable of analyzing pet symptoms and
images (vomit, stool, urine, skin, etc.)
Fuse multi-modal inputs (symptoms + images) for improved
-
prediction accuracy - Provide explainable AI outputs
(highlight image regions or symptom factors influencing
predictions)
Design the system to be user-friendly for non-expert pet
-
owners - Offer preventive health advice and alerts for serious
issues.

Expected Deliverable
Deliverables:
A dataset combining symptom descriptions and annotated pet
-
images
A trained hybrid AI model (CNN for images + ML classifier
-
for symptoms)
A prototype web/mobile application for pet owners
-
Explainability module (Grad-CAM for images, SHAP for
-
symptoms) - Final report and presentation
-

Risks and Challenges :
-Limited availability of publicly accessible datasets combining
symptoms and images
Variability in image quality due to different lighting and
-
camera devices
Need for careful design to ensure predictions are advisory,
-
not diagnostic
Balancing explainability with accuracy
-
Integration of multi-modal data sources
-

Capstone (Phase-I Phase-II, Phase-III) Project Timeline
Capstone-I deliverables
•
Defined and refined problem statement
Literature survey on CNNs, symptom analysis, multimodal
AI
Initial dataset collection (dog images, symptoms, breed
data)
Dataset annotation and preprocessing plan

Interim report and presentation
Capstone-II deliverables
•
System architecture and workflow diagram
Preprocessing pipelines for image and symptom data
Baseline AI models (CNN for images, NLP/rule-based for
symptoms)
Prototype interface (image/symptom input + result display)
Progress report and demo presentation

Capstone-III deliverables
•
Model optimization and evaluation results
Functional recommendation/alert system
Draft research paper (methodology + results)
Usability testing report with user feedback
Integrated dual-input AI model with breed-specific tuning

Gantt chart

Reference :
-Proceedings of the Third International Conference on Augmented Intelligence and Sustainable Systems
(ICAISS-2025) IEEE Xplore Part Number: CFP25CB2-ART; ISBN: 979-8-3315-0724-4
-Proceedings of the International Conference on Intelligent Computing and Control Systems (ICICCS-
2025) IEEE Xplore Part Number: CFP25K74-ART; ISBN: 979-8-3315-1208-8
Datasets:
Pet health link: https://www.kaggle.com/datasets/sathwiknomula/animal-veterinary-health-dataset
Symptoms link: https://www.kaggle.com/datasets/yyzz1010/pet-health-symptoms-dataset
Skin diseases link: https://universe.roboflow.com/pethealth/dog-skin-disease-dataset-s8tt2
Images link : https://www.kaggle.com/datasets/amartya0roy/dogs-diseases

Thank You