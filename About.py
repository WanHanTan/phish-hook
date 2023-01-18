import streamlit as st
from PIL import Image


def show_about_page():
    with st.container():
        yol = "HTML/container_background.html"
        f = open(yol, 'r')
        contents = f.read()
        f.close()
        contents = contents.replace('smth', 'About Phish Hook')
        st.markdown(contents, unsafe_allow_html=True)
    
    font_color("Malicious websites are on the rise.")
    st.write("The COVID-19 pandemic has had a tremendous impact on organizations and people around the world, which has resulted in the widespread use of the Internet for working, shopping, and communicating. They are therefore vulnerable to a wide range of harmful Internet activities. Even though there are numerous methods for identifying suspicious Internet behaviors, many attackers still have access to breaking people's confidentiality. ")
    st.text(" ")
    st.write("Websites that contain content that allows attackers to take advantage of users are considered **:red[malicious]**. This includes websites that contain phishing URLs, spam URLs, malware scripts written in JavaScript, adware, and many others.")
        
   

    font_color("What is phishing?")
    col7, col8 = st.columns([4, 3])
    with col7:
        st.write("Phishing is one of the familiar attacks that trick users to access malicious content and gain their information. In terms of website interface and uniform resource locator (URL), most phishing webpages look identical to the actual webpages.Phishing is a fraudulent method that obtains client identity information and financial credentials via the use of technological and social tricks. Social networking platforms utilize spoof emails from legitimate organizations to let users access fake websites and disclose financial information such as usernames and passwords.")
        
    with col8:
        st.video('https://www.youtube.com/watch?v=XBkzBrXlle0')

        
    font_color("Common Phishing Techniques")
    st.markdown("""
    * Link manipulation to create a malicious URL that is displayed as if it were linking to a legitimate site or webpage.
    * Link shortening services like Bitly to hide link destination.
    * Homograph spoofing depends on URLs that were created using different characters to read exactly like a trusted domain.
    * Rendering all or part of a message as a graphical image sometimes enables attackers to bypass phishing defenses.
    * URL redirection is a vulnerability which allows an attacker to force users of your application to an untrusted external site. 
    """)
    
        
    font_color("How to Prevent Phishing")
    st.write("To help prevent phishing messages from reaching end users, experts recommend layering security controls, including:")
    col9, col10 = st.columns([4, 3])
    with col9:
        st.markdown("""
        * antivirus software;
        * both desktop and network firewalls;
        * web security gateway;
        * antiphishing toolbar in web browsers; and
        * phishing filters from vendors like Microsoft.
        """)
    
    with col10:
        st.image(Image.open("images/prevent-phishing.png"), use_column_width=True) 

        
def font_color(text):
    yol = "HTML/text_color.html"
    f = open(yol, 'r')
    contents = f.read()
    f.close()
    contents = contents.replace('smth', text)
    st.markdown(contents, unsafe_allow_html=True)