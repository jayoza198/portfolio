from pathlib import Path

import streamlit as st
from PIL import Image
import random
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


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
- ✅ B.S in Data Science and Applications - Indian Institute of Technology, Madras
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
- ☁️ Deployment : AWS, GCP, Streamlit, Hugging Face, MLFlow
"""
)

# --- RADAR MAP ---
st.write('\n')
st.subheader("Skill Map")
st.write('---')

def radar_chart():
    categories = ['Data Analysis', 'Machine Learning', 'Database Engineering',
                'Natural Language Processing', 'Computer Vision', 'Big Data Analysis', 'AWS']
    values = [5, 4, 4, 3, 3, 3, 3]

    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True),
        ),
        showlegend=False
    )

    st.plotly_chart(fig)

if __name__ == '__main__':
    radar_chart()

    
# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 
st.write("👨🏻‍💻", "**Risk Analyst | Deloitte.**")
st.write("07/2024 - Present")
st.write(
    """
"""
)


# --- JOB 
st.write("👨🏻‍💻", "**Data Science Intern | YOLOH INC.**")
st.write("08/2023 - 07/2024")
st.write(
    """
- ► Innovating a technological fusion that leverages OCR, harnessing the capabilities of Llama 2, GPT-3.5, and GPT-4 models.
- ► Synergizing the potential of Neo4j graph database with the scalability of AWS resources, achieving a 30% reduction in manual data entry and optimizing data retrieval efficiency by an outstanding 53%.
"""
)

# --- JOB 
st.write("📈", "**Quant Research Consultant | WorldQuant Brain**")
st.write("10/2023 - 05/2024")
st.write(
    """
- ► Conducted dynamic market analysis and formulated strategic equations, contributing to enhanced market efficiency as a Quant Research Consultant at WorldQuant Brain.
- ► Specialized in crafting visionary mathematical models, significantly improving precision and introducing innovative approaches to market strategies.
- ► Demonstrated a proven track record in rigorous backtesting, ensuring adaptability and long-term success of strategies in various market scenarios as a Quant Research Consultant.
"""
)


# --- JOB 
st.write("👨🏻‍💻", "**Data Science Intern | Nutriva Lifescience Ltd**")
st.write("06/2023 - 06/2023")
st.write(
    """
- ► Developed and deployed an end-to-end healthcare data analysis web-app using Streamlit and Python, handling over 1 GB of data. Leveraged data science techniques to extract valuable insights and trends from large datasets. Implemented interactive visualizations which ensured data accuracy and reliability. Received positive feedback from team leaders and the CEO.
- ► Led the architecture and development of a centralized healthcare product database for Nutriva Lifesciences Pvt Ltd. Designed a scalable schema for efficient querying and data management of healthcare products.
- ► Streamlined inventory management through data linking with merchants. Utilized advanced data modelling techniques to ensure data integrity and optimize database performance. Integrated the database seamlessly with existing systems
"""
)


# --- JOB 
st.write("👨🏻‍💻", "**Machine Learning Intern | Omdena**")
st.write("06/2023 - 07/2023")
st.write(
    """
- ► Developed and executed a finance project with the help of Benin’s banking dataset, achieving a significant increase in credit score analysis accuracy from 56% to 83% through the application of machine learning. Collaborated with Omdena, utilizing ensemble learning algorithms (XGBoost, Random Forest) and SVM. 
- ► Ensured fairness, incorporated domain knowledge, and optimized the data pipeline for enhanced efficiency.
- ► Spearheaded critical finance project, achieving remarkable 83% accuracy (48% increase) in credit score analysis. Leveraged ensemble learning (XGBoost, Random Forest) and SVM. Ensured fairness, incorporated domain knowledge, optimized data pipeline, and conducted rigorous testing for reliable loan classification model.
"""
)

# --- JOB 
st.write("👨🏻‍💻", "**NLP Engineering Intern | Omdena**")
st.write("05/2023 - 06/2023")
st.write(
    """
- ► As a Machine Learning Engineer at Omdena, I collaborated with a global team to develop an NLP-based machine learning model that accurately identified and categorized disaster-related tweets.
- ► Using advanced techniques like sentiment analysis and LSTM models, we created a user-friendly web application to improve emergency response efforts
- ► My contributions included conducting data analysis, addressing data quality and bias issues, modelling and presenting findings to project head.
"""
)

# --- JOB 
st.write("👨🏻‍💻", "**Business Developement & Management Intern | Max Conformance**")
st.write("03/2023 - 06/2023")
st.write(
    """
