ABSTRACT

Many dog health issues go unnoticed or are detected late because most systems rely on only
one type of input. In this project, the idea is to fix that by using a setup that looks at both the
dog’s photo and the symptoms the owner explains. The image part is checked through deep
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

_________________________________________________________________________________

Dept. of CSE

_ ___

Aug-Dec 2025

1

CHAPTER 1

INTRODUCTION

Our project mainly focuses on creating an AI-based Dog Health Monitoring System that can

look at both a dog’s photo and the symptoms shared by the owner to detect diseases more

accurately. Instead of depending only on images or only on text like many current systems do,

we use a dual-input model so the assessment becomes more complete for small, medium, and

large breeds. Once the visual data is paired with the symptoms, the system can understand the

dog’s condition much faster and give more useful guidance to vets and pet owners.

The whole idea is to use multimodal AI in a practical way so that dog health monitoring

becomes more reliable and actually helps in improving everyday pet care.

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

_________________________________________________________________________________

Dept. of CSE

_ ___

Aug-Dec 2025

1

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

diseases, while others use rule-based systems to answer text-based symptom queries.  On the

other hand, symptom-only systems fail to identify diseases that are supported by important

visual cues like lesions, fur loss, rashes, or discoloration. Lack of a system considering both

forms of evidence together severely limits the reliability and accuracy of existing solutions.

Another big limitation that exists today is the absence of breed-informed diagnostic tools.

Symptoms vary between breeds and breed sizes (small, medium, large), as does their

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

_________________________________________________________________________________

Dept. of CSE

_ ___

Aug-Dec 2025

1

The above challenges can  be addressed with a dual-model AI-based Dog Health Monitoring

System that can take both images and symptom descriptions. Dual input processing applied in

the proposed model relies on deep learning image analysis for the visible abnormalities while,

at the same time, machine learning and NLP techniques can interpret the textual symptom

descriptions that the owner provides. These two forms of evidence are then combined by the

multi-modal AI to generate a more accurate and holistic health assessment. It will not replace

veterinarians, but rather act like a preliminary screening tool to aid the decisions that pet

owners make. our system aims to help users understand whether a symptom is common and

can be monitored at home, or  it indicates wheather it is a serious condition that requires

veterinary care. It helps pet owners with action, insights, reduces unnecessary clinic visits,

and helps  in early detection of diseases.  Our work responds to this need by offering an

intelligent, breed-aware, user-friendly system able to provide trustworthy preliminary

diagnoses, improving the efficiency of pet healthcare and helping both owners and

veterinarians in the pursuit of better health outcomes for dogs.

_________________________________________________________________________________

Dept. of CSE

_ ___

Aug-Dec 2025

1

_________________________________________________________________________________

Dept. of CSE

_ ___

Aug-Dec 2025

1

_________________________________________________________________________________

Dept. of CSE

_ ___

Aug-Dec 2025

1

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
experiencing. Without combined datasets, models cannot perform symptom-image
crossvalidation, which is necessary for accurate diagnosis. This gap also restricts the
development of hybrid architectures using deep learning and machine learning together.

Moreover, much of the existing research completely ignores breed-specific variations. Small,
medium, and large breeds of dogs differ considerably in their physiological, immunological,
symptomatic, and disease manifestation characteristics. A condition that might appear acute
in a small breed may be considered minor in a larger breed, and vice versa. Single-input
systems, not really accounting for these subtleties, often provide generic or even misleading
predictions. One of the major drawbacks with the current state of AI-powered veterinary tools
is the lack of breed-aware models.

_________________________________________________________________________________

Dept. of CSE

_ ___

Aug-Dec 2025

1

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

_________________________________________________________________________________

Dept. of CSE

_ ___

Aug-Dec 2025

1

OBJECTIVES :

To create an AI-based system that uses symptom data and images to identify and track

1.
health issues in dogs.

To use machine learning algorithms to study symptoms and deep learning to detect

