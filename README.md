An end-to-end machine learning project for predicting customer churn and deploying the trained model as a web application using FastAPI, Streamlit, and Docker.

Project Overview

Customer churn prediction helps identify customers who may be likely to discontinue a service. This project develops a machine learning classification pipeline to predict customer churn from customer, service, and account-related information.

The project covers the complete workflow:

Data Preparation → Exploratory Data Analysis → Preprocessing → Feature Preparation → Model Training → Model Evaluation → Model Saving → FastAPI → Streamlit → Docker

Machine Learning Workflow
Data cleaning and preparation
Exploratory Data Analysis (EDA)
Categorical and numerical feature preprocessing
Feature preparation
Model training and comparison
Classification threshold selection
Model evaluation using F1-score and ROC-AUC
Saving the trained model and preprocessing pipeline
Models Evaluated

The following classification models were built and evaluated:

Logistic Regression
Decision Tree
Random Forest

Logistic Regression with a 0.40 classification threshold performed best based on F1-score and was selected as the final model.

Final Model Performance
Metric	Result
Model	Logistic Regression
Classification Threshold	0.40
F1-Score	73.98%
ROC-AUC	92.74%

The selected threshold was used to prioritize identifying potential churn customers while maintaining a balance between precision and recall.

Deployment

The trained model was deployed as an application using:

Backend
FastAPI
Scikit-learn
Joblib

The FastAPI backend accepts customer information and returns:

Churn probability
Churn prediction
Classification threshold
Frontend
Streamlit
Requests

The Streamlit interface allows users to enter customer information and receive a churn prediction through the FastAPI backend.

Containerization
Docker
Docker Compose

The backend and frontend are containerized separately and managed together using Docker Compose.

Project Structure
telco_customer_churn/
│
├── README.md
├── .dockerignore
├── docker-compose.yml
│
├── notebooks/
│   └── telco_customer_churn_model.ipynb
│
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   ├── preprocessor.pkl
│   └── telco_churn_model.pkl
│
└── frontend/
    ├── Dockerfile
    ├── requirements.txt
    └── streamlit_app.py


End-to-End Architecture
Customer Input
      ↓
Streamlit Frontend
      ↓
FastAPI Backend
      ↓
Preprocessing Pipeline
      ↓
Logistic Regression Model
      ↓
Churn Probability
      ↓
Churn Prediction


Technologies Used
Python
Pandas
NumPy
Scikit-learn
FastAPI
Streamlit
Joblib
Docker
Docker Compose
Jupyter Notebook


Project Objective

The objective of this project was to build a complete machine learning solution that goes beyond model training by integrating the trained model into an API, creating a user interface, and containerizing the application for deployment.

Note

This repository contains the machine learning workflow and deployment implementation developed as part of a portfolio project.