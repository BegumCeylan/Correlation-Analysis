# Correlation-Analysis
<h1>Correlation Analysis Between Atrributes and the Target </h1>

The dataset provided is from a study of heart disease. The study collects various measurements on patient health and cardiovascular statistics, and of course makes patient identities anonymous.

Feature, Type, Description
01. age         - int      - Age of patient (in years)
02. gender      - cat      - Gender of patient (Female/Male)
03. cp          - cat      - Type of chest pain (Typical Angina, Atypical Angina, Non-anginal Pain, Asymptomatic)
04. trestbps    - float    - Resting blood pressure (in mm Hg) on admission to hospital 
05. chol        - float    - Serum Cholestrol in mg/dl  
06. fbs         - cat      - Fasting blood pressure > 120 mg/dl? (True: T, False: F)         
07. restecg     - cat      - Resting electrocardiographic (ECG) results (Normal, Having ST-T wave abnormality, Left ventricular hyperthrophy)
08. thalach     - int      - Maximum heart rate achieved (in beats per minute)
09. exang       - cat      - Exercise-induced angina/chest pain (True: T, False: F)
10. oldpeak     - float    - ST depression induced by exercise relative to rest (pressure of the ST segment) 
11. slope       - ordinal  - The slope of the peak exercise ST segment (1: Up, 2: Flat, 3: Down)
12. ca          - int      - Number of major vessels colored by flourosopy (0-3)             
13. thal        - cat      - Thalassemia - Results of thallium stress test measuring blood flow to the heart with possible values (Normal, Fixed defect, Reversible defect)
                         
<b>The goal is to predict the target class which represents whether or not a patient has heart disease (marked as Disease or Nodiease):</b>

More on the features (towardsdatascience.com/heart-disease-prediction-73468d630cfc):

Angina (Chest Pain): Angina is chest pain or discomfort caused when your heart muscle doesn’t get enough oxygen-rich blood. It may feel like pressure or squeezing in your chest. The discomfort also can occur in your shoulders, arms, neck, jaw, or back. Angina pain may even feel like indigestion.

Resting Blood Pressure: Over time, high blood pressure can damage arteries that feed your heart. High blood pressure that occurs with other conditions, such as obesity, high cholesterol or diabetes, increases your risk even more.

Serum Cholesterol: A high level of low-density lipoprotein (LDL) cholesterol (the “bad” cholesterol) is most likely to narrow arteries. A high level of triglycerides, a type of blood fat related to your diet, also ups your risk of a heart attack. However, a high level of high-density lipoprotein (HDL) cholesterol (the “good” cholesterol) lowers your risk of a heart attack.

Fasting Blood Sugar: Not producing enough of a hormone secreted by your pancreas (insulin) or not responding to insulin properly causes your body’s blood sugar levels to rise, increasing your risk of a heart attack.

Resting ECG: For people at low risk of cardiovascular disease, the USPSTF concludes with moderate certainty that the potential harms of screening with resting or exercise ECG equal or exceed the potential benefits. For people at intermediate to high risk, current evidence is insufficient to assess the balance of benefits and harms of screening.

Max heart rate achieved: The increase in cardiovascular risk, associated with the acceleration of heart rate, was comparable to the increase in risk observed with high blood pressure. It has been shown that an increase in heart rate by 10 beats per minute was associated with an increase in the risk of cardiac death by at least 20%, and this increase in the risk is similar to the one observed with an increase in systolic blood pressure by 10 mm Hg.

Exercise induced angina: The pain or discomfort associated with angina usually feels tight, gripping or squeezing, and can vary from mild to severe. Angina is usually felt in the center of your chest but may spread to either or both of your shoulders, or your back, neck, jaw or arm. It can even be felt in your hands. o Types of Angina a. Stable Angina / Angina Pectoris b. Unstable Angina c. Variant (Prinzmetal) Angina d. Microvascular Angina.

Peak exercise ST segment: A treadmill ECG stress test is considered abnormal when there is a horizontal or down-sloping ST-segment depression ≥ 1 mm at 60–80 ms after the J point. Exercise ECGs with up-sloping ST-segment depressions are typically reported as an ‘equivocal’ test. In general, the occurrence of horizontal or down-sloping ST-segment depression at a lower workload (calculated in METs) or heart rate indicates a worse prognosis and higher likelihood of multi-vessel disease. The duration of ST-segment depression is also important, as prolonged recovery after peak stress is consistent with a positive treadmill ECG stress test. Another finding that is highly indicative of significant CAD is the occurrence of ST-segment elevation > 1 mm (often suggesting transmural ischemia); these patients are frequently referred urgently for coronary angiography.

<b>The features and the target used in this data set are expleined in the table above. Based on the type column for these variables, the aim is to conduct a detailed correlation analysis and find the correlation between the target variable and all other features. Also identifying those features that have a potential to impact the target variable, whether the disease is present or not.</b>

