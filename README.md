# Data Science & AI Portfolio

Welcome to my professional portfolio! This repository hosts a multi-page **Streamlit** application that showcases my expertise in Data Science, Machine Learning, and Artificial Intelligence.

Link: https://portfolio-antoniel.streamlit.app/

---

## About the Portfolio
This project is a centralized hub designed to demonstrate my technical skills through real-world applications. Instead of just code, this interactive app provides visualizations, model explanations, and two user-friendly interface for each project.

## Featured Projects

### Time Series Project
An end-to-end study of fire outbreaks in Brazil (2020-2024). It features comparative forecasting using **ARIMA** and **XGBoost** models, validated through **backtesting** strategies to ensure predictive accuracy.

### Heart Disease project
A healthcare-focused classification project. I developed a machine learning model to identify risk factors and built a screening interface that predicts the likelihood of heart disease based on patient data.

### Heart Disease App
The app built from the Heart Disease Screening project, featuring a decoupled architecture where a Streamlit front-end communicates via HTTP requests with a machine learning model deployed as a high-performance FastAPI service on Render, ensuring a professional separation of concerns.

### Resume Chatbot
A **Retrieval-Augmented Generation (RAG)** implementation that transforms my professional resume into an interactive AI. This assistant allows users to query my experience, education, and skills using natural language.

### About Me & Home
* **Home:** A high-level summary of the projects presented in the portfolio.
* **About Me:** A deeper look into my professional background, certifications, and career goals.

---

## Repository Structure
```text

├── chatbot/
│   ├── chroma_db                               # Persistent Vector Store containing resume embeddings
│   ├── chatbot.py                              # RAG logic: handles retrieval and LLM response generation
│
├── images_hd/                                  # Assets and visualizations for the Heart Disease project
│
├── output_TS/                          
│   ├── imgs                                    # Plots and charts for the Time Series analysis
│   ├── metrics                                 # Model performance logs (RMSE, MAE, etc.)
│   ├── values                                  # CSVs containing truth vs. predicted values
│
├── pages/                          
│   ├── 1_Time_Series_Project.py                # Deep dive into the Brazil Forest Fires study
│   ├── 2_Heart_Disease_Project.py              # Technical documentation of the classification model
│   ├── 3_Heart_Disease_App.py                  # Interactive screening interface (connects to FastAPI)
│   ├── 4_Resume_Chatbot.py                     # AI Assistant interface powered by RAG
│   ├── About_me.py                             # Background, certifications, and contact info
│
├── Home.py                                     # Project portal and high-level summary                                         
├── model_heart_disease.pkl                     # Included for model lineage and verification purposes
├── requirements.txt                            # Project dependencies
└── README.md                                   # Project documentation
