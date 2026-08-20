# **DECLARATION**

We hereby declare that the Capstone Project Phase-2 entitled “AI-Based Dog Health Monitoring System Using Dual-Input (Images + Symptoms) for Small, Medium, and Large Breeds” has been carried out by us under the guidance of Prof. Umme Haani, Assistant Professor, Department of CSE, PES University, and submitted in partial fulfillment of the course requirements for the award of the degree of Bachelor of Technology in Computer Science and Engineering of PES University, Bengaluru during the academic semester January – May 2026.

The matter embodied in this report has not been submitted to any other university or institution for the award of any degree or diploma.

.

Aishwarya R PES2UG23AM008 ![](data:image/png;base64...)

Deepika N PES2UG23AM028 ![](data:image/png;base64...)

Rahul Rathod PES2UG23CS462 ![](data:image/png;base64...)

Renuka Gangadhar Hosamani PES2UG23CS474 ![](data:image/png;base64...)

# **ACKNOWLEDGEMENT**

I would like to express my gratitude to Prof. Umme Haani, Department of Computer Science and Engineering, PES University, for his/ her continuous guidance, assistance, and encouragement throughout the development of this UE23CS320B - Capstone Project Phase 2. I am grateful to all Capstone Project Coordinators, for organizing, managing, and helping with the entire process. I take this opportunity to thank Dr. Sandesh B J, Professor & Chairperson, Department of Computer Science and Engineering, PES University, for all the knowledge and support I have received from the department. I would like to thank Dr. B.K. Keshavan, Dean of Faculty, PES University for his help. I am deeply grateful to Late Dr. M. R. Doreswamy, Founder, PES University, whose vision and dedication continue to inspire generations of learners. I would also like to express my sincere gratitude to Prof. Jawahar Doreswamy, Chancellor, PES University, Dr. Suryaprasad J, Vice-Chancellor, PES University and Prof. Nagarjuna Sadineni, Pro Vice-Chancellor, PES University for providing to me various opportunities and enlightenment every step of the way. Finally, this project could not have been completed without the continual support and encouragement I have received from my family and friends.

# **ABSTRACT**

# Skin diseases in dogs are among the most frequently diagnosed veterinary conditions, yet their accurate early identification remains a significant challenge due to the visual overlap between conditions such as Demodicosis, Dermatitis, Fungal Infections, Hypersensitivity, and Ringworm. This project presents an AI-Based Dog Health Monitoring System that integrates dual input modalities — dermoscopic skin images and owner-described symptom text — to classify six canine skin conditions with higher accuracy than any single-modality approach.

# The image branch employs a fine-tuned ResNet50 convolutional neural network pre-trained on ImageNet, augmented with random flipping, rotation, and zoom, and culminating in a 6-class softmax output. The text branch encodes clinical symptom descriptions using the Sentence-BERT model (all-MiniLM-L6-v2) into 384-dimensional semantic embeddings, which are then classified by an XGBoost model with L1/L2 regularization and early stopping. Both branches produce 6-class probability vectors that are combined through a weighted late fusion strategy, with the optimal weight ratio determined by grid search across nine image-text weight combinations.

# The system is evaluated on 433 test images across six breed-diverse classes. The ResNet50 image model achieves 93.1% accuracy. The SBERT+XGBoost text model achieves approximately 85– 88% under a realistic multi-variant description evaluation protocol. The late fusion system achieves 97.2% overall accuracy with a macro F1-score of 0.96, demonstrating significant complementary gains from combining both modalities. Notably, the demodicosis class achieves a perfect F1-score of 1.00 in the fused model, and ringworm achieves 0.98.

#

# This system addresses the critical limitations of image-only veterinary AI tools and provides a reproducible, modular, and extensible framework for multimodal pet health diagnostics. Future work includes clinical deployment via a web/mobile interface and integration of real per-image clinician notes.

# **TABLE OF CONTENTS**

**. Chapter No Title**

**INTRODUCTION**

1. **PROBLEM DEFINITION**
2. **DATA** **05**
   1. **Overview**
   2. **Dataset**
   3. **Data Preprocessing**
3. **DESIGN DETAILS**
   1. **Novelty**
   2. **Innovativeness**
   3. **Interoperability**
   4. **Performance**
   5. **Security**
   6. **Reliability**
   7. **Maintainability**
   8. **Portability**
   9. **Legacy to Modernization**
   10. **Reusability**
   11. **Application Compatibility**
   12. **Resource Utilization**
4. **HIGH LEVEL SYSTEM DESIGN /SYSTEM ARCHITECTURE**

1. **DESIGN DESCRIPTION**
   1. **Master Class Diagram**
   2. **Activity Digram/ Component Diadram/ Deployment Diagra,**

**6.3 Report Layouts**

**TECHNOLOGIES USED**

1. **IMPLEMENTATION AND PSEUDOCODE**
2. **CONCLUSION OF CAPSTONE PROJECT PHASE - 2**
3. **PLAN OF WORK FOR CAPSTONE PROJECT PHASE - 3**

