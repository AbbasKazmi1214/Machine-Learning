# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:01:29 2024

@author: HP
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav','rb'))

# sidebar for navigation to different diseases
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction','Parkinsons Prediction'],
                           
                           icons = ['heart-pulse','virus'],
                           
                           default_index=0) # default index helps us to set the default Prediction System to appear in the web page when it opens

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    # page title  
    st.title('Diabetes Prediction using Machine Learning')
    
    # Getting the input data from the user
    # columns for input fields
    col1,col2,col3,col4=st.columns(4)
    
    with col1:
        Pregnancies = st.text_input("Enter the no. of pregnancies you had!")
    with col2:
        Glucose = st.text_input("Enter your glucose level!")
    with col3:
        BloodPressure = st.text_input("Enter your Blood Pressure rate!!")
    
    with col4:
        SkinThickness = st.text_input("Enter your skin thickness!!")
    with col1:
        Insulin = st.text_input("Enter your insulin level!!")
    with col2:
        BMI = st.text_input("Enter your BMI!")
    with col3:
        DiabetesPedigreeFunction = st.text_input("Enter Diabetes Pedigree Function!!")
    with col4:
        Age = st.text_input("Enter your age!!")
    
    #code for prediction
    diab_diagnosis = " "
    
    # creating a button
    
    if st.button("Press for result :>"):
        user_input = diabetes_model.predict([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])
        
        if(diab_prediction[0]=='1'):
            diab_diagnosis='You are Diabetic :<'
        else:
            diab_diagnosis='You are Good :>'
    st.success(diab_diagnosis)
    
    
    
    
    
if (selected=='Parkinsons Prediction'):
    st.title('Parkinsons Prediction using Machine learning')
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
       fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
       fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
       flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
       Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
       Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
       RAP = st.text_input('MDVP:RAP')

    with col2:
       PPQ = st.text_input('MDVP:PPQ')

    with col3:
       DDP = st.text_input('Jitter:DDP')

    with col4:
       Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
       Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
       APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
       APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
       APQ = st.text_input('MDVP:APQ')

    with col4:
       DDA = st.text_input('Shimmer:DDA')

    with col5:
       NHR = st.text_input('NHR')

    with col1:
       HNR = st.text_input('HNR')

    with col2:
       RPDE = st.text_input('RPDE')

    with col3:
       DFA = st.text_input('DFA')

    with col4:
       spread1 = st.text_input('spread1')

    with col5:
       spread2 = st.text_input('spread2')

    with col1:
       D2 = st.text_input('D2')

    with col2:
       PPE = st.text_input('PPE')

    park_diagnosis = " "
    
    # creating a button
    
    if st.button("Press for result :>"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        
        user_input = [float(x) for x in user_input]
        park_prediction = parkinsons_model.predict([user_input])
        
        if(park_prediction[0]=='1'):
            park_diagnosis='You have Parkinsons Disease :<'
        else:
            park_diagnosis='You are Good :>'
    st.success(park_diagnosis)
    