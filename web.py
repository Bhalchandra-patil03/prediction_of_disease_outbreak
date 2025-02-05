import os 
import pickle 
import streamlit as st 
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Prediction Of Disease Outbreak"
                   ,layout='wide'
                   ,page_icon="Doctor")

diabetes_model = pickle.load(open(r"C:\Users\Bhalchandra\Desktop\Prediction_Disease_Outbreak\Training_models\diabetes_model.sav",'rb'))
heart_model = pickle.load(open(r"C:\Users\Bhalchandra\Desktop\Prediction_Disease_Outbreak\Training_models\heart_model.sav",'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\Bhalchandra\Desktop\Prediction_Disease_Outbreak\Training_models\parkinsons_model.sav",'rb'))

with st.sidebar :
    selected = option_menu("Prediction Of Disease Outbreak System",["Diabetes disease Prediction","heart disease prediction","parkinsons Disease prediction"],
                           menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)
    
if selected == 'Diabetes disease Prediction':
    st.title("Diabetes disease Prediction using ML")
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input("Number of Pregnancies")
    with col2:
        Glucose = st.number_input("enter Glucose level")
    with col3:
        BloodPressure = st.number_input("enter BloodPressure ")
    with col1:
        SkinThickness = st.number_input("enter SkinThickness")
    with col2:
        Insulin = st.number_input("enter Insulin value")
    with col3:
        BMI = st.number_input("enter BMI value ")
    with col1:
        DiabetesPedigreeFunction = st.number_input("enter DiabetesPedigreeFunction value")
    with col2:
        Age = st.number_input("enter your Age")

diab_diagnosis = ''
if st.button('Diabetes Test Result'):
    user_input=[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                BMI, DiabetesPedigreeFunction, Age]
    user_input= [int(x) for x in user_input]
    diab_prediction= diabetes_model.predict([user_input])
    if diab_prediction[0]==1:
        diab_diagnosis= 'The person is diabetic'
    else:
        diab_diagnosis= 'The person is not diabetic'
st.success(diab_diagnosis)