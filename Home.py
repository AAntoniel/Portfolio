import streamlit as st

st.title("Antoniel's Portfolio 📚")

st.write("## Welcome to my portfolio!")
st.write("This portfolio is structured to demonstrate a versatile range of my data science competencies.")

st.divider()

# --- Time Series Project Section ---
st.page_link("pages/1_Time_Series_Project.py", label="🔥📈 **Time Series Project: A Technical Deep Dive**")

st.write("⏱️*Est. Read Time: 20–25 min*")

st.write("""
    This project provides a comprehensive evaluation of daily fire occurrences within the Amazon region 
    through advanced time series forecasting. Utilizing a dataset spanning 2020 to 2024, the analysis 
    identifies the stochastic cycles and temporal dependencies that characterize environmental crises in Northern 
    Brazil. The methodology involves a comparative performance study between classical statistical forecasting (ARIMA) 
    and machine learning algorithms (XGBoost), employing Sliding Window to ensure predictive integrity. 
""")

st.divider()

# --- Heart Disease Project Section ---
st.page_link("pages/2_Heart_Disease_Project.py", label="❤️📊 **Heart Disease Project: Risk Classification & SEMMA Methodology**")

st.write("⏱️*Est. Read Time: 10–15 min*")

st.write("""
    This page presents the full development of a classification model app. It includes 
    data preprocessing, feature selection, model implementation, and performance evaluation. The 
    entire workflow follows the **SEMMA** methodology developed by SAS. 
""")

st.divider()

# --- Heart Disease App Section ---
st.page_link("pages/3_Heart_Disease_App.py", label="❤️📱 **Heart Disease Interactive Screening App**")

st.write("⏱️*Est. Read Time: < 5 min*")

st.write("""
    This is the final application built after the "Heart Disease Project". It serves 
    as a risk assessment tool and is **not** a substitute for medical diagnosis. You can experiment with
    your own or hypothetical data. If the model detects anything unusual, it will highlight it — and in 
    such cases, consulting a medical professional may be advisable. 
""")

st.divider()
