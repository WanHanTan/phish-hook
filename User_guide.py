import streamlit as st
from About import font_color

def show_userguide_page():
    yol = "HTML/container_background.html"
    f = open(yol, 'r')
    contents = f.read()
    f.close()
    contents = contents.replace('smth', 'User Guide')
    st.markdown(contents, unsafe_allow_html=True)
    # st.title("User Guide")
    #st.caption("Kindly refer the [user guide] for more detailed guidance to use this web app. ")

    font_color("Home")
    st.write("The **Home** page consists of a Random Forest malicious website classification model. You can input a URL into the textbox and click the _scan URL_ button to generate the result.")

    font_color("About")
    st.write("The **About** page shows an overview of Phish Hook. Find out more details about phishing websites to prevent them in future.")

    font_color("EDA")
    st.write("The **EDA** page shows various visualizations including word cloud, bar charts and histograms after exploring the dataset. The visualizations mainly shows the lexical features of phishing websites. These extracted features are categorized into _length-based, count-based, and binary_ features. ")

    font_color("Project")
    st.write("The **Project** page briefly explains the problem statements, objectives and the potential stakeholders/ target groups for Phish Hook. You can click into the GitHub link to access the data source and source code.")