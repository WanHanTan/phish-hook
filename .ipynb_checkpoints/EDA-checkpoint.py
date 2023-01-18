import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize
from PIL import Image



def show_EDA_page():
    yol = "HTML/container_background.html"
    f = open(yol, 'r')
    contents = f.read()
    f.close()
    contents = contents.replace('smth', 'Exploratory Data Analysis')
    st.markdown(contents, unsafe_allow_html=True)
   
    
    st.write("###### Visualizations are created on distributions of each feature obtained of both malicious and benign URLs. This enable users to see the significance of each feature on classifying malicious URLs based on the aggregated url database.Furthermore, it's one of the ways to visualize feature importance.")
    st.write("""***""")
    
    st.subheader("1. Correlation between features")
    st.write("The correlation heatmap shows relationship between all lexical features.")
    correlation_heatmap()

    
    st.subheader("2. Length-based features")
    st.write("The following shows the distribution for length-based features: ")
    length_based_chart()
    length_result = "URL is a formatted text string utilized by internet users to recognize a network resource on the Internet. URL string consists of three elements such as network protocol, host name and path. For a given URL, the host name, first directory, top level domain and path are extracted and their respective lengths are examined. <br> <br> Usually, Phishers can use long URL to hide the doubtful part in the address bar."
    format3(length_result)
    
    st.subheader("3. Count-based features")
    st.write("The following shows the distribution for count-based features: ")
    count_based_chart()
    count_result = "1. Count of '-': Phishers have jumped on the little-used soft hyphen to fool URL filtering devices. <br> 2. Count of '@': Using “@” symbol in the URL leads the browser to ignore everything preceding the “@” symbol. <br> 3. Count of '?': Seeing more '?' in URL denotes a query string that contains the data to be passed to the server. <br> 4. Count of '%': Malicious websites generally contain more spaces in their URL hence more number of %. <br> 5. Count of '.': Each domain is separated by dot (.). Phishing websites generally use more than two sub-domains in the URL.<br> 6. Count of '=': Using '=' indicates passing of variable values from one form page to another which is risky. <br> 7. Count of http = Phishing websites have more than one HTTP in their URL whereas safe sites have only one HTTP. <br> 8. Count of https: Generally malicious URLs do not use HTTPS protocols as it generally requires user credentials and ensures that the website is safe for transactions. <br> 9. Count of www = Most malicious URLs has no or more than one www. <br> <br> Besides that, count for letters, digits and directories are calculated."
    format3(count_result)

    st.subheader("4. Binary features")
    st.write("The following shows the distribution for binary features: ")
    st.write("""*The URL is passed through a list. If there is matching patterns of being a malicious URL, result is labeled **-1** whereas **1** indicates that does not match the pattern.*""")
    binary_chart()
    binary_result = "1. Use of IP address: Generally cyber attackers use an IP address in place of the domain name to hide the identity of the website.his feature will check whether the URL has IP address or not. <br> 2. Use of URL shortening service: This feature is created to identify whether the URL uses URL shortening services like bit. \ly, goo.gl, go2l.ink, etc."
    format3(binary_result)
    
    
    st.subheader("5. Word cloud for malicious and benign URLs")
    st.write("The following shows the most common words found on **malicious** and **benign** URLs: ")
    word_cloud()

    
    
def correlation_heatmap():
    urldata = pd.read_csv("data/url_processed.csv")
    # droping "Unnamed: 0" as its unncessary feature
    urldata.drop("Unnamed: 0",axis=1,inplace=True)
    corr = urldata[['count.', 'count-', 'url_length', 'count@',
       'hostname_length', 'path_length', 'fd_length',
       'tld_length', 'count?', 'count%', 'count=', 
       'count_http', 'count_https', 'count_www', 'count_dir',
       'count_letters', 'count_digits', 'use_of_ip', 'short_url']].corr()

    fig1, ax1 = plt.subplots() 
    sns.heatmap(corr, xticklabels=corr.columns.values,
                       yticklabels=corr.columns.values)
    st.write(fig1)
    
def length_based_chart():
    urldata = pd.read_csv("data/url_processed.csv")
    # droping "Unnamed: 0" as its unncessary feature
    urldata.drop("Unnamed: 0",axis=1,inplace=True)
    colours = {'benign': 'green', 'malicious': 'red'} 
    hist_features = ["url_length","hostname_length","path_length","fd_length", "tld_length"]
    selected_hist =  st.selectbox('Select a length-based feature:', hist_features)
    index = hist_features.index(selected_hist)

    if selected_hist == "url_length":
        fig2, ax2 = plt.subplots()
        sns.histplot(data=urldata,x=hist_features[0],bins=100,hue='label', palette=colours)
        plt.xlabel(hist_features[0])
        plt.ylabel("Number Of URLs")
        plt.xlim(0,150)
        st.pyplot(fig2)
    
    if selected_hist == "hostname_length":
        fig3, ax3 = plt.subplots()
        sns.histplot(data=urldata,x=hist_features[1],bins=100,hue='label', palette=colours)
        plt.xlabel(hist_features[1])
        plt.ylabel("Number Of URLs")
        plt.xlim(0,50)
        st.pyplot(fig3)
        
    if selected_hist == "path_length":
        fig4, ax4 = plt.subplots()
        sns.histplot(data=urldata,x=hist_features[2],bins=100,hue='label', palette=colours)
        plt.xlabel(hist_features[2])
        plt.ylabel("Number Of URLs")
        plt.xlim(0,160)
        st.pyplot(fig4)

    if selected_hist == "fd_length":
        fig5, ax5 = plt.subplots()
        sns.histplot(data=urldata,x=hist_features[3],bins=100,hue='label', palette=colours)
        plt.xlabel(hist_features[3])
        plt.ylabel("Number Of URLs")
        plt.xlim(0,70)
        st.pyplot(fig5)
        
    if selected_hist == "tld_length":
        fig6, ax6 = plt.subplots()
        sns.histplot(data=urldata,x=hist_features[4],bins=100,hue='label', palette=colours)
        plt.xlabel(hist_features[4])
        plt.ylabel("Number Of URLs")
        plt.xlim(0,20)
        st.pyplot(fig6)
        
