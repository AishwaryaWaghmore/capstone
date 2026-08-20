Page 1 of 15 - Cover Page Submission ID trn:oid:::1:3418479426
Deepika N
Team-193_capstone-phase-1
Quick Submit
Quick Submit
LIBRARY
Document Details
Submission ID
trn:oid:::1:3418479426 13 Pages
Submission Date 2,949 Words
Nov 20, 2025, 2:39 PM GMT+5:30
17,667 Characters
Download Date
Nov 20, 2025, 3:34 PM GMT+5:30
File Name
Team-193_capstone-phase-1.pdf
File Size
155.1 KB
Page 1 of 15 - Cover Page Submission ID trn:oid:::1:3418479426

Page 2 of 15 - AI Writing Overview Submission ID trn:oid:::1:3418479426
26% detected as AI Caution: Review required.
The percentage indicates the combined amount of likely AI-generated text as It is essential to understand the limitations of AI detection before making decisions
well as likely AI-generated text that was also likely AI-paraphrased. about a student’s work. We encourage you to learn more about Turnitin’s AI detection
capabilities before using the tool.
Detection Groups
9 AI-generated only 26%
Likely AI-generated text from a large-language model.
0 AI-generated text that was AI-paraphrased 0%
Likely AI-generated text that was likely revised using an AI-paraphrase tool
or word spinner.
Disclaimer
Our AI writing assessment is designed to help educators identify text that might be prepared by a generative AI tool. Our AI writing assessment may not always be accurate (i.e., our AI models
may produce either false positive results or false negative results), so it should not be used as the sole basis for adverse actions against a student. It takes further scrutiny and human
judgment in conjunction with an organization's application of its specific academic policies to determine whether any academic misconduct has occurred.
Frequently Asked Questions
How should I interpret Turnitin's AI writing percentage and false positives?
The percentage shown in the AI writing report is the amount of qualifying text within the submission that Turnitin’s AI writing
detection model determines was either likely AI-generated text from a large-language model or likely AI-generated text that was
likely revised using an AI paraphrase tool or word spinner.
False positives (incorrectly flagging human-written text as AI-generated) are a possibility in AI models.
AI detection scores under 20%, which we do not surface in new reports, have a higher likelihood of false positives. To reduce the
likelihood of misinterpretation, no score or highlights are attributed and are indicated with an asterisk in the report (*%).
The AI writing percentage should not be the sole basis to determine whether misconduct has occurred. The reviewer/instructor
should use the percentage as a means to start a formative conversation with their student and/or use it to examine the submitted
assignment in accordance with their school's policies.
What does 'qualifying text' mean?
Our model only processes qualifying text in the form of long-form writing. Long-form writing means individual sentences contained in paragraphs that make up a
longer piece of written work, such as an essay, a dissertation, or an article, etc. Qualifying text that has been determined to be likely AI-generated will be
highlighted in cyan in the submission, and likely AI-generated and then likely AI-paraphrased will be highlighted purple.
Non-qualifying text, such as bullet points, annotated bibliographies, etc., will not be processed and can create disparity between the submission highlights and the
percentage shown.
Page 2 of 15 - AI Writing Overview Submission ID trn:oid:::1:3418479426

Page 3 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426
ABSTRACT
Many dog health issues go unnoticed or are detected late because most systems rely on only
one type of input. In this project, the idea is to fix that by using a setup that looks at both the
dog’s photo and the symptoms the owner explains. The image part is checked through deep-
learning methods, while the symptoms are handled with a simpler machine-learning
approach. When both of these are combined, the system gives results that are earlier and
usually more trustworthy for dogs of different sizes and breeds. The whole point is to make
things a bit easier for vets and even for pet owners, so they can catch problems sooner instead
of waiting until the dog gets worse.
The project is centred on creating a straightforward system that collects a dog’s health details,
cleans and organizes the data, and then trains models that learn from both the photos and the
symptoms provided. Since different breeds and sizes of dogs show health issues differently,
the system tries to adjust its predictions based on that. It also gives owners an easy page
where they can upload a picture of their dog and mention any signs they’ve noticed, and it
quickly shows what the issue might be. Later on, this work could grow into a mobile app so
that owners can keep track of their dog’s health in real time. Overall, the project sets the
groundwork for a practical, AI-based health monitoring system that understands breed
differences and makes checking a dog’s condition much easier.
__________________________________________________________________________________
___
Dept. of CSE Aug-Dec 2025 1
Page 3 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426

