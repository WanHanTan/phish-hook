# phish-hook
 Phishing URLs detection using Machine Learning

## Presentation Slides
Link: https://drive.google.com/file/d/1gQcY2FraO4Z0v_IHS9BkQqcmSuMwu-vw/view?usp=sharing

# Data Science Project Documentation
### Introduction
Link to App: https://phish-hook-malicious-url-detection.streamlit.app/

**Phishing** is one of the familiar attacks that trick users to access malicious content and gain their information. It is a fraudulent method that obtains client identity information and financial credentials via the use of technological and social tricks. In terms of website interface and uniform resource locator (URL), most phishing webpages look identical to the actual webpages. Social networking platforms utilize spoof emails from legitimate organizations to let users access fake websites and disclose financial information such as usernames and passwords. 

Consequently, to produce more accurate results, a phishing website detection application is created to serve as middleware between users and harmful websites.

### How Phish Hook works?
Phish Hook is an anti-phishing site that secures users against ongoing phishing attacks by checking whether a webpage is malicious.
1. Extract URL from user's pasted text.
2. Scans the URL to detect any issues.
3. Shows whether the URL is "HIGH RISK" or "MINIMAL RISK".

The pictures below show the homepage of Phish Hook, Users can enter or paste any URL into a text field. The backend of Phish Hook will analyze the URL to classify whether the website is malicious.

![](https://github.com/WanHanTan/phish-hook/blob/main/images/output1.png?raw=true)
+ **MINIMAL RISK** is one of the outcomes of Phish Hook. This indicated that the entered URL doesn't contain any/ many malicious contents. Basically, it is a legit brand link and won't lead to a phishing site.

![](https://github.com/WanHanTan/phish-hook/blob/main/images/output2.png?raw=true)
+ **HIGH RISK** indicates that the URL leads to a malicious phishing website, and users are encouraged to avoid clicking it.

