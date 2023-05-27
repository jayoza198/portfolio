from pathlib import Path

import streamlit as st
from PIL import Image
import random
import plotly.express as px
import pandas as pd


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Jay Oza"
PAGE_ICON = ":wave:"
NAME = "Jay Oza"
DESCRIPTION = """
Passionate Computer Engineer and Data Scientist with expertise in Machine Learning. Kaggle Expert skilled in tackling complex data problems with innovative solutions.
"""
EMAIL = "jayoza198@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/jayoza2002",
    "GitHub": "https://github.com/jayoza198",
    "Twitter": "https://twitter.com/jayozaa",
    "Kaggle": "https://www.kaggle.com/jayoza198",
    "Blog": "https://jayoza.hashnode.dev/",
    
}
# PROJECTS = {
#     "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
#     "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
#     "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
#     "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
# }


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Qualifications")
st.write(
    """
- ✅ B.Tech in Computer Engineering - K.J. Somaiya Institute of Technology, Mumbai
- ✅ B.Sc in Data Science and Programming - Indian Institute of Technology, Madras
- ✅ Honors in Artificial Intelligence and Machine Learning - K.J. Somaiya Institute of Technology, Mumbai
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👨🏻‍💻 Programming: Python (Scikit-learn, Pandas, Numpy), SQL, HTML, CSS
- 📊 Data Visulization: Tableau, PowerBI, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, Decision Tree, Ensemble Learning
- 🗄️ Databases: Postgres, MySQL, SQlite
- 💾 Frameworks : Flask, Django
- ☁️ Deployment : Streamlit, Hugging Face, MLFlow
"""
)

# --- RADAR MAP ---
st.write('\n')
st.subheader("Skill Map")
st.write('---')