Page 4 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426
CHAPTER 1
INTRODUCTION
Our project mainly focuses on creating an AI-based Dog Health Monitoring System that can
look at both a dog’s photo and the symptoms shared by the owner to detect diseases more
accurately. Instead of depending only on images or only on text like many current systems
do, we use a dual-input model so the assessment becomes more complete for small, medium,
and large breeds. Once the visual data is paired with the symptoms, the system can
understand the dog’s condition much faster and give more useful guidance to vets and pet
owners.
The whole idea is to use multimodal AI in a practical way so that dog health monitoring
becomes more reliable and actually helps in improving everyday pet care.
__________________________________________________________________________________
___
Dept. of CSE Aug-Dec 2025 1
Page 4 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426

Page 5 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426
PROBLEM STATEMENT
With more and more people depending on their pets for companionship and emotional
support, the health management of pets is a growing concern for millions of pet owners.
Highly expressive animals, dogs usually manifest subtle changes in behavior, appetite,
physical appearance, or energy levels as early signs of some sort of discomfort or illness.
Still, the majority of such indicators are not that easy for non-professionals to interpret
correctly. Unlike humans, they cannot express feelings of pain or symptoms; it is up to the
dog owners to second-guess what was causing the problem based on limited knowledge or
information from the internet, which often leads to inaccurate assumptions or delayed
medical attention.
Traditional veterinary care often requires the owners to physically see a clinic, even for minor
complaints such as sudden vomiting, skin irritation, abnormal stool, or a change in activity
level. Although it is crucial to visit a veterinarian in serious cases, this may be very expensive
for every small symptom, especially if a family owns more than one pet. Besides, there are
also other limitations that some pet owners may face: busy schedules, lack of transportation,
or limited availability of veterinary facilities within the place of their residence. Such
situations usually lead to a delay in seeking medical consultation until the symptoms become
intense, which compromises the possibility of early diagnosis and timely treatment.
Most of the digital pet-health tools and mobile applications available today address only one
aspect of the problem. For instance, some apps provide image-based diagnosis of skin
diseases, while others use rule-based systems to answer text-based symptom queries. On the
other hand, symptom-only systems fail to identify diseases that are supported by important
visual cues like lesions, fur loss, rashes, or discoloration. Lack of a system considering both
forms of evidence together severely limits the reliability and accuracy of existing solutions.
Another big limitation that exists today is the absence of breed-informed diagnostic tools.
Symptoms vary between breeds and breed sizes (small, medium, large), as does their
__________________________________________________________________________________
___
Dept. of CSE Aug-Dec 2025 1
Page 5 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426

Page 6 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426
susceptibility to diseases and their appearance. Certain skin conditions will look very
different in short-haired versus long-haired dogs, and appetite loss on a large breed can be
very different in implication from the same condition on a small breed. Without the
information provided by breed-specific factors, single-input systems give inconsistent and
sometimes misleading results.
The lack of multimodal datasets further complicates the development of accurate health
monitoring tools. Most available dog-health datasets include symptom descriptions or
images, but rarely both together. Because of this, existing AI models are not learning the
natural relationship between what owners observe-symptoms-and what the dog visually
presents-images. This sets up a significant gap in research findings and points to the need for
a unified, multimodal approach.
The above challenges can be addressed with a dual-model AI-based Dog Health Monitoring
System that can take both images and symptom descriptions. Dual input processing applied in
the proposed model relies on deep learning image analysis for the visible abnormalities while,
at the same time, machine learning and NLP techniques can interpret the textual symptom
descriptions that the owner provides. These two forms of evidence are then combined by the
multi-modal AI to generate a more accurate and holistic health assessment. It will not replace
veterinarians, but rather act like a preliminary screening tool to aid the decisions that pet
owners make. our system aims to help users understand whether a symptom is common and
can be monitored at home, or it indicates wheather it is a serious condition that requires
veterinary care. It helps pet owners with action, insights, reduces unnecessary clinic visits,
and helps in early detection of diseases. Our work responds to this need by offering an
intelligent, breed-aware, user-friendly system able to provide trustworthy preliminary
diagnoses, improving the efficiency of pet healthcare and helping both owners and
veterinarians in the pursuit of better health outcomes for dogs.
__________________________________________________________________________________
___
Dept. of CSE Aug-Dec 2025 1
Page 6 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426

Page 7 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426
   Literature survey

