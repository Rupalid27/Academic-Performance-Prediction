# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 12:05:17 2023

@author: rupal
"""

import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore or Predict", 
                            ("Explore", "Predict"))

if page == "Predict":
   show_predict_page()
else:
    show_explore_page()