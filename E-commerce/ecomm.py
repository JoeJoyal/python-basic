import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns



def main():
    st.title("This is app for ecomm I am creating")
    st.sidebar.title("you can upload your file here")

    upload_file = st.sidebar.file_uploader("upload your file" type=['csv', 'excel'])

if __name__ == "__main__":
    main()