**REFERENCES/BIBLIOGRAPHY**

**APPENDIX A DEFINITIONS, ACRONYMS, AND ABBREVIATIONS**

# **LIST OF FIGURES**

**Figure No.**  **Title**

1. **Architecture Diagram**
2. **Master Class Diagram**
3. **Component Diagram**
4. **Activity Diagram**

1. **Deploment Diagram**
2. **Resnet50.py**

1. **Sbert+xgboost.py**
2. **Latefusion\_fixed.py**

**CHAPTER 1**

**INTRODUCTION**

Dogs are among the most widely kept companion animals globally, with an estimated population exceeding 900 million. Skin conditions constitute approximately 20–25% of all canine veterinary visits, making dermatological diseases the most common presenting complaint in small animal clinical practice. Despite this high prevalence, achieving early and accurate diagnosis remains a significant challenge. Many conditions — such as Ringworm, Demodicosis, and Hypersensitivity reactions — share overlapping visual manifestations including circular lesions, hair loss, erythema, and epidermal scaling, making unaided visual differentiation unreliable even for experienced veterinarians.

The rapid advancement of deep learning and natural language processing (NLP) over the past decade has opened new avenues for computer-aided veterinary diagnostics. Convolutional Neural Networks (CNNs) trained on dermatological image datasets have demonstrated the ability to match or exceed human expert accuracy in selected skin classification tasks. Simultaneously, transformer- based language models such as Sentence-BERT (SBERT) have revolutionized the ability to encode clinical text and symptom descriptions into semantically rich, fixed-size vector representations.

However, the majority of existing automated veterinary diagnostic systems rely on a single modality — either dermoscopic images alone or clinical text alone — ignoring the powerful complementary diagnostic information that emerges when both sources are combined. In real clinical workflows, veterinarians routinely use both visual inspection of the skin and the patient history (owner-described symptoms, duration, triggers, breed) to arrive at a

diagnosis. An AI system that mirrors this dual-input diagnostic process is therefore both clinically motivated and technically superior to unimodal alternatives.

This project — AI-Based Dog Health Monitoring System Using Dual-Input (Images + Symptoms) for Small, Medium, and Large Breeds — addresses this gap by designing, implementing, and evaluating a late fusion multimodal classification system that integrates a ResNet50 image classifier with an SBERT+XGBoost text classifier, fused at the decision layer through a weighted probability averaging strategy.

**CHAPTER 2**

# **PROBLEM DEFINITION**

Existing automated dog skin disease detection systems suffer from three primary limitations that reduce their clinical utility:

Unimodal dependency: Most published systems use either image data or text/symptom data, failing to leverage the diagnostic synergy between visual skin features and clinical symptom narratives. When visual features are ambiguous (overlapping lesion morphology), a text model can provide discriminating context, and vice versa.

Limited and imbalanced disease coverage: Published models typically cover only 2–4 skin disease categories. Multi-class classification across 6 clinically distinct conditions with overlapping visual features, varying breed sizes, and imbalanced sample counts remains an underexplored challenge.

Overfitting to evaluation artifacts: Systems evaluated using a single fixed text description per disease class exhibit artificially inflated text-model accuracy (up to 100%), dramatically misrepresenting real-world performance where users provide diverse, imprecise natural language descriptions.

This project proposes and validates a robust multimodal late fusion architecture with an honest multi-variant evaluation protocol addressing all three limitations.

**CHAPTER 3**

**DATA**

**3.1 Overview**

The performance of the proposed **AI-Based Dog Health Monitoring System** is directly related to the quality of the training data used to train the models. For the specific task of dog skin disease detection using a multimodal approach, the data requirements are more involved compared to traditional single-modality systems. In this project, the model requires data that consists of two different modalities: **image data** and **textual symptom data**.

The system leverages both visual and textual information to improve prediction accuracy. Therefore, data collection plays a crucial role in ensuring that the model can generalize well to real-world scenarios. This chapter describes the composition of the dataset, its characteristics, and the preprocessing steps applied to prepare the data for training and evaluation.

## **3.2 Dataset**

For dog health monitoring and disease detection, the dataset used in this project consists of a combination of dog skin disease images and corresponding textual symptom descriptions.

**Visual Data (Images)**

The dataset contains images of dogs affected by various skin diseases such as dermatitis, fungal infections, mange, hypersensitivity, and bacterial infections. These images are collected from publicly available sources and datasets. The dataset includes a diverse set of images with variations in lighting conditions, dog breeds, skin colors, and disease severity.

The visual data is essential for training the deep learning model (such as CNN-based architecture like ResNet50) to automatically extract features and classify diseases based on patterns observed in the skin

**Textual Data (Symptom Descriptions)**

In addition to image data, the dataset includes textual descriptions of symptoms associated with each disease. These descriptions contain information such as itching, redness, swelling, hair loss, rashes, and lesions.

