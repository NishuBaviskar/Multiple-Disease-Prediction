# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
import os
from streamlit_option_menu import option_menu

# Define paths dynamically
base_path = os.path.join(os.getcwd(), "saved_models")

def load_model(filename):
    model_path = os.path.join(base_path, filename)
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    return pickle.load(open(model_path, "rb"))

# Load models
diabetes_model = load_model("diabetes_model.sav")
heart_disease_model = load_model("heart_disease_model.sav")
parkinsons_model = load_model("parkinsons_model.sav")

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')   
    col1, col2, col3 = st.columns(3)
    
    with col1: Pregnancies = st.text_input('Number of Pregnancies')
    with col2: Glucose = st.text_input('Glucose Level')
    with col3: BloodPressure = st.text_input('Blood Pressure value')
    with col1: SkinThickness = st.text_input('Skin Thickness value')
    with col2: Insulin = st.text_input('Insulin Level')
    with col3: BMI = st.text_input('BMI value')
    with col1: DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2: Age = st.text_input('Age of the Person')
    
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        try:
            user_input = [float(x) for x in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
            diab_prediction = diabetes_model.predict([user_input])
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        except Exception as e:
            diab_diagnosis = f"Error: {str(e)}"
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    
    inputs = []
    labels = ['Age', 'Sex', 'Chest Pain types', 'Resting Blood Pressure', 'Serum Cholestoral in mg/dl', 'Fasting Blood Sugar > 120 mg/dl',
              'Resting Electrocardiographic results', 'Maximum Heart Rate achieved', 'Exercise Induced Angina', 'ST depression induced by exercise',
              'Slope of the peak exercise ST segment', 'Major vessels colored by flourosopy', 'Thal (0=normal, 1=fixed defect, 2=reversible defect)']
    
    for i, label in enumerate(labels):
        with (col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3):
            inputs.append(st.text_input(label))
    
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            user_input = [float(x) for x in inputs]
            heart_prediction = heart_disease_model.predict([user_input])
            heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        except Exception as e:
            heart_diagnosis = f"Error: {str(e)}"
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction using ML')
    
    parkinsons_inputs = []
    labels = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
              'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
              'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR',
              'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE']
    
    cols = st.columns(5)
    for i, label in enumerate(labels):
        with cols[i % 5]:
            parkinsons_inputs.append(st.text_input(label))
    
    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        try:
            user_input = [float(x) for x in parkinsons_inputs]
            parkinsons_prediction = parkinsons_model.predict([user_input])
            parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        except Exception as e:
            parkinsons_diagnosis = f"Error: {str(e)}"
    st.success(parkinsons_diagnosis)

      