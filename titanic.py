# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:28:03 2024

@author: HP
"""

import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open("titanic_model.sav",'rb'))

def survival_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0]==0):
        return 'The person did not survive'
    else:
        return 'The person survived'
        
def main():
    st.title("Titanic Survival Prediction")
    
    col1,col2,col3=st.columns(3)
    
    
    with col1:
        Pclass = st.number_input("Passenger Class")
    with col2:
        Sex = st.number_input("Sex")
    with col3:
        Age = st.number_input("Age")
    with col1:
        Sibsp = st.number_input("Siblings/Spouses on board")
    with col2:
        Parch = st.number_input("Parent and Children on board")
    with col3:
        Fare = st.number_input("Fare")
    with col1:
        Embarked = st.number_input("Port where you boarded")
    
    prediction=""
    
    if st.button("Press for result"):
        prediction = survival_prediction([Pclass,Sex,Age,Sibsp,Parch,Fare,Embarked])
    
    st.success(prediction)

if __name__ =="__main__":
    main()