def radar_chart():
    df = pd.DataFrame(dict(
        r=[5, 3, 2, 2, 1, 3],
        theta=['Data Analysis', 'Machine Learning', 'Database Engineering',
               'Natural Language Processing', 'Computer Vision', 'Big Data Analysis']
    ))
    trace_data = pd.concat([df, df.iloc[[0]]], ignore_index=True)
    fig = px.line_polar(data_frame= trace_data, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')
    st.write(fig)

if __name__ == '__main__':
    radar_chart()




# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("👨🏻‍💻", "**NLP Engineering Intern | Omdena**")
st.write("05/2023 - Present")
st.write(
    """
- ► As a Machine Learning Engineer at Omdena, I collaborated with a global team to develop an NLP-based machine learning model that accurately identified and categorized disaster-related tweets.
- ► Using advanced techniques like sentiment analysis and LSTM models, we created a user-friendly web application to improve emergency response efforts
- ► My contributions included conducting data analysis, addressing data quality and bias issues, modelling and presenting findings to project head.
"""
)

# --- JOB 2
st.write("👨🏻‍💻", "**Business Developement & Management Intern | Max Conformance**")
st.write("03/2023 - Present")
st.write(
    """
- ► Proactively engaged in business development efforts as a Management Intern at Max Coformance, effectively reaching out to CISOs of diverse companies via LinkedIn and other platforms to promote the company's product.
- ► Collaborated closely with the CTO and CEO, leveraging their expertise and guidance to gain valuable insights into the operations and strategic decision-making processes of a SaaS startup.
- ► Demonstrated strong interpersonal skills and effective communication in building connections with CISOs, contributing to the expansion of Max Coformance's network and fostering potential business opportunities.
"""
)

# --- JOB 3
st.write('\n')
st.write("👨🏻‍💻", "**Data Science Intern | Omdena**")
st.write("04/2023 - 05/2023")
st.write(
    """
- ► As a Data Scientist at Omdena, I collaborated with a dynamic team to develop a personalized recommendation system for grocery shopping in Berlin that supports local businesses and reduces waste.
- ► By leveraging advanced data analysis techniques and machine learning algorithms, we created an innovative engine that provides consumers with informed purchasing decisions based on their individual preferences.
- ► Our groundbreaking solution has the potential to transform the grocery shopping experience in Berlin and beyond, while making a real-world impact.
"""
)

# --- JOB 4
st.write('\n')
st.write("👨🏻‍💻", "**Machine Learning Engineering Intern | Omdena**")
st.write("03/2023 - 04/2023")
st.write(
    """
- ► As a team member at Omdena, I collaborated with professionals from diverse backgrounds on a project aimed at mitigating air pollution by analyzing air quality patterns.
- ► My responsibilities included identifying predictors of air quality levels and using machine learning algorithms such as LSTM and DARTS to forecast air quality levels accurately.
- ► Through this experience, I developed my skills in data analysis and machine learning while gaining valuable experience in collaborating with a diverse team.
"""
)

# --- JOB 5
st.write('\n')
st.write("👨🏻‍💻", "**App Development Intern | PHJ Technologies**")
st.write("07/2022 - 08/2022")
st.write(
    """
- ► Working closely with subject matter experts to curate and review the company's educational content.
- ► Working on design, development and integration of the application product for the chemical engineering team and has become a valuable resource for practical education and training.
- ► It was incredibly rewarding to see the app being used by the employees helping to make a positive difference in the team's knowledge.
"""
)

# --- JOB 6
st.write('\n')
st.write("👨🏻‍💻", "**Data Analyst Intern | Devic Earth**")
st.write("01/2022 - 02/2022")
st.write(
    """
- ► As a data analyst intern at Devic Earth, I worked on a project that allowed me to make a tangible impact on the business.
- ► By providing clean and accurate data to our clients and Devic Earth which helped to improve decision-making and drive business results by providing solutions for their product efficiently.
"""
)

# --- Projects  ---
st.write('\n')
st.subheader("Projects")
st.write("---")

# --- Project 1
st.write("🖥️", "**Butler.ai**")
st.write(
    """
- ► Butler.ai is a one-stop solution for all your content-related needs. 
- ► Our advanced Q\&A prompt and video transcription service powered by Whisper AI can help you find answers and transcribe videos efficiently. 
- ► Additionally, our text summarization and paraphrasing tools can help you condense and rewrite long pieces of text with ease.
"""
)

# --- Project 2
st.write("🖥️", "**Movie Ticket Booking WebApp**")
st.write(
    """
- ► The movie ticket booking web app is a user-friendly platform built using Python, Flask, and Sqlite3. 
- ► It allows users to easily search and book tickets for their favourite movies, with the help of Jinja2 templates.
- ► Developed a mobile ticket booking application with extensive features for both admin and users, including user authentication, show management, booking system, and seamless user experience.
"""
)

# --- Project 3
st.write("🖥️", "**NFT Tweets Sentimental Analysis**")
st.write(
    """
- ► Developed a powerful Twitter scraper utilizing the Twitter API to extract real-time data based on keywords, hashtags, user handles, or geolocations. Ensured data integrity and scalability for collecting comprehensive tweets to build an up-to-date dataset.
- ► Employed sentiment analysis techniques using NLP and machine learning algorithms to determine the sentiment (positive, negative, or neutral) of NFT-related tweets. Generated valuable insights on public opinion, sentiment trends, and customer feedback.
- ► Implemented visualization and reporting features, presenting sentiment analysis results through intuitive visualizations like bar charts, word clouds, and sentiment distribution plots.Empowered data-driven decision-making and provided market insights.
"""
)


# --- Project 4
st.write("🖥️", "**Customer Analysis Dashboard - Tableau**")
st.write(
    """
- ► Developed a comprehensive dashboard in Tableau showcasing customer segmentation, providing valuable insights into customer behavior and preferences. 
- ► Analyzed revenue generated by each state, gender-based revenue distribution, and region-wise gross revenue, enabling data-driven decision making for targeted marketing strategies.
- ► Explored the correlation between quantity and discount, uncovering potential opportunities for optimizing pricing and promotions to maximize profitability.
"""
)

# --- Project 5
st.write("🖥️", "**Dhani.ai**")
st.write(
    """
- ► Dhani.ai is a cutting-edge finance content generation website that harnesses the power of OpenAI to provide users with personalized investment advice and market insights.  
- ► The website is built using the Python programming language, Flask web framework, and is hosted on Streamlit, a powerful platform for building and deploying machine learning applications.
- ► The app is deployed on Streamlit having seamless user experience powered by Cohere's api.
"""
)

# Certifications
st.write('\n')
st.subheader("Certification")
st.write("---")

# ---- Certification 1------
st.write("👨🏻‍🎓", "**Machine Learning Specialization - Standford University, Coursera**")
st.write(
    """
- ► Developed a strong foundation in fundamental machine learning algorithms, including linear regression, logistic regression, neural networks, and support vector machines. Proficient in implementing appropriate algorithms for diverse machine learning tasks.
- ► Experienced in data preprocessing, feature engineering, and utilizing popular machine learning tools and libraries such as Python, NumPy, pandas, and scikit-learn. Skilled in model evaluation, performance metrics, and making informed decisions for effective implementation.
"""
)

# ---- Certification 2------

st.write("👨🏻‍🎓", "**Open Source MLOps Platforms - Duke University, Coursera**")
st.write(
    """
- ► Acquired a comprehensive understanding of open-source platforms such as Hugging Face, MLflow, and Azure Cloud, gaining expertise in their implementation for effective MLOps (Machine Learning Operations) practices.
- ► Developed practical skills in utilizing these platforms for model deployment, version control, model tracking, and performance monitoring, enabling streamlined and efficient management of machine learning projects.
"""
)

# ---- Certification 3------

st.write("👨🏻‍🎓", "**Game Theory - Stanford University, Coursera**")
st.write(
    """
- ► Gained a comprehensive understanding of game theory principles and their applications in various fields, including economics, politics, and social sciences. Explored concepts such as strategic interactions, Nash equilibrium, bargaining, and mechanism design.
- ► Developed skills in analyzing complex decision-making scenarios, identifying optimal strategies, and predicting outcomes in competitive situations. Proficient in applying game theory frameworks to real-world scenarios for strategic decision-making and negotiation.
"""
)

# ---- Certification 4------
st.write("👨🏻‍🎓", "**AI Product Management Specialization - Duke University, Coursera**")
st.write(
    """
- ► Acquired a comprehensive understanding of the principles and practices of AI product management, including the ethical considerations, data strategies, and deployment techniques specific to AI-driven products.
- ► Developed skills in identifying market opportunities, defining product requirements, and leading cross-functional teams to successfully develop and launch AI-powered products, while ensuring alignment with business objectives and user needs.
"""
)