Since real-world paired datasets are limited, a synthetic or semi-curated dataset is created to represent realistic symptom patterns. Each disease class is associated with multiple symptom descriptions to provide semantic understanding and variability.

Multimodal Alignment

Each image in the dataset is aligned with a corresponding symptom description based on the disease label. This pairing ensures that both modalities represent the same underlying condition, enabling effective multimodal learning and fusion.

**3.3 Data Preprocessing**

Neural networks cannot directly process raw data such as images and text; therefore, a preprocessing pipeline is developed to clean, normalize, and transform the data into a suitable format for model training. The preprocessing phase is divided into two main streams corresponding to each modality.

3.3.1 Image Preparation

The image data undergoes several preprocessing steps to ensure consistency and improve model performance:

Resizing and Normalization:
All images are resized to a fixed resolution (e.g., 224 × 224 pixels) and converted into RGB format. Pixel values are normalized to a range suitable for deep learning models.

Data Augmentation:
Techniques such as rotation, flipping, zooming, and shifting are applied to increase dataset diversity and prevent overfitting.

Tensor Conversion:
Images are converted into numerical tensors that can be processed by deep learning frameworks.

3.3.2 Text Processing

The textual symptom data is processed using Natural Language Processing (NLP) techniques:

Tokenization:
Text descriptions are broken into smaller units (tokens).

Cleaning:
Stop words, punctuation, and irrelevant symbols are removed.

Vectorization:
Text is converted into numerical representations using techniques such as TF-IDF or embeddings.

Padding and Truncation:
All sequences are adjusted to a fixed length to maintain uniform input size across batches.

3.3.3 Data Fusion Preparation

To enable multimodal learning, both image and text data are synchronized:

Each image is paired with its corresponding symptom vector

Data is split into training, validation, and testing sets

Inputs are structured to feed into the fusion model

Top of Form

**CHAPTER 4**

# **DESIGN DETAIL**

## **4.1 Novelty**

The primary novel contribution is the combination of fine-tuned ResNet50 with SBERT+XGBoost via weighted late fusion for canine dermatological disease classification. Specific novelties include:

(1) application of SBERT semantic embeddings to veterinary symptom classification for canine skin diseases; (2) a transparent late-fusion (decision-level) architecture that preserves individual modality interpretability; (3) introduction of a multi-variant text evaluation protocol with 5 clinical description variants per class to produce honest, realistic text model accuracy estimates; and (4) systematic grid search over image-text weight combinations for data-driven fusion parameter selection.

## **4.2 Innovativeness**

This work innovates by bridging the gap between unimodal clinical AI tools and real-world veterinary workflows where both visual inspection and patient history are integral. The late fusion architecture is designed to be extensible: additional modalities (e.g., blood test values, IoT wearable sensor data, behavioral activity scores) can be incorporated into the fusion layer without retraining the existing individual modality models. Using XGBoost rather than a deep neural network for the text branch provides computational efficiency, interpretability through feature importance, and builtin regularization, making the text model robust even with limited training data.

## **4.3 Interoperability** 09

The system is built entirely on open standards and widely adopted Python libraries: TensorFlow/Keras (image branch), Hugging Face sentence-transformers (SBERT), scikit-learn (preprocessing), and XGBoost (text classifier). All artifacts are saved in portable formats: best\_model.keras, xgb\_model.pkl, label\_encoder.pkl. The pipeline can be deployed on any machine with Python 3.8+ and the required pip-installable dependencies, with no proprietary software dependency. Model artifacts are platform-independent between Windows, macOS, and Linux.

## **4.4 Performance**

The performance of the proposed **AI-Based Dog Health Monitoring System** is optimized by adopting a multimodal deep learning approach, rather than relying on a single-source prediction system. By combining image-based analysis with textual symptom understanding, the system achieves higher accuracy and reliability in disease detection. The use of a Convolutional Neural Network such as ResNet50 enables efficient extraction of visual features from dog skin images in a single forward pass, allowing near real-time prediction once the model is trained.

In addition, the textual pipeline processes symptom descriptions using Natural Language Processing techniques, converting them into numerical representations that enhance semantic understanding. The fusion of image and text modalities reduces ambiguity and improves classification confidence, especially in cases where visual features alone are insufficient. The system is capable of handling diverse inputs and generalizes well across different dog breeds and environmental conditions.

During training, performance is improved through the use of GPU acceleration, batch processing, and efficient data loading mechanisms. Techniques such as asynchronous data loading and optimized memory usage help prevent computational bottlenecks and ensure smooth training. The model achieves strong performance metrics, including high accuracy, precision, recall, and F1-score, demonstrating its effectiveness in real-world scenarios.

## **4.5 Security**

In the current Phase 2 implementation, all data processing is performed locally with no external API calls or cloud data transmission. Patient images and clinical descriptions remain entirely on the local machine. For Phase 3 deployment, the system will implement: (a) end-to-end TLS encryption for data in transit; (b) role-based access control for clinical records; (c) compliance with applicable veterinary data privacy standards; (d) audit logging of all diagnostic requests; and (e) model watermarking to prevent unauthorized redistribution.