Details of Paper-  year  Methodology Used  Result  Limitations
Title, author,
conference /Journal
Deep Learning-Based  2023  Used CNN (ResNet50)  Achieved 91%  Focused only on images
Pet Disease  for classification of pet  accuracy in   ignores symptom-based diagnostics.
| Diagnosis Using Skin  |     | skin diseases from  | detecting visible  |     |
| --------------------- | --- | ------------------- | ------------------ | --- |
| and Fur Images        |     | image datasets.     | infections.        |     |
A. Kumar, R.
Sharma, S. Gupta
Pet Care AI: A  2021  Designed rule-based  Assisted remote  No machine learning or
Smartphone-Based  expert system for dog  users to self-check  image processing; limited adaptability.
Health Monitoring  disease diagnosis based  dog health issues.
| Tool for Dogs   |     | on user-input symptoms.  |     |     |
| --------------- | --- | ------------------------ | --- | --- |
S. Patel, R. Nair, P.
Joshi
PawSense: AI-IoT  2025  Combined AI, IoT, and  Enabled real-time  Only uses IoT sensor data; lacks
Enabled Smart Pet  blockchain in a Flutter- anomaly detection  integration of image and symptom-based
Care for Real-Time  based pet care system.  and predictive  AI models.
| Health Monitoring      |     | Real-time health data   | alerts for pet    |     |
| ---------------------- | --- | ----------------------- | ----------------- | --- |
| Aravind G., Dr.        |     | from IoT collars        | health. Improved  |     |
| Sasirekha S.P., Jeeva  |     | processed with deep     | security and      |     |
| S., Selvaganesh D.     |     | learning on cloud-edge  | latency.          |     |
architecture.

__________________________________________________________________________________
___
|     | Dept. of CSE  |     | Aug-Dec 2025  | 1   |
| --- | ------------- | --- | ------------- | --- |

Page 7 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426

Page 8 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
Details of Paper-  year  Methodology Used  Result  Limitations
Title, author,
conference /Journal
Development of a  2024  Activity sensors  Achieved ~87.5%  Only behavioral data from sensors; doesn’t include images or symptom-text
Dog Health Score  (leash/wearables)  concordance with  fusion.
Using an Artificial  monitoring behaviors  veterinarian diagnoses.
| Intelligence Disease  |     | (scratching, licking,    |     |     |
| --------------------- | --- | ------------------------ | --- | --- |
| Prediction            |     | swallowing, sleep) + AI  |     |     |
| Algorithm Based on    |     | algorithm to assign a    |     |     |
| Multifaceted Data     |     | “Health Score”.          |     |     |
S-C Kim & S. Kim
A Multimodal  2024  Combined CNN (images)  Fusion improved  Model focused on livestock; not adapted for pet species or user-facing
Fusion Approach  and LSTM (text  accuracy by 12% over  systems..
| for Veterinary      |     | symptoms) for disease     | single-modal models  |     |
| ------------------- | --- | ------------------------- | -------------------- | --- |
| Disease Detection   |     | prediction in livestock.  |                      |     |
L. Chen, M. Zhao,
Y. Li
Pet Pulse: Detecting  2025  Mobile app combining  Demonstrated ability  Limited described dataset; possibly restricted to skin/disease types; full
Dog Diseases with  symptom tracking + pulse  for owners to detect  multimodal (symptoms + image + text) integration not completely detailed.
| TFLite, Booking  |     | monitoring + image  | pet skin/health issues  |     |
| ---------------- | --- | ------------------- | ----------------------- | --- |
| Vet Consults”    |     | processing (skin    | via mobile app;         |     |
B. Abirami & T.  conditions) using TFLite  improved accessibility
| Momithasree   |     | on smartphone. I  |     |     |
| ------------- | --- | ----------------- | --- | --- |
__________________________________________________________________________________
___
|     | Dept. of CSE  |     | Aug-Dec 2025  | 1   |
| --- | ------------- | --- | ------------- | --- |

Page 8 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426

