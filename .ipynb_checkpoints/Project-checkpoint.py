import streamlit as st
from PIL import Image
from About import font_color

def show_project_page():
    with st.container():
        yol = "HTML/container_background.html"
        f = open(yol, 'r')
        contents = f.read()
        f.close()
        contents = contents.replace('smth', 'Project')
        st.markdown(contents, unsafe_allow_html=True)
    st.write("Phish, as the word suggests, refers to phishing. While the second word “Hook” means to catch something with a hook.")
    st.write("With both words together, Phish Hook is an anti-phishing site that secures users against ongoing phishing attacks by checking whether a webpage is malicious.")

    # st.write("""### Problem Statement: """)
    font_color("Problem Statement")
    st.write("Phishing is a huge threat and growing more widespread every year. Because malicious websites can be flexible, **:red[conventional approaches frequently fail to detect new threats]**. Constantly following up on the up-to-date blacklists with new malicious websites is difficult. ")
    st.write("In comparison to most previous approaches, researchers focus on detecting malicious URLs from a massive list of URLs by a trusted source. The drawback of this method is that **:red[the blacklist used is non-exhaustive]**. Furthermore, with the large list of websites collected, the **:red[previous system's latency time will always increase]**, which can annoy the user.")
    st.write("These existing research works show that the performance of the phishing detection system is limited.")
    st.write("""***""")

    # st.write("""### Objective:""")
    font_color("Objective: ")
    st.write("1. To compare the existing approaches used for malicious website detection.")
    st.write("2. To apply Machine Learning techniques in analyzing real-time URLs and produce accurate results.")
    st.write("3. To present a dashboard for the users to identify malicious websites.")
    st.write("""***""")

    font_color("Target Users: ")
    st.write("##### 1. Industries and organizations")
    st.write("The most targeted industries are:")
    st.markdown("""
    * ecommerce
    * banking and money tranfer
    * social networking and email providers
    """)
    st.write("The reason for being the targeted industries is because scammers hoping to gain access to users’ accounts and/or gather enough information to steal identities and profit from it.")
    st.write("##### 2. General public")
    st.write("The general public especially those age between 18-25 are most susceptible to phishing attempts because of their low level of world experience.")
    st.write("Real-life cases of phishing show how any organization or individual can be a target and, unfortunately, a victim. Therefore, everyone should have the awareness to protect themselves. Technologies like **Phish Hook** can help users by catching and identifying the most common traits of phishing attempts, stopping malicious attachments, warning users about the dangers related to clicking on links.")
    st.write("""***""")

    # st.write("""### Data Source:""")
    font_color("Data Source: ")
    st.write("""##### Malicious and Benign URLs""")
    st.write("The dataset used is from the [Kaggle website](https://www.kaggle.com/datasets/siddharthkumar25/malicious-and-benign-urls).")
    data_img = Image.open("images/data-source-image.png")
    st.image(data_img, use_column_width=True)
    st.write("This dataset was acquired from various sources such as [PhishTank](https://phishtank.org/). This dataset consists of 345,000 legitimate and 104,000 malicious URLs. Each has been categorized with class labels ‘0’ for benign and ‘1’ for malicious.")
    st.write("""***""")

    col1, col2 = st.columns(2)
    with col1:
        # st.write("""### Source Code""")
        font_color("Source Code")
        st.write("The project source code can be obtained [here](https://github.com/WanHanTan/phish-hook)!")


    with col2:
        font_color("Presentation Link ")
        st.write("The presentation slides can be obtained [here](https://drive.google.com/file/d/1pmxJNSqogc2LzKshWHkz-SxKiUVCqq_I/view?usp=sharing)!")        
    st.write("""***""")
        
    # st.write("""### Developed by:""")
    font_color("Developed by ")
    st.write("[Wan Han](https://www.linkedin.com/in/wanhantan/)")