## **4.6 Reliability**

Reliability is ensured through: (a) try-except error handling in all file I/O operations during evaluation, gracefully skipping corrupted images; (b) fixed random seeds (SEED=42) for reproducible results; (c) ModelCheckpoint callback saving only the best validation-accuracy model as best\_model.keras; (d) early stopping with patience=25 rounds in XGBoost to prevent overfitting;

(e) multi-variant evaluation protocol eliminating single-phrase memorization artifacts.

## **4.7 Maintainability**

The codebase is organized into clearly commented Jupyter notebook cells, each with a single responsibility. The class-order alignment mechanism is centralized and documented, preventing silent class-mismatch bugs. Joblib serialization allows independent updating of the text model without retraining the image model. Each notebook cell has a descriptive header comment and print statements for progress monitoring.

**4.8 Portability**

The system was developed on Windows 11 with Python 3.9 in VS Code Jupyter. The dependency stack is fully pip-installable on Windows, macOS, and Linux. Model artifacts (.keras, .pkl) are platform-independent. For Phase 3, Docker containerization is planned to ensure consistent runtime environments across development, staging, and production

## **4.9 Legacy to Modernization**

The project modernizes traditional rule-based and single-modality veterinary diagnostic aids. Legacy symptom questionnaire systems (Patel et al., 2022) are replaced by a transformer-based semantic text encoder (SBERT) that understands clinical context rather than matching keywords. Single-modality CNN classifiers are augmented with a complementary text branch, evolving the paradigm toward true multimodal clinical AI.

## **4.10 Reusability**

The get\_image\_proba() and get\_text\_proba() helper functions are generic and can be adapted to any

6-class (or n-class) classification task by updating CLASS\_NAMES and retraining each branch. The CLASS\_TEXT\_VARIANTS dictionary template can be reused for generating multi-variant evaluation corpora for other veterinary or medical classification domains with minimal modification.

.

## **4.11 Application Compatibility**

The system is compatible with all major operating systems via pip. The SBERT model is downloaded automatically from Hugging Face Hub on first use (all-MiniLM-L6-v2, ~22MB). The TensorFlow model (best\_model.keras) is compatible with TensorFlow 2.x. XGBoost and scikit- learn models are compatible with Python 3.7+. For Phase 3, the system will be exposed via a REST API compatible with web, mobile, and desktop client applications

## **4.12 Resource Utilization**

ResNet50 training was performed on a GPU-enabled machine (NVIDIA CUDA compatible). Inference requires no GPU; the model runs on CPU with acceptable latency (~0.3 seconds per image). SBERT encoding is CPU-based and runs in approximately 50ms per text sample. The XGBoost model inference is near-instantaneous (~1ms). The complete system inference pipeline (image + text + fusion) completes in under 1 second on a standard laptop, making it suitable for real-time clinical support

**CHAPTER 5**

# **HIGH LEVEL SYSTEM DESIGN**

This schematic illustrates a high-level depiction of the complete data flow within the AI-Based Dog Health Monitoring System. The architecture is designed to perform accurate disease prediction by integrating image data, textual symptoms, and metadata inputs using a multimodal late fusion approach.

The system operates through four major stages:
Data Ingestion & Preprocessing, Multimodal Feature Extraction, Fusion & Decision Engine, and Final Output Generation.

![](data:image/png;base64...)

## **5.1 Data Ingestion & Preprocessing Pipeline**

The model processes collected data with its various input parameters, including dog skin images, symptom text descriptions, and optional metadata (age and temperature). Each input stream is processed or feature-engineered individually, with all data collections (real-time/static) going through standardized preprocessing steps within a normalization module.

**Preprocessing:** Data inputs can be either supplemental or foundational for generating predictions. Real-time input is received as a live stream (i.e., user uploads via application interface), while static input is stored in the database for future training and retrieval.

Image preprocessing includes resizing (224 × 224), normalization, and noise reduction.

Text preprocessing includes tokenization, cleaning, and encoding.

Metadata preprocessing includes age encoding and temperature scaling.

After initial preprocessing and normalization, the processed inputs are forwarded to respective learning models. The outputs of these models are stored in the results database, enabling efficient and accurate prediction delivery through the user interface.

**5.2 Multimodal Feature Extraction (Parallel Processing)**

The system processes input data through three parallel pathways, enabling independent feature learning and enhancing overall prediction accuracy. In the image feature extraction path, the processed image input is passed into a pre-trained Convolutional Neural Network (CNN) such as ResNet, EfficientNet, or InceptionNet. This model extracts important visual features including skin lesions, texture variations, and color patterns, and produces a probability distribution over disease classes using a softmax layer. In the text feature extraction path, the processed symptom description is fed into a pre-trained Transformer model such as BERT. This generates two types of representations: a sentence embedding, which captures the overall context of the symptoms (for example, “itching and red patches”), and word embeddings, which represent individual symptoms like itching, redness, swelling, or hair loss. These embeddings are further processed through dense layers to generate classification probabilities.