Page 9 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426
Research Gap
While significant strides are being made in the field of veterinary technology and AI-based
health analysis, several critical gaps persist that curtail the effectiveness of existing solutions
for dog health monitoring. Most systems today work exclusively with either image-based
data or text-based symptoms as inputs. Image-only diagnostic systems have gained much
popularity, particularly for skin infections, rashes, or other external abnormalities. Many of
the common ailments affecting dogs, such as digestive issues, viral infections, fever, or
internal discomfort, do not necessarily show strong visual signs. Hence, image-only systems
fail to capture the complete clinical features of such ailments and end up with incomplete or
inaccurate assessments.
On the contrary, symptom-based tools rely solely on the descriptions given by the users,
which introduces a high level of subjectivity. Pet owners can misinterpret symptoms, fail to
notice important details, or give incomplete information about the symptoms exhibited. A
symptom-only system, without visual confirmation, cannot distinguish between diseases that
present similar symptoms. Most current text-based models also have high dependence on
preliminary rule-based systems or small datasets; thus, generalizing across a wide array of
breeds, ages, and health conditions is limited.
Another major research gap is that dog health monitoring lacks a multimodal dataset. Most
publicly available datasets either comprise images of skin diseases or symptom descriptions,
but rarely both together. This separation of symptom reports and images prevents AI models
from learning the natural correlation between what a dog looks like and what it is
experiencing. Without combined datasets, models cannot perform symptom-image cross-
validation, which is necessary for accurate diagnosis. This gap also restricts the development
of hybrid architectures using deep learning and machine learning together.
Moreover, much of the existing research completely ignores breed-specific variations. Small,
medium, and large breeds of dogs differ considerably in their physiological, immunological,
symptomatic, and disease manifestation characteristics. A condition that might appear acute
in a small breed may be considered minor in a larger breed, and vice versa. Single-input
systems, not really accounting for these subtleties, often provide generic or even misleading
predictions. One of the major drawbacks with the current state of AI-powered veterinary tools
is the lack of breed-aware models.
__________________________________________________________________________________
___
Dept. of CSE Aug-Dec 2025 1
Page 9 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426

Page 10 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426
Besides these, accessibility and usability present further gaps. Many AI-powered diagnostic
tools require some technical understanding from the users, high-quality images, or sets of
symptoms that are too descriptive for an average pet owner to provide. This reduces effective
adoption in practical real-life scenarios. The clear need is for a user-friendly, intuitive
interface where a pet owner can simply upload an image, describe basic symptoms, and
receive a reliable preliminary health assessment.
Finally, there is minimal work represented in the existing literature regarding the integration
of deep learning–based visual analysis with machine learning/NLP-based symptom
interpretation in the veterinary domain. While multimodal learning has been effective in
human healthcare, it has not been extended to animal health monitoring in an effective way.
This itself shows a significant unexplored frontier with strong potential for innovation.
__________________________________________________________________________________
___
Dept. of CSE Aug-Dec 2025 1
Page 10 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426

Page 11 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426
OBJECTIVES :
1. To create an AI-based system that uses symptom data and images to identify and track
health issues in dogs.
2. To use machine learning algorithms to study symptoms and deep learning to detect
diseases from images.
3.To integrate (fuse) clinical and visual characteristics to predict diseases accurately and
early.
4. To create a system that functions well with small, medium, and large dog breeds
5. To design an intuitive user interface that makes it simple for pet owners to enter symptoms
and upload photos.
6.To support early diagnosis and preventive healthcare for veterinarians and pet owners.
7. To ensure our system can grow easily and can connect with new devices and new users by
making health apps in the future
__________________________________________________________________________________
___
Dept. of CSE Aug-Dec 2025 1
Page 11 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426

Page 12 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426
Overview of datasets
4.1 Description
Datasets are critical in enabling the multimodal learning approach, where both visual and
textual information are put together to assess the health condition of a dog. Data was
collected from publicly available sources, reliable data science communities, and resources
such as Kaggle, Roboflow, and HuggingFace that host large datasets with great diversity and
well-labeled examples, both of dog images and symptom descriptions.
These include photographs of dogs with visible health issues such as skin infections, rashes,
fur loss, discoloration, woulds, and other visible abnormalities. These images are taken under
different light conditions, angles, and environments that help in improving the robustness of
the model. The datasets also contain healthy images to enable the model to identify the
difference between normal and abnormal visual indicators.
Apart from the images, textual symptom datasets were obtained from veterinary symptom
repositories and crowdsourced forums available in HuggingFace and similar platforms.
Examples of symptoms described in such data include vomiting, diarrhea, loss of appetite,
lethargy, coughing, itching, and abnormal color of waste. Most entries also contain extra
contextual details like duration, frequency, and severity, which allows the model to
understand a wide range of clinical presentations.
The combination of image and text-based datasets would facilitate the development of a
multimodal system that can cross-verify symptoms by visual cues, enabling an even more
accurate and reliable diagnosis. This dataset collection ensures that the model can evaluate
both the external and internal indicators of the onset of an illness for early detection and to
assist pet owners in making informed decisions.
__________________________________________________________________________________
___
Dept. of CSE Aug-Dec 2025 1
Page 12 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426

