# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:50:12 2023

@author: rupal
"""


import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('reg_model.pkl','rb') as file: 
     data = pickle.load(file)
    return data

data = load_model()

regressor_loaded = data["model"]
hours = data["hours"]

def show_predict_page():
    st.title("Student's score prediction")
    
    st.write(""" ### we need some information to predict the marks """)
    
    hrs = st.text_input("Enter number of hours you studey: ", "")
    
    ok = st.button("calculated marks")
    if ok:
        X = np.array([[hrs]])
        X = X.astype(float)
        
        marks = regressor_loaded.predict(X)
        st.subheader(f"The estimated Marks are {marks[0]: .2f}")
        
show_predict_page()