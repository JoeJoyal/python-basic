import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# import pickle
import os
from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import joblib

def load_models():
    model_files = {
        "SVC Binary": 'svm_binary.pkl',
        "SVC Multi": "svm_multi.pkl",
        "Logistic Regression Binary": "logistics_binary.pkl",
        # "Logistic Regression OVR": "logistics_ovr.pkl",
        # "Logistic Regression Multinomial": "logistics_multinomial.pkl"
    }
    models = {}

    for model_name, file_name in model_files.items():
        if os.path.exists(file_name):
            with open(file_name, "rb") as file:
                models[model_name] = joblib.load(file)
        else:
            print(f"Warning: {file_name} not found. Skipping {model_name}.")
    return models


def predict(model, data):
    df = pd.DataFrame([data])  # Convert user input to DataFrame
    
    # Remove any extra columns not used during training
    if "model used" in df.columns:
        df = df.drop(columns=["model used"])
    
    prediction = model.predict(df)  # Directly predict without scaling
    return prediction



def main():
    st.title("Iris Flower Classification")
    st.write("Enter the features to classify the iris flower.")
    
    models = load_models()
    model_selection = st.sidebar.selectbox("Select Model", list(models.keys()))
    selected_model = models[model_selection]
    
    sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.0)
    sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.0)
    petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=3.5)
    petal_width = st.number_input("Petal Width (cm)", min_value=0.1, max_value=10.0, value=1.0)
    
    if st.button("Predict Class"):
        user_data = {
            "sepal length (cm)": sepal_length,
            "sepal width (cm)": sepal_width,
            "petal length (cm)": petal_length,
            "petal width (cm)": petal_width,
            "model used": model_selection  # Store model name
        }
        
        prediction = predict(selected_model, user_data)
        iris_data = load_iris()
        predicted_class = iris_data.target_names[prediction[0]]
        user_data["predicted class"] = predicted_class  # Store predicted class
        
        st.success(f"Predicted Iris Class: {predicted_class}")
      
    
    if st.sidebar.button("Select Model"):
        st.sidebar.success(f"You selected {model_selection}")

    upload_file = st.sidebar.file_uploader("Upload your file", type=['csv', 'xlsx'])

    if upload_file is not None:
        try:
            if upload_file.name.endswith('.csv'):
                data = pd.read_csv(upload_file)
            else:
                data = pd.read_excel(upload_file)
            st.sidebar.success("file uploaded successfully")

            st.subheader("I am going to show you a data details")
            st.dataframe(data.head())

            st.subheader("lets see some more detail data")
            st.write("shape of the data", data.shape)
            st.write("the column name inside data is", data.columns)
            st.write("missing value into column", data.isnull().sum())

            st.subheader("I will show you the bit of stats")
            st.write(data.describe())

        except Exception as e:
            print(e)

        def countplot():
            fig_gender = plt.figure(figsize=(10, 4))
            sns.countplot(x='Species', data=data)
            st.pyplot(fig_gender)

        page = st.sidebar.selectbox(
            "Select a Chart",
            [
                "--select--",
                "Count Plot"
            ]
        )

        if page == "Count Plot":
            countplot()

if __name__ == "__main__":
    main()