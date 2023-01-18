import streamlit as st
from PIL import Image
import numpy as np
from tensorflow import keras
from Feature_Extraction import extract_features
import pickle
from selenium import webdriver
from time import sleep


def show_home_page():
    yol = "HTML/container_background.html"
    f = open(yol, 'r')
    contents = f.read()
    f.close()
    contents = contents.replace('smth', 'Phish Hook')
    st.markdown(contents, unsafe_allow_html=True)
    
    st.title("Real-time malicious URL detection")
    col5, col6 = st.columns([4,2])
    with col5:
        st.subheader("How Phish Hook works?")
        st.markdown("""
        * Extracts URL from the pasted text
        * Scans the URL to deetct any issues
        * Tells you whether it is **:red["High Risk"]** or **:orange["Minimal Risk"]**
        """)   
    
    with col6:
        st.image(Image.open("images/phishhook-logo.png"))
    
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("What does a **:orange[Minimal Risk URL]** mean?")
        st.write("**Minimal Risk** is one of the outcomes of Phish Hook. This means the URL doesn't contain any/ many malicious elements. Basically, it's a legit brand link and can't lead to a phishing site.")
        
    with col4:
        st.subheader("What does a **:red[High Risk URL]** mean?")
        st.write("**High Risk** is the second outcome of Phish Hook. This means the URL leads to a malicious website, and it's better to avoid clicking it.")

    st.write("***")
               
    col1, col2 = st.columns([3, 4])
    with col1:
        st.image("https://hailbytes.com/wp-content/uploads/2020/06/Email-Phishing-Attack.gif")
    
    with col2:
        st.subheader("**:Purple[Check if this website is secure.]**")
        input_url = st.text_input("Enter website address/ URL: (eg - https://www.youtube.com)"," ")
        clicked = st.button("Scan URL")

        # path to trained model
        model_path = 'C:/Users/Hannah Tan/OneDrive - Universiti Malaya/Y3S1/DS Project/Notebook_PhishHook/model/malicious_url_prediction.pkl'    
        #pickled_model = pickle.load(open('model/malicious_url_prediction.pkl', 'rb'))
    
        if clicked:
            prediction = get_prediction(input_url,model_path)
            #print(prediction)

#Return probability value
def get_prediction(url, model_path):
    print("Loading the model...")
    model = pickle.load(open(model_path, 'rb'))
    
    print("Extracting features from URL...")
    url_features = extract_features(url)
    print(url_features)

    print("Making prediction...")
    prediction = model.predict_proba([url_features])

    i = prediction

    i = prediction[0][1]
    
    if i == 1.0:
        result_str = "This website has HIGH RISK to be malicious!" 
        format1(result_str)
        
    else:
        result_str = "This website has MINIMAL RISK to be malicious."
        format2(result_str)
    
def format1(text):
    yol = "HTML/result_text_1.html"
    f = open(yol, 'r')
    contents = f.read()
    f.close()
    contents = contents.replace('smth', text)
    st.markdown(contents, unsafe_allow_html=True)
    
def format2(text):
    yol = "HTML/result_text_2.html"
    f = open(yol, 'r')
    contents = f.read()
    f.close()
    contents = contents.replace('smth', text)
    st.markdown(contents, unsafe_allow_html=True)
    
    



    
    