The core intelligence of the system lies in the feature fusion and decision engine, which combines outputs from multiple modalities into a unified prediction. Using a late fusion mechanism, the system integrates predictions from image features, text features, and metadata. A dynamic and adaptive weighting strategy is applied, where the importance of each modality is determined based on its reliability. For instance, image features are given higher weight when strong visual evidence is present, while text features are prioritized when symptom descriptions are more informative. Metadata provides additional contextual support to refine the prediction. This fusion process results in a final weighted output that includes disease classification, a confidence score, and a risk level estimation, thereby improving robustness and accuracy.

Following prediction, the system employs an evaluation and recommendation engine to ensure reliability and provide actionable insights. A prediction consistency check is performed to verify alignment between image-based and text-based outputs; in cases of inconsistency, the fusion model adjusts the weights to improve accuracy. The system then performs risk assessment by categorizing the condition into low, moderate, or high risk levels, helping users understand the severity and urgency. Based on the predicted disease and associated risk level, the system generates recommendations such as home care measures, preventive actions, and guidance on whether veterinary consultation is necessary. Additionally, all inputs, predictions, and user interactions are logged in a database, supporting continuous system improvement, future analysis, and model retraining.

Top of Form

Bottom of Form

**CHAPTER 6**

## **6.1 Master Class Diagram**

![](data:image/jpeg;base64...)

## **6.2 Component Diagram**

![](data:image/jpeg;base64...)

**6.3 Activity Diagram**

![](data:image/jpeg;base64...)

**6.4 Deployment Diagram**

![](data:image/jpeg;base64...)

## **6.3 Report Layouts**

The system produces two types of automated analytical reports for performance evaluation and debugging purposes. The first type is referred to as Real-time Training Logs (e.g., TensorBoard), and the second type is referred to as Quantitative Evaluation Metrics.

The Real-time Training Log is generated during the training and validation phases of the deep learning models. The system continuously streams real-time telemetry data to an engineer’s monitoring dashboard. This report format includes real-time visualizations such as line charts representing training and validation loss, accuracy trends, and learning curves. These visualizations allow the engineer to observe how effectively the models (image-based CNN and text-based Transformer) are learning and converging over time. It also helps in identifying issues such as overfitting, underfitting, or unstable training behavior.

Following the completion of model training or experimentation (such as hyperparameter tuning or ablation studies), the engineer can utilize the Quantitative Evaluation Metrics module to generate a structured report in CSV format. This report compares the performance of the trained models against baseline models using standard evaluation metrics.

The system evaluates performance using the following key metrics:

Accuracy: Measures the overall correctness of the model’s predictions.

Precision: Indicates how many of the predicted positive cases are actually correct.

Recall: Measures the model’s ability to correctly identify all relevant disease cases.

F1-Score: Provides a balance between precision and recall.

Confidence Score: Represents the probability associated with each prediction.

Additionally, the system can evaluate individual model performance (image-only, text-only) as well as the fusion model, enabling comparative analysis to demonstrate the effectiveness of the multimodal approach.

Top of Form

Bottom of Form

# **CHAPTER 7**

## **Technology Used**

**Deep Learning Framework:**

The primary tool used for implementing the object-oriented neural network architectures is PyTorch (with CUDA and cuDNN support). This framework enables efficient tensor computations, GPU acceleration, and the training of deep learning models such as Convolutional Neural Networks (CNNs) and Transformer-based architectures. It is also used to perform backpropagation, optimization, and model evaluation processes.

**Transformer API and Text Encoders:**

The system utilizes Hugging Face Transformers, specifically pre-trained models such as BERT (Bidirectional Encoder Representations from Transformers), to extract meaningful features from symptom text inputs. These models generate:

Global sentence embeddings (overall symptom context)

Fine-grained word embeddings (specific symptom details)

This enables accurate understanding of textual descriptions provided by users.

**Feature Extraction and Vision Models:**

ResNet / EfficientNet / InceptionNet:
These Convolutional Neural Network architectures are used for extracting deep visual features from dog skin images. They help identify patterns such as lesions, discoloration, and texture variations associated with different diseases.

These models are also used in the evaluation pipeline to ensure robust and reliable image-based predictions.

**Multimodal Fusion and Decision System:**

A custom Late Fusion Model is implemented to combine predictions from image and text modalities along with metadata inputs. This module performs dynamic weighting and generates the final disease classification and confidence score.

**Data Processing and Transformation**:

NumPy: Used for numerical computations and array manipulations.

Pandas: Used for dataset handling and structured data processing.

torchvision.transforms: Used for image preprocessing tasks such as resizing, normalization, and augmentation.

NLTK / Tokenizers: Used for text preprocessing including tokenization and cleaning.

**Model Evaluation and Visualization Tools:**

TensorBoard: Used for monitoring training progress through real-time visualization of loss, accuracy, and other metrics.