2.
diseases from images.

3.To integrate (fuse) clinical and visual characteristics to predict diseases accurately and
early.

4. To create a system that functions well with small, medium, and large dog breeds

5. To design an intuitive user interface that makes it simple for pet owners to enter symptoms

and upload photos.

6.To support early diagnosis and preventive healthcare for veterinarians and pet owners.

7. To ensure our system can grow easily and can connect with new devices and new users by
making health apps in the future

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

_________________________________________________________________________________

Dept. of CSE

_ ___

Aug-Dec 2025

1

Examples of symptoms described in such data include vomiting, diarrhea, loss of appetite,
lethargy, coughing, itching, and abnormal color of waste. Most entries also contain extra
contextual details like duration, frequency, and severity, which allows the model to
understand a wide range of clinical presentations.

The combination of image and text-based datasets would facilitate the development of a
multimodal system that can cross-verify symptoms by visual cues, enabling an even more
accurate and reliable diagnosis. This dataset collection ensures that the model can evaluate
both the external and internal indicators of the onset of an illness for early detection and to
assist pet owners in making informed decisions.

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
_________________________________________________________________________________

Dept. of CSE

_ ___

Aug-Dec 2025

1

Digestive indicators: Color of stool, its consistency, frequency, and patterns of abnormal
waste.

Symptom duration: The length of time the symptom has been experienced.
Severity indicators include: frequency of episodes, intensity of discomfort, and effect on daily
activity.

The features of text are extracted using NLP techniques like tokenization, embedding
methods, and classification models.

C. Breed & Category Features

Since disease expression does vary across breeds, the dataset also includes:

Breed type:  Labrador, German Shepherd, Beagle, Pug.

Breed size categories include small, medium, and large breeds.

Age and gender (if available): Useful for understanding susceptibility.

D. Label Features (Ground Truth)

Each entry in this dataset contains labels like:

Category of disease:  dermatitis, mange, ear infection, malnutrition, allergy, etc.

Health status: healthy / mildly affected / severe

Symptom cluster mapping: Differential diagnosis based on symptoms

These labels enable supervised learning and allow the system to predict probable diseases.

_________________________________________________________________________________

Dept. of CSE

_ ___

Aug-Dec 2025

1

 CONCLUSION OF CAPSTONE PROJECT PHASE – 1

In phase-1 of our capstone project AI-Based Dog Health Monitoring System Using DualInput

(Images + Symptom) , we successfully framed our problem statement. we identified how

difficult it is for pet owners to recognize if their dogs is sick . during this phase, we

researched existing methods like CNN for image and symptom-based classification models

and multi model fusion techniques.

We got to know that combination of datasets is very rare, and initially collected datasets and

whether to build app or website . we also checked practically possible We got to know what

we are suppose to do in phase 2 .

PLAN OF WORK FOR CAPSTONE PROJECT PHASE – 2

In Phase–2, our team will focus on identifying and finalizing suitable datasets for dog images and

symptom information. After selecting the datasets, preprocessing steps such as cleaning, resizing, and

encoding will be carried out. The development of the CNN model for images and the symptom

analysis model will begin based on the available data. The team will begin basic testing of both

models and check how they work together in the system. Our team is designing the system using a

high-level modular approach that allows each component to work independently while still

contributing to a unified prediction output. We are developing two major modules , an image analysis

_________________________________________________________________________________

Dept. of CSE

_ ___

Aug-Dec 2025

1

module and a symptom analysis module. For image processing, our team is implementing a

CNNbased model that identifies visual issues such as skin infections, rashes . At the same time, we

are building an NLP/ML model that interprets the symptoms entered by the pet owner, such as

vomiting, appetite loss, or fatigue. Once both modules generate their predictions, we are integrating

them through a multimodal fusion layer that combines visual and textual evidence to give a more

accurate final diagnosis.

_________________________________________________________________________________

Dept. of CSE

_ ___

Aug-Dec 2025

1

