import streamlit as st

st.title("Antoniel's Portfolio 📚")

st.write(
    """
    ## Welcome to my portfolio!  
    **Please feel free to explore the projects in the menu on the side. Below are brief descriptions 
    of each one.**

    ### 🔥📊Time Series Project
    This project analyzes wildfire occurrences in Brazil. After an initial exploratory analysis, 
    it was identified that the Amazon biome is the most affected region. Based on this insight, 
    a time series was constructed, analyzed, and two forecasting models were evaluated.

    ### ❤️📈Heart Disease Project
    This page presents the full development of a classification model app. It includes 
    data preprocessing, feature selection, model implementation, and performance evaluation. The 
    entire workflow follows the **SEMMA** methodology developed by SAS.

    ### ❤️📱 Heart Disease App
    This is the final application built after the "Heart Disease Project". It serves 
    as a risk assessment tool and is **not** a substitute for medical diagnosis. You can experiment with
    your own or hypothetical data. If the model detects anything unusual, it will highlight it — and in 
    such cases, consulting a medical professional may be advisable. 
    """
)
