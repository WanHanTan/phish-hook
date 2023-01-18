import streamlit as st

from Home import show_home_page
from About import show_about_page
from User_guide import show_userguide_page
from EDA import show_EDA_page
from Project import show_project_page

st.sidebar.title("Navigate to...")
navigator = st.sidebar.radio("", ("Home", "About", "Exploratory Data Analysis","User Guide", "Project"))

st.markdown(
    """ 
    <style>
    .main{ 
    background-color: #F5F5F5;
    } 
    </style> 
    """,
    unsafe_allow_html=True )

if navigator == "Home":
    show_home_page()
if navigator == "About":
    show_about_page()
if navigator == "Exploratory Data Analysis":
    show_EDA_page()
if navigator == "User Guide":
    show_userguide_page()
if navigator == "Project":
    show_project_page()

    
