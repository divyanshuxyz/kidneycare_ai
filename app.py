import streamlit as st
import joblib
import numpy as np

# Load the trained model
loaded_model = joblib.load('model.pkl')  
st.image('logo.jpeg')

# Define the Streamlit app
st.title('Enter value for prediction')
# Collect user input
age = st.slider('Age', 0, 100, 30)
bp = st.slider('Blood Pressure (mm Hg)', 50, 200, 120)
sg = st.slider('Specific Gravity', 1.0, 1.05, 1.02)
al = st.slider('Albumin', 0, 5, 0)
su = st.slider('Sugar', 0, 5, 0)
rbc=st.radio('Red Blood Cell [Normal-0, Abnormal-1]', [0, 1])
pul=st.radio('Pus Cells [Abnormal-0, Normal-1]', [0, 1])
pccl=st.radio('Pus Cell Clumps [Not Present-0 , Present-1]', [0, 1])
bac=st.radio('Bacteria [Not Present-0 , Present-1]', [0, 1])
bgr = st.slider('Blood Glucose Random (mg/dL)', 50, 250, 120)
bu = st.slider('Blood Urea (mg/dL)', 10, 250, 40)
sc = st.slider('Serum Creatinine (mg/dL)', 0.4, 15.0, 1.0)
sod = st.slider('Sodium (mEq/L)', 100, 200, 135)
pot = st.slider('Potassium (mEq/L)', 2.5, 7.0, 4.0)
hemo = st.slider('Hemoglobin (g/dL)', 3.0, 17.0, 12.0)
pcv = st.slider('Packed Cell Volume (%)', 10, 70, 38)
wc = st.slider('White Blood Cell Count (cells/cubic mm)', 2000, 25000, 8000)
rbcc = st.slider('Red Blood Cell Count (millions/cubic mm)', 2.0, 7.0, 5.0)
hyp=st.radio('Hypertension [No-0 , Yes-1]', [0, 1])
dia=st.radio('Diabetes Mellitus [Not Present-0 , Present-1]', [0, 1])
cor=st.radio('Coronary Artery Disease [Not-0 , Yes-1]', [0, 1])
appe=st.radio('Appetite [Good-0 , Poor-1]', [0, 1])
ped=st.radio('Pedal Edema [No-0 , Yes-1]', [0, 1])
aane=st.radio('Aanemia [No-0 , Yes-1]', [0, 1])
# Perform prediction when a button is clicked
if st.button('Predict'):
    # Prepare the input data for prediction
    input_data = np.array([[
        age, bp, sg, al, su, rbc, pul, pccl, bac, bgr, bu, sc, sod, pot, hemo, pcv, wc, rbcc, hyp, dia, cor, appe, ped, aane
    ]])
    
    # Make the prediction
    prediction = loaded_model.predict(input_data)

    # Display the prediction result
    if prediction[0] == 0:
        st.write('Prediction: Person is suffering from Kidney Disease')
    else:
        st.write('Prediction: Person is not suffering from Kidney Disease')
# streamlit run app.py
