<!-- Slide number: 1 -->

UE23CS320B – Capstone Project Phase – 2

Project Progress Review #2
Project Title: AI-Based Dog Health Monitoring System Using Dual-Input (Images +
                      Symptoms)
Project ID:        193
Project Guide:  Prof. Umme Haani
Project Team:   Aishwarya Ravi – PES2UG23AM008
                         Deepika N -      PES2UG23AM028
                         Rahul Rathod – PES2UG23CS462
                         Renuka Gangadhar Hosamani - PES2UG23CS474

<!-- Slide number: 2 -->

Objectives

To detect and classify common dog skin diseases at an early stage
To integrate image-based (CNN) and symptom-based (ML) predictions
To provide confidence score and risk level assessment
To generate actionable recommendations for pet owners
To develop a multimodal dog health monitoring system using image and symptom inputs
To design a user-friendly application interface for easy interaction

<!-- Slide number: 3 -->

Objectives

Collect and preprocess image and symptom datasets
Develop image classification model (CNN)
Develop symptom analysis model (sbert+xgboost)
Combine outputs using decision-level (late) fusion
Display results through Flask-based web interface
Perform independent predictions from both models
Generate final prediction, confidence score, and risk level

<!-- Slide number: 4 -->

 Methodology Overview

Data Collection: Gather dog disease images and symptom data.
Data Preprocessing:Images → Resize, augment, normalize
                             Text → Clean, tokenize, SBERT embeddings.
Model Development:CNN for image classification
                               SBERT + XGBoost for symptom analysis.
Fusion Technique: Combine both model outputs (decision-level fusion)
Prediction Output:Disease prediction
                            Confidence score
                            Risk level (Low / Medium / High)
Deployment: Flask-based web interface for user interaction

<!-- Slide number: 5 -->

    Data Pre-processing
    Image Data
Resizing images (224×224 / 300×300)
Data augmentation (flip, rotation, zoom)
Normalization of pixel values

   Text Data
Cleaning (removing noise, special characters)
Tokenization
Feature extraction using SBERT embeddings

Dataset split into Train, Validation, Test sets
Improves generalization and reduces overfitting
Expected Deliverables

<!-- Slide number: 6 -->

Expected Deliverables

  Data Visualization
    Image Data
 Display sample images from each disease class
   Helps understand visual differences (lesions, color, texture)

   Text Data
Analyze sample symptom descriptions
Observe common keywords (itching, redness, hair loss)

Ensures data quality and correct labeling

<!-- Slide number: 7 -->

Expected Deliverables

      Data Interpretation
Dataset contains 6 dog disease classes
Image model learns visual patterns (texture, lesions, color)
Text model learns semantic meaning of symptoms
Evaluation using Accuracy, Precision, Recall, F1-score
Confusion matrix used to analyze misclassifications

Text → Clean → (Optional preprocessing) → SBERT Embedding → Train Classifier → Prediction
Image → Resize → Augment → Normalize → Encode Labels → Split → Batch → Train Model

<!-- Slide number: 8 -->

Expected Deliverables

sbert+xgboost output

<!-- Slide number: 9 -->

Expected Deliverables

Resnet50 output

<!-- Slide number: 10 -->

Expected Deliverables

     Storage
Dataset stored in structured folders (Train / Validation / Test)
Image and text datasets maintained separately
Models saved in .keras / .h5 format
Enables reuse without retraining

<!-- Slide number: 11 -->

Expected Deliverables

![](Picture8.jpg)

<!-- Slide number: 12 -->

Team members contribution

![](Picture9.jpg)

<!-- Slide number: 13 -->
Expected Deliverables

4. SDK / API / Model / Tools & Technologies Used
All tools are 100% Open Source — no licensing cost required

Programming Language
Deep Learning
Machine Learning
🐍  Python 3.10
Core language for all
modules and scripting
🧠  TensorFlow / Keras
     PyTorch
CNN model training
& ResNet50 fine-tuning
📊  Scikit-learn
     XGBoost
TF-IDF, Random Forest
for symptom prediction