Page 13 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426
4.2 Data Attributes / Features
Therefore, to construct a powerful multimodal AI framework, two important types of features
are extracted from images and symptom descriptions. Such features enable the model to
understand the health condition of the dog from two perspectives: visual and clinical.
A. Image Features
The key image-related attributes include:
Skin/fur coloration changes: Color patterns indicating possible infection, irritation, or
inflammation in skin or fur.
Variations in skin texture: feeling coarse, dry with bumps or other irregularities.
Lesion characteristics Size, shape, and distribution of rashes, wounds, or patches
Alopecia: Circular or patchy areas of thinning or lost fur, usually due to allergic reactions or
fungal infections.
Swelling or redness could be indicative of allergic reactions or bacterial infections.
Image metadata include resolution, lighting conditions, and background information.
Features are extracted using CNNs, which enable the model to learn the visual patterns
associated with different disease categories.
B. Symptom Text Features
The text dataset contributes clinical attributes such as:
Primary symptoms: vomiting, diarrhea, itching, coughing, fatigue, less appetite, etc.
Behavioral changes: Increased restlessness, weakness, excessive licking, or social
withdrawal.
Digestive indicators: Color of stool, its consistency, frequency, and patterns of abnormal
waste.
Symptom duration: The length of time the symptom has been experienced.
Severity indicators include: frequency of episodes, intensity of discomfort, and effect on daily
activity.
The features of text are extracted using NLP techniques like tokenization, embedding
methods, and classification models.
C. Breed & Category Features
__________________________________________________________________________________
___
Dept. of CSE Aug-Dec 2025 1
Page 13 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426

Page 14 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426
Since disease expression does vary across breeds, the dataset also includes:
Breed type: Labrador, German Shepherd, Beagle, Pug.
Breed size categories include small, medium, and large breeds.
Age and gender (if available): Useful for understanding susceptibility.
D. Label Features (Ground Truth)
Each entry in this dataset contains labels like:
Category of disease: dermatitis, mange, ear infection, malnutrition, allergy, etc.
Health status: healthy / mildly affected / severe
Symptom cluster mapping: Differential diagnosis based on symptoms
These labels enable supervised learning and allow the system to predict probable diseases.
__________________________________________________________________________________
___
Dept. of CSE Aug-Dec 2025 1
Page 14 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426

Page 15 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426
CONCLUSION OF CAPSTONE PROJECT PHASE – 1
In phase-1 of our capstone project AI-Based Dog Health Monitoring System Using Dual-
Input (Images + Symptom) , we successfully framed our problem statement. we identified
how difficult it is for pet owners to recognize if their dogs is sick . during this phase, we
researched existing methods like CNN for image and symptom-based classification models
and multi model fusion techniques.
We got to know that combination of datasets is very rare, and initially collected datasets and
whether to build app or website . we also checked practically possible
We got to know what we are suppose to do in phase 2 .
PLAN OF WORK FOR CAPSTONE PROJECT PHASE – 2
In Phase–2, our team will focus on identifying and finalizing suitable datasets for dog images and
symptom information. After selecting the datasets, preprocessing steps such as cleaning, resizing, and
encoding will be carried out. The development of the CNN model for images and the symptom
analysis model will begin based on the available data. The team will begin basic testing of both
models and check how they work together in the system. Our team is designing the system using a
high-level modular approach that allows each component to work independently while still
contributing to a unified prediction output. We are developing two major modules , an image analysis
module and a symptom analysis module. For image processing, our team is implementing a CNN-
based model that identifies visual issues such as skin infections, rashes . At the same time, we are
building an NLP/ML model that interprets the symptoms entered by the pet owner, such as vomiting,
appetite loss, or fatigue. Once both modules generate their predictions, we are integrating them
through a multimodal fusion layer that combines visual and textual evidence to give a more accurate
final diagnosis.
__________________________________________________________________________________
___
Dept. of CSE Aug-Dec 2025 1
Page 15 of 15 - AI Writing Submission Submission ID trn:oid:::1:3418479426