- ► Proactively engaged in business development efforts as a Management Intern at Max Coformance, effectively reaching out to CISOs of diverse companies via LinkedIn and other platforms to promote the company's product.
- ► Collaborated closely with the CTO and CEO, leveraging their expertise and guidance to gain valuable insights into the operations and strategic decision-making processes of a SaaS startup.
- ► Demonstrated strong interpersonal skills and effective communication in building connections with CISOs, contributing to the expansion of Max Coformance's network and fostering potential business opportunities.
"""
)

# --- JOB 
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

# --- JOB 
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

# --- JOB 
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

# --- JOB 
st.write('\n')
st.write("👨🏻‍💻", "**Data Analyst Intern | Devic Earth**")
st.write("01/2022 - 02/2022")
st.write(
    """
- ► As a data analyst intern at Devic Earth, I worked on a project that allowed me to make a tangible impact on the business.
- ► By providing clean and accurate data to our clients and Devic Earth which helped to improve decision-making and drive business results by providing solutions for their product efficiently.
"""
)

# Publications
st.write('\n')
st.subheader("Publications")
st.write("---")

# ---- Publication------
st.write("📝", "**The DeepFake Dilemma: Balancing Innovation, Ethics, and Accountability Through Law**")

# ---- Publication------
st.markdown(
    "📝 [**Pixels to Phrases: Evolution of Vision Language Models**](https://www.researchgate.net/publication/381037796_Pixels_to_Phrases_Evolution_of_Vision_Language_Models)",
    unsafe_allow_html=True,
)

# ---- Publication------
st.markdown(
    "📝 [**Metrics to Meaning: Enabling Human-Interpretable Language Model Assessment**](https://openreview.net/forum?id=DiAazbnedy&referrer=%5Bthe%20profile%20of%20Jay%20Oza%5D(%2Fprofile%3Fid%3D~Jay_Oza1))",
    unsafe_allow_html=True,
)

# ---- Publication------
st.markdown(
    "📝 [**Harnessing Insights from Streams: Unlocking Real-Time Data Flow with Docker and Cassandra in the Apache Ecosystem**](https://www.researchgate.net/publication/377066874_Harnessing_Insights_from_Streams_Unlocking_Real-Time_Data_Flow_with_Docker_and_Cassandra_in_the_Apache_Ecosystem)",
    unsafe_allow_html=True,
)

# ---- Publication------
st.markdown(
    "📝 [**MelSpectroNet: Enhancing Voice Authentication Security with AI-based Siamese Model and Noise Reduction for Seamless User Experience**](https://www.researchgate.net/publication/376540209_MelSpectroNet_Enhancing_Voice_Authentication_Security_with_AI-based_Siamese_Model_and_Noise_Reduction_for_Seamless_User_Experience)",
    unsafe_allow_html=True,
)

# ---- Publication------
st.markdown(
    "📝 [**Enhancing Question Prediction with Flan T5 -A Context-Aware Language Model Approach**](https://www.authorea.com/users/706759/articles/693477-enhancing-question-prediction-with-flan-t5-a-context-aware-language-model-approach)",
    unsafe_allow_html=True,
)

# ---- Publication------
st.markdown(
    "📝 [**A Streamlined Approach towards Monkeypox Detection**](https://www.researchgate.net/publication/376201851_A_Streamlined_Approach_towards_Monkeypox_Detection)",
    unsafe_allow_html=True,
)

# ---- Publication------
st.markdown(
    "📝 [**Toxic Comment Detection Using Bidirectional Sequence Classifiers**](https://ieeexplore.ieee.org/document/10467922)",
    unsafe_allow_html=True,
)



# --- Projects  ---
st.write('\n')
st.subheader("Projects")
st.write("---")

# --- Project 
st.write("🖥️", "**Portfolio Optimization Using Markowitz Model**")
st.write(
    """
- ► Executed Portfolio Optimization using the Markowitz Model for VOO (NYSE) and BLV (NYSE) initially within Google Sheets. 
- ► Developed an Efficient Frontier and Mean-Standard Deviation Plot to gain a comprehensive insight into the stock movements.
"""
)

# --- Project 
st.write("🖥️", "**Real-Time Data Flow with Docker and Cassandra in the Apache Ecosystem**")
st.write(
    """
- ► Engineered a real-time big data pipeline with Kafka, Spark, and Cassandra on Docker, achieving a 95% data ingestion success rate, sub-100ms latency, and a highly scalable, fault-tolerant architecture. 
- ► Utilized Docker for rapid deployment and implemented a CI/CD pipeline for efficient feature rollouts.
- ► Analyzed and optimized pipeline performance, processing 1000+ records/sec with 96% accuracy using custom API and Kaggle dataset streams. 
- ► Ingested diverse data types, conducted rigorous testing for data integrity, and monitored key metrics to validate linear scalability under varying loads.
"""
)

# --- Project 
st.write("🖥️", "**Monkey Pox Detection Using Custom CNN Model**")
st.write(
    """
- ► Developed of a project, "Monkeypox Detection through image detection," employing a custom Convolutional Neural Network (CNN) model boasting a formidable architecture of 14 layers.
- ► This groundbreaking initiative was fortified with a robust dataset exceeding 6GB, meticulously curated for precision and diversity.
"""
)

# --- Project 
st.write("🖥️", "**CourseCompass: A Learning-Path Recommendation System**")
st.write(
    """
- ► Led the development of "CourseCompass: A Learning-Path Recommendation System" at IIT Madras as part of the Software Engineering Course curriculum, targeting first and second-year students.
- ► Orchestrated the design and implementation of the frontend using HTML, CSS, and Vue.js, while employing Python for the backend & Machine Learning and SQLite for the database
- ►  Executed the project using the Agile methodology for efficient and iterative progress.
"""
)

# --- Project 
st.write("🖥️", "**Fine Tuning BERT for Text Classification**")
st.write(
    """
- ► Fine-tuned BERT, a pre-trained language model, to classify text for detecting insincere questions. 
- ► Built tf.data pipelines to feed data to the network and customized the model architecture by adding classifier layers.
- ► Achieved over 96% validation accuracy after 100 epochs of training on Quora dataset with binary cross-entropy loss and Adam optimizer. 
- ► The project enhanced my skills in leveraging transfer learning and fine-tuning large pre-trained NLP models for downstream tasks
"""
)

# --- Project 
st.write("🖥️", "**Butler.ai**")
st.write(
    """
- ► Butler.ai is a one-stop solution for all your content-related needs. 
- ► Our advanced Q\&A prompt and video transcription service powered by Whisper AI can help you find answers and transcribe videos efficiently. 
- ► Additionally, our text summarization and paraphrasing tools can help you condense and rewrite long pieces of text with ease.
"""
)

# --- Project 
st.write("🖥️", "**Movie Ticket Booking WebApp**")
st.write(
    """
- ► The movie ticket booking web app is a user-friendly platform built using Python, Flask, and Sqlite3. 
- ► It allows users to easily search and book tickets for their favourite movies, with the help of Jinja2 templates.
- ► Developed a mobile ticket booking application with extensive features for both admin and users, including user authentication, show management, booking system, and seamless user experience.
"""
)

# --- Project 
st.write("🖥️", "**NFT Tweets Sentimental Analysis**")
st.write(
    """
- ► Developed a powerful Twitter scraper utilizing the Twitter API to extract real-time data based on keywords, hashtags, user handles, or geolocations. Ensured data integrity and scalability for collecting comprehensive tweets to build an up-to-date dataset.
- ► Employed sentiment analysis techniques using NLP and machine learning algorithms to determine the sentiment (positive, negative, or neutral) of NFT-related tweets. Generated valuable insights on public opinion, sentiment trends, and customer feedback.
- ► Implemented visualization and reporting features, presenting sentiment analysis results through intuitive visualizations like bar charts, word clouds, and sentiment distribution plots.Empowered data-driven decision-making and provided market insights.
"""
)


# --- Project 
st.write("🖥️", "**Customer Analysis Dashboard - Tableau**")
st.write(
    """
- ► Developed a comprehensive dashboard in Tableau showcasing customer segmentation, providing valuable insights into customer behavior and preferences. 
- ► Analyzed revenue generated by each state, gender-based revenue distribution, and region-wise gross revenue, enabling data-driven decision making for targeted marketing strategies.
- ► Explored the correlation between quantity and discount, uncovering potential opportunities for optimizing pricing and promotions to maximize profitability.
"""
)

# --- Project 
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