NLP / Embeddings
Web & Backend
Dev Tools & Datasets
💬  SBERT
Semantic symptom text
understanding
🌐  Flask + MySQL
     HTML/CSS/Bootstrap
Backend API, database
& user interface
🛠  VS Code / Colab
     Kaggle / Roboflow
IDE, training platform
& image datasets

<!-- Slide number: 14 -->
Expected Deliverables

4a. AI & Machine Learning Libraries

Tool / Library
Type
License
How We Use It

Python 3.10
Language
PSF — Free
Core language for all code: model training, Flask app, scripts

TensorFlow 2.x/Keras
Deep Learning
Apache 2.0
CNN model building, training pipeline, pretrained weight loading

PyTorch + torchvision
Deep Learning
BSD License
ResNet50 pretrained model loading and fine-tuning on dog data

Scikit-learn
ML Library
BSD License
TF-IDF vectorizer, Random Forest classifier, accuracy metrics

XGBoost
ML Boosting
Apache 2.0
Gradient-boosted classifier for symptom-based disease prediction

SBERT
NLP / Embeds
Apache 2.0
Converts symptom text to semantic vectors for smarter matching

<!-- Slide number: 15 -->
Expected Deliverables

4b. Web, Backend, Datasets & Development Tools

Tool / Library
Type
License
How We Use It

Flask 3.x
Web Framework
BSD — Free
Backend API endpoints, routing, session management for the app

MySQL 8.0
Database
GPL — Free
Stores user data, prediction history, vet appointment records

HTML5 / CSS3 / Bootstrap
Frontend
MIT / W3C
Image upload form, symptom input, results display, responsive UI

Kaggle Datasets
Dataset Source
Open / Free
Labeled dog skin disease image dataset — 6 disease classes

Roboflow
Dataset Tool
Free Tier
Image annotation, augmentation export, dataset versioning

VS Code / Google Colab
Dev / Training
MIT / Free
VS Code for development; Colab for free GPU model training

<!-- Slide number: 16 -->
Expected Deliverables

4c. Summary — Technology Stack at a Glance

10+
100%
6
2
Libraries Used
Open Source
Disease Classes
AI Models (CNN + ML)

Why Open Source?
✔  No licensing cost   ✔  Industry-standard for AI/ML research   ✔  Large community support   ✔  Reproducible & peer-reviewed

Python 3.10
TensorFlow
PyTorch
Scikit-learn
XGBoost

SBERT
Flask
MySQL
Bootstrap
Kaggle

<!-- Slide number: 17 -->

Expected Deliverables

Implementation (Phase-2 Progress)
Developed initial multimodal system prototype
Implemented symptom-based prediction using Machine Learning (sbert+ xgboost )
Designed basic CNN architecture for image processing
Integrated both models using fusion logic
Built a web-based user interface using Flask
Generated prediction with confidence score
Added risk level classification and recommendation system

<!-- Slide number: 18 -->

Expected Deliverables

System Output

User enters symptoms through web interface
System processes input using ML model
Image and symptom predictions are combined
Final output includes:
                 Predicted disease
                 Confidence score
                 Risk level (Low / Medium / High)
                 Suggested action

<!-- Slide number: 19 -->

Expected Deliverables

<!-- Slide number: 20 -->

Expected Deliverables

Key Features

Multimodal  input (image + symptom )
Machine learning-based prediction
Decision-level fusion approach
Confidence score generation
Risk classification system
User-friendly web interface
Actionable veterinary recommendations

<!-- Slide number: 21 -->

Expected Deliverables

Technologies Used

Python
TensorFlow / Keras (for CNN)
Scikit-learn (Random Forest, sbert+ xgboost )
Flask (Web framework)
HTML, CSS (UI design)

<!-- Slide number: 22 -->

Expected Deliverables

Current progress

Initial model setup completed
Basic implementation (~10–15%) achieved
UI prototype developed
Integration logic implemented
Dataset collection and preprocessing completed

<!-- Slide number: 23 -->

Expected Deliverables

Future enhancements

Train CNN model with real image dataset
Improve model accuracy with larger dataset
Integrate real image-based prediction
Develop mobile application
Add real-time monitoring features