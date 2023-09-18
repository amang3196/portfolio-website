from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Aman_Garg_Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Aman Garg"
PAGE_ICON = ":wave:"
NAME = "Aman Garg"
DESCRIPTION = """
I am a MBA graduate specializing in Data Sciences and Data Analytics. Possessing this degree showcases my interest and skills in Data Science and Data Analytics along with how it can be leveraged into developing businesses. Data Science is a vast field and one of the subject I am most interested in is Machine Learning and its capabilities to solve real-world problems. I majorly use Python for learning and developing and have understanding of R and SQL. Some of the tools that I have had my hands-on include Tableau, PowerBI, and MongoDB. I am also interested in researching the applications of ML in brain-computer interface.
"""
EMAIL = "amangarg3196@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com"
}
PROJECTS = {
    "🏆 Customer Segmentation - Identifying segments of customers to build marketing stratgies.": "github link",
    "🏆 Movie Recommeder System - Content based recommender system deployed using streamlit cloud": "https://content-based-movie-recommender-system.streamlit.app/",
    "🏆 US Police Shootings Analysis - Detailed trends and analysis on US Police Shootings": "github link",
    "🏆 Twitter Sentiment Analysis - Analysing sentiment based around #Apple": "github link",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    #st.write("📫", EMAIL)


# # --- SOCIAL LINKS ---
# st.write('\n')
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")

col1 , col2, col3 = st.columns([1,2,1],gap='large')
with col1:
    st.write(f"[{'LinkedIn'}]({'https://www.linkedin.com/in/aman-garg-b2ba4a120/'})")

with col2:
    st.write(EMAIL)
    
with col3:
    st.write(f"[{'GitHub'}]({'https://github.com/amang3196'})")

# # --- EXPERIENCE & QUALIFICATIONS ---
# st.write('\n')
# st.subheader("Experience & Qulifications")
# st.write(
#     """
# - ✔️ 7 Years expereince extracting actionable insights from data
# - ✔️ Strong hands on experience and knowledge in Python and Excel
# - ✔️ Good understanding of statistical principles and their respective applications
# - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
# """
# )

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Intern - Data Science/AI | Aethereus Consulting**")
st.write("05/2023 - 08/2023")
st.write(
    """
- ► Built requirements for AI based solution for route optimization for field sales reps

- ► Built a connection to source data from Salesforce CDP into AWS
- ► Developed a pipeline to build and deploy ML model using Amazon Sagemaker
- ► Developed a VR Gallery using Unity and Oculus Quest 2 to market the companies products
- ► Tools: Python, Amazon S3, Amazon Sagemaker, Amazon API Gateway, AWS Lambda, Unity

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Science Intern | Alpha AI**")
st.write("04/2022 - 07/2022")
st.write(
    """
- ► Research and experiment with pre built AI models to solve existing business problems

- ► Built an AI generated animation with first order head motion, audio-video lip syncing algorithms
- ► Developed a streamlit API to combine first order head motion and lip syncing
- ► Containerize the streamlit API using Docker
- ► Parallelize machine learning model inference in order to serve multiple users
- ► Collaborate with other teams as an additional resource
- ► Tools: Generative AI, PyTorch, Tensorflow OpenCV, Streamlit, Docker, Blender, Omniverse.

"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**AI Intern | Vitesco Technology**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Collaborate with a team of domain experts to understand the business problem and provide bridge between
domain knowledge and Artificial Intelligence.

- ► Built a neural network to predict the value of axle torque in order to develop a digital twin.
- ► Tools: Pycharm, Python, Pandas, Keras, Numpy, asammdf.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming : Python, Pandas, Numpy, Scikit-learn, Tensorflow, PyTorch
- 🕸️ Web Frameworks : Flask, Streamlit
- 📈 Data Visulization : PowerBI, Plotly, Seaborn, Matplotlib
- 🗄️ Databases : MongoDB, MySQL
- 🤖 Machine Learning : Linear Regression, Decision Trees, Random Forrest, Clustering
"""
)

skills = {
    'Programming/Frameworks': 'Python, Pandas, Numpy, Scikit-learn, Tensorflow, PyTorch',
    'Web Frameworks' : 'Flask, Streamlit',
    'Data Visulization': 'PowerBI, Plotly, Seaborn, Matplotlib',
    'Machine Learning' : 'Linear Regression, Decision Trees, Random Forrest, Clustering',
    'Databases': 'MongoDB, MySQL'
}



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