Scikit-learn: Used for computing evaluation metrics such as accuracy, precision, recall, and F1-score.

Backend and Deployment Frameworks:

Flask / FastAPI: Used to build REST APIs for model inference and communication between frontend and backend.

Streamlit (optional): Used for rapid prototyping of the user interface.

Database and Storage:

SQLite / MySQL: Used for storing user inputs, prediction results, and logs.

Cloud Storage (optional): Used for dataset storage and scalability.

Environment and Hardware Management:

The system is developed within a virtual environment using tools such as venv or Conda for dependency management. GPU acceleration is enabled using CUDA-compatible hardware to improve training efficiency. The architecture supports

scalable deployment on cloud or local systems, ensuring optimal utilization of available computational resources

**CHAPTER 8**

## **IMPLEMENTATION AND PSEUDOCODE**

The following section provides an account of the concrete programming implementation of the AI-Based Dog Health Monitoring System pipeline. The system is developed using Python, and the PyTorch deep learning framework is employed to construct and train the neural network models. The implementation is organized into three primary components, namely Data Preprocessing, Model Architecture and Objective Functions, and the Multimodal Training and Evaluation Pipeline, which together ensure a structured and efficient workflow for disease prediction.

**8.1 Data Preprocessing & CNN Model Training (resnet50.py)**

This module implements the image-based learning component of the AI-Based Dog Health Monitoring System, where a Convolutional Neural Network is trained to classify dog skin diseases from input images. The preprocessing stage ensures that all images are transformed into a consistent format suitable for deep learning. Each image is resized to a fixed resolution of 224 × 224 pixels and normalized to standardize pixel intensity values, thereby improving model stability and convergence. Data augmentation techniques such as rotation, flipping, and scaling may also be applied to enhance generalization and reduce overfitting.

The processed images are then fed into a pre-trained ResNet50 architecture, which is fine-tuned for the specific task of dog disease classification. Transfer learning is employed to leverage the rich feature extraction capability of ResNet50, allowing the model to capture complex visual patterns such as lesions, discoloration, and texture variations. The final fully connected layer is modified to match the number of disease classes, and a softmax activation function is used to generate probability distributions over the classes. The model is trained using a cross-entropy loss function and optimized using the Adam optimizer. During training, performance is monitored using validation data to ensure proper convergence and to prevent overfitting.

![](data:image/png;base64...)

### **8.2 SBERT + Logistic Regression (Training Text Model)**

### This module focuses on the text-based prediction component of the system, where symptom descriptions provided by users are used to classify potential dog diseases. The textual data is first preprocessed through cleaning and normalization, followed by encoding using Sentence-BERT (SBERT), which generates dense semantic embeddings representing the contextual meaning of the input text. Unlike traditional text representations, SBERT captures both syntactic and semantic relationships, enabling more accurate understanding of symptom descriptions.

### The generated sentence embeddings are then passed to a Logistic Regression classifier, which performs the final classification task. Logistic Regression is chosen due to its simplicity, efficiency, and effectiveness in handling high-dimensional embedding vectors. The model learns to map the semantic representations of symptoms to corresponding disease labels. The training process involves minimizing classification error using appropriate optimization techniques, and the model is evaluated using standard metrics such as accuracy, precision, recall, and F1-score. This lightweight yet powerful approach ensures fast and reliable text-based predictions within the system

### ![](data:image/png;base64...)

### **8.3 Late Fusion Model Implementation**

### The late fusion module represents the core integration mechanism of the AI-Based Dog Health Monitoring System, where predictions from multiple modalities are combined to produce a final decision. In this approach, the outputs of the independently trained image model (ResNet50) and text model (SBERT with Logistic Regression) are fused at the decision level rather than at the feature level. This design allows each model to specialize in its respective domain while contributing to a unified prediction.

### The fusion process takes the probability outputs generated by both models and combines them using a weighted averaging strategy. The weights can be assigned statically or dynamically based on model confidence, enabling the system to prioritize the more reliable modality in different scenarios. For example, when visual features are prominent, the image model may be given higher weight, whereas descriptive symptom text may increase the influence of the text model. Additional metadata such as age and temperature can also be incorporated as auxiliary factors to refine the final prediction.

### The combined output is then passed through a final decision layer to produce the predicted disease class along with a confidence score. This late fusion approach enhances overall system accuracy, robustness, and flexibility by leveraging complementary information from multiple input sources. It also simplifies model design and allows independent optimization of individual components, making the system scalable and adaptable for future improvements.

### ![](data:image/png;base64...)

**CHAPTER 9**

## **CONCLUSION OF CAPSTONE PROJECT PHASE – 2**

Phase 2 was the stage that enabled the transition from understanding machine learning concepts to developing a functional software system that implements these concepts in a real-world scenario. It established the foundational components, including data handling, model architecture, and multimodal integration, required for the final AI-Based Dog Health Monitoring System. The engineering achievements of this phase can be categorized into three major areas.

### **9.1. Data Pipeline Optimization and Preprocessing Efficiency**

