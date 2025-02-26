import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# def countPlot():
#     fig = plt.figure(figsize=(10, 4))
#     sns.countplot(x = "year", data = data)
#     st.pyplot(fig)

def main():

    st.title("E-commerence Apps - Black Friday Sale")
    st.sidebar.title("You can upload your file here")

    
    upload_file = st.sidebar.file_uploader("upload your file", type=['csv', 'xlsx'])

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
            fig = plt.figure(figsize=(10, 4))
            sns.countplot(x='Gender', data=data)
            st.pyplot(fig)
    
        page = st.sidebar.selectbox(
            "Select a Chart",
            [
                "--select--",
                "Count Plot",
                "LIne Plot"
            ]
        )

        if page == "Count Plot":
            countplot()


if __name__ == "__main__":
    main()