def count_based_chart():
    urldata = pd.read_csv("data/url_processed.csv")
    # droping "Unnamed: 0" as its unncessary feature
    urldata.drop("Unnamed: 0",axis=1,inplace=True) 
    count_features = ["count-","count@","count?","count%", "count.",
                     "count=", "count_letters", "count_digits", "count_dir", 
                     "count_http","count_https","count_www"]
    selected_count =  st.selectbox('Select a count-based feature:', count_features)
    index = count_features.index(selected_count)

    if selected_count == "count-":
        fig7, ax7 = plt.subplots()
        sns.countplot(x=count_features[0],data=urldata)
        plt.xlabel(count_features[0],)
        plt.ylabel("Number Of URLs")
        st.pyplot(fig7)
        
    if selected_count == "count@":
        fig8, ax8 = plt.subplots()
        sns.countplot(x=count_features[1],data=urldata)
        plt.xlabel(count_features[1],)
        plt.ylabel("Number Of URLs")
        st.pyplot(fig8)
        
    if selected_count == "count?":
        fig9, ax9 = plt.subplots()
        sns.countplot(x=count_features[2],data=urldata)
        plt.xlabel(count_features[2])
        plt.ylabel("Number Of URLs")
        st.pyplot(fig9)

    if selected_count == "count%":
        fig10, ax10 = plt.subplots()
        sns.countplot(x=count_features[3],data=urldata)
        plt.xlabel(count_features[3])
        plt.ylabel("Number Of URLs")
        st.pyplot(fig10)
        
    if selected_count == "count.":
        fig11, ax11 = plt.subplots()
        sns.countplot(x=count_features[4],data=urldata)
        plt.xlabel(count_features[4])
        plt.ylabel("Number Of URLs")
        st.pyplot(fig11)
        
    if selected_count == "count=":
        fig12, ax12 = plt.subplots()
        sns.countplot(x=count_features[5],data=urldata)
        plt.xlabel(count_features[5])
        plt.ylabel("Number Of URLs")
        st.pyplot(fig12)
        
    if selected_count == "count_letters":
        fig13, ax13 = plt.subplots()
        sns.countplot(x=count_features[6],data=urldata)
        plt.xlabel(count_features[6])
        plt.ylabel("Number Of URLs")
        st.pyplot(fig13)
        
    if selected_count == "count_digits":
        fig14, ax14 = plt.subplots()
        sns.countplot(x=count_features[7],data=urldata)
        plt.xlabel(count_features[7])
        plt.ylabel("Number Of URLs")
        st.pyplot(fig14)
        
    if selected_count == "count_dir":
        fig15, ax15 = plt.subplots()
        sns.countplot(x=count_features[8],data=urldata)
        plt.xlabel(count_features[8])
        plt.ylabel("Number Of URLs")
        st.pyplot(fig15)
        
    if selected_count == "count_http":
        fig16, ax16 = plt.subplots()
        sns.countplot(x=count_features[9],data=urldata)
        plt.xlabel(count_features[9])
        plt.ylabel("Number Of URLs")
        st.pyplot(fig16)
        
    if selected_count == "count_https":
        fig17, ax17 = plt.subplots()
        sns.countplot(x=count_features[10],data=urldata)
        plt.xlabel(count_features[10])
        plt.ylabel("Number Of URLs")
        st.pyplot(fig17)
        
    if selected_count == "count_www":
        fig18, ax18 = plt.subplots()
        sns.countplot(x=count_features[11],data=urldata)
        plt.xlabel(count_features[11])
        plt.ylabel("Number Of URLs")
        st.pyplot(fig18)

def binary_chart():
    urldata = pd.read_csv("data/url_processed.csv")
    # droping "Unnamed: 0" as its unncessary feature
    urldata.drop("Unnamed: 0",axis=1,inplace=True) 
    binary_features = ["use_of_ip","short_url"]
    selected_binary =  st.selectbox('Select a binary feature:', binary_features)
    index = binary_features.index(selected_binary)

    if selected_binary == "use_of_ip":
        fig19, ax19 = plt.subplots()
        sns.countplot(x="label", data=urldata,hue = binary_features[0], palette='YlOrRd')
        st.pyplot(fig19)
        
    if selected_binary == "short_url":
        fig20, ax20 = plt.subplots()
        sns.countplot(x="label", data=urldata,hue = binary_features[1], palette='viridis')
        st.pyplot(fig20)
        
def word_cloud():
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Malicious URLs:")
        malicious_img = Image.open("images/malicious-wordcloud.png")
        st.image(malicious_img, use_column_width=True)
        st.caption("Keywords: amp, php, phphttp, wp, index, etc.")
        
    with col2:
        st.write("Benign URLs:")
        benign_img = Image.open("images/benign-wordcloud.png")
        st.image(benign_img, use_column_width=True)
        st.caption("Keywords: https, htmlhtttps, org, wiki, wiki, etc.")
        
def format3(text):
    yol = "HTML/EDA_text.html"
    f = open(yol, 'r')
    contents = f.read()
    f.close()
    contents = contents.replace('smth', text)
    st.markdown(contents, unsafe_allow_html=True)