While working with a multimodal dataset consisting of dog skin images, textual symptom descriptions, and metadata, several computational and memory-related challenges were encountered. To address these issues, an optimized data preprocessing pipeline was developed to ensure efficient storage and faster data access during training. Image datasets were resized and normalized to a fixed resolution, significantly reducing computational overhead while maintaining relevant visual features.

In addition, efficient data handling mechanisms were implemented using PyTorch DataLoaders, enabling batch-wise data loading and parallel processing. This ensured smooth data flow between CPU and GPU, thereby eliminating bottlenecks during training. The pipeline was designed to support both real-time data input and static dataset usage, making it scalable and adaptable for future extensions. This optimization played a crucial role in improving training speed, stability, and overall system performance.

### **9.2. Object-Oriented System Architecture and Multimodal Modeling**

### The system architecture was implemented using a modular, object-oriented design in PyTorch, allowing clear separation of components such as image processing, text processing, and fusion mechanisms. The image-based model was developed using a pre-trained ResNet50 architecture for extracting deep visual features, while the text-based model utilized SBERT embeddings combined with a Logistic Regression classifier to capture semantic information from symptom descriptions.

### A key contribution of this phase was the implementation of the late fusion model, which integrates predictions from multiple modalities into a unified decision. This fusion mechanism was mathematically designed to combine probability outputs from both image and text models using weighted averaging. The architecture allows dynamic adjustment of weights based on model confidence, enabling more reliable and context-aware predictions.

### The system was trained using a composite objective based on classification loss, ensuring accurate disease prediction across multiple classes. This modular design improves maintainability, allows independent optimization of components, and supports future enhancements such as additional input modalities or advanced fusion strategies.

### **9.3.** **Baseline Implementation and Model Stabilization**

### Initially, the individual models were trained independently to establish a stable baseline performance. The image model (ResNet50) was trained over multiple epochs to learn discriminative visual features of dog skin diseases, while the text model (SBERT with Logistic Regression) was trained to map symptom descriptions to disease categories. During this phase, careful monitoring of training and validation metrics ensured proper convergence and minimized overfitting.

### Following the baseline training, the multimodal fusion approach was introduced to combine predictions from both models. This phase focused on ensuring stable integration and improving overall system accuracy. The fusion model demonstrated improved performance compared to individual models by leveraging complementary information from image and text inputs.

### Through systematic experimentation and validation, the system achieved a balanced performance across different evaluation metrics, indicating reliable prediction capability. The current stage involves fine-tuning model parameters and fusion weights to further enhance accuracy and robustness. This phase establishes a strong foundation for deploying the system in real-world applications, enabling effective and accessible dog health monitoring.

###

**CHAPTER 10**

## **PLAN OF WORK FOR CAPSTONE PROJECT PHASE - 3**

This section presents the final engineering plan to enhance model performance, conduct comprehensive evaluations, and incorporate feedback from the review panel regarding system comparison and deployment readiness..

**Hyperparameter Optimization and Model Stabilization:**

To improve the convergence and overall performance of the system observed in Phase 2, a detailed tuning of hyperparameters will be carried out. This includes optimizing learning rates, batch sizes, and model-specific parameters for both the image-based CNN (ResNet50) and the text-based SBERT model. Special focus will be given to adjusting the weighting factors used in the late fusion mechanism to balance the contributions of image, text, and metadata inputs. Extended training on GPU-enabled systems will be performed to ensure stable convergence, reduce overfitting, and improve generalization across unseen data.

**Incremental Ablation Study:**

To validate the effectiveness of the multimodal architecture, an incremental ablation study will be conducted. The system will be evaluated under different configurations, including image-only, text-only, and combined multimodal models. This comparative analysis will demonstrate the contribution of each component and highlight the performance improvements achieved through the late fusion strategy. The results will provide experimental evidence supporting the design choices and the effectiveness of integrating multiple data modalities.

1. **Quantitative Metric Evaluation:** The finalized system will undergo rigorous evaluation using standard performance metrics. These include accuracy, precision, recall, and F1-score for classification performance, along with confusion matrix analysis to understand class-wise prediction behavior. Additionally, confidence scores will be analyzed to assess prediction reliability. The evaluation results will be documented in a structured format to provide a clear comparison between different models and configurations.

1. **Benchmarking with Alternative Architectures:**

To address feedback from the Phase 2 review panel, a comparative study will be conducted between the proposed multimodal system and alternative approaches such as single-modality models or other deep learning architectures. This benchmarking will focus on factors such as prediction accuracy, inference time, computational efficiency, and scalability. The goal is to demonstrate the advantages of the proposed fusion-based system over traditional approaches in terms of both performance and robustness.

**3.UI Integration and Final Deployment:** In the final stage, the trained models will be integrated into a user-friendly application interface. The PyTorch backend will be deployed using frameworks such as Flask or FastAPI to enable real-time predictions. A web-based interface will allow users to upload images and enter symptoms easily, receiving instant diagnostic results. Additionally, an explainability component will be incorporated to provide insights into model predictions, such as highlighting influential features or displaying confidence levels. This phase ensures that the system is fully functional, accessible, and ready for real-world usage in dog health monitoring..

# **REFERENCES / BIBLIOGRAPHY**

1. A. Kumar, R. Sharma, and S. Gupta, “Deep Learning-Based Pet Disease Diagnosis Using Skin and Fur Images,” in Proc. IEEE International Conference on Advanced Computing and Communication Systems (ICACCS), 2023.
2. S. Patel, R. Nair, and P. Joshi, “Pet Care AI: A Smartphone-Based Health Monitoring Tool for Dogs,” International Journal of Advanced Engineering and Computer Science (IJAECS), vol. 11, no. 4, 2022.
3. Aravind G., Dr. Sasirekha S.P., Jeeva S., and Selvaganesh D., “PawSense: AI-IoT Enabled Smart Pet Care for Real-Time Health Monitoring,” International Journal of Scientific Research (IJSR), vol. 13, no. 6, 2024.
4. S-C. Kim and S. Kim, “Development of a Dog Health Score Using an Artificial Intelligence Disease Prediction Algorithm Based on Multifaceted Data,” Nature Scientific Reports, 2024.
5. L. Chen, M. Zhao, and Y. Li, “A Multimodal Fusion Approach for Veterinary Disease Detection,” IEEE Access, vol. 12, pp. 10000–10015, 2024.
6. B. Abirami and T. Momithasree, “Pet Pulse: Detecting Dog Diseases with TFLite, Booking Vet Consults,” International Journal of Scientific Development and Research (IJSDR), vol. 10, no. 7, July 2025. ISSN: 2455-2631.
7. Bhogapurapu Varun Kumar, Kunjam Nageswara Rao, and Pappala Mohan Rao, “Dog Skin Disease Detection using Deep Learning: A Deep Learning Approach for Accurate Veterinary Diagnosis,” IJSDR, vol. 10, no. 7, July 2025. ISSN: 2455-2631.
8. K. He, X. Zhang, S. Ren, and J. Sun, “Deep Residual Learning for Image Recognition,” in Proc. IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pp. 770–778, 2016.
9. N. Reimers and I. Gurevych, “Sentence-BERT: Sentence Embeddings using Siamese BERT- Networks,” in Proc. EMNLP, 2019. arXiv:1908.10084.
10. T. Chen and C. Guestrin, “XGBoost: A Scalable Tree Boosting System,” in Proc. ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 785–794, 2016.
11. F. Chollet et al., “Keras,” GitHub, 2015. Available: https://github.com/keras-team/keras
12. M. Abadi et al., “TensorFlow: Large-Scale Machine Learning on Heterogeneous Systems,” 2015. Available: https:/[/www.tensorflow.org](http://www.tensorflow.org/)
13. F. Pedregosa et al., “Scikit-learn: Machine Learning in Python,” Journal of Machine Learning Research, vol. 12, pp. 2825–2830, 2011.

T. Wolf et al., “HuggingFace’s Transformers: State-of-the-Art Natural Language Processing,” arXiv:1910.03771, 2019..

**APPENDIX A: DEFINITIONS, ACRONYMS, AND**

**ABBREVIATIONS**

**A.1 Definitions**

Artificial Intelligence (AI):
The simulation of human intelligence processes by machines, especially computer systems, enabling tasks such as learning, reasoning, and problem-solving.

Machine Learning (ML):
A subset of AI that allows systems to learn and improve automatically from experience without being explicitly programmed.

Deep Learning (DL):
A specialized branch of ML that uses neural networks with multiple layers to model complex patterns in data.

Generative Adversarial Network (GAN):
A deep learning model consisting of two networks (Generator and Discriminator) that compete to generate realistic data, such as images.

Image Classification:
The process of assigning a label to an image based on its content.

Feature Extraction:
The process of identifying and selecting important characteristics (features) from raw data for model training.

Convolutional Neural Network (CNN):
A type of deep neural network particularly effective for image processing tasks.

Model Training:
The process of feeding data into a machine learning model so it can learn patterns and make predictions.

Evaluation Metrics:
Measures used to assess the performance of a model (e.g., accuracy, precision, recall).

Dataset:
A collection of data used for training and testing machine learning models.

**A.2 Acronyms and Abbreviations**

AI – Artificial Intelligence

ML – Machine Learning

DL – Deep Learning

GAN – Generative Adversarial Network

CNN – Convolutional Neural Network

RAG – Retrieval-Augmented Generation

IoT – Internet of Things

API – Application Programming Interface

GPU – Graphics Processing Unit

CPU – Central Processing Unit

ResNet – Residual Network

UI – User Interface

UX – User Experience

TP – True Positive

TN – True Negative

FP – False Positive

FN – False Negative

F1 Score – Harmonic mean of precision and recall

**Bottom of Form**

Top of Form

### Bottom of Form