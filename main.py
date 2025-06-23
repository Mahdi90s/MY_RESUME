import requests
import streamlit as st
from pathlib import Path
from PIL import Image
from streamlit_lottie import st_lottie
import os


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir /"styles" /"main.css"
resume_file = current_dir /"assets" /"Mirmahdi Mirhashemi CV.pdf"
coverlatter_file = current_dir /"assets" /"Mirmahdi Mirhashemi Cover Latter.pdf"
profile_pic = current_dir /"assets" /"2189.png"
QUALIFICATIONS_i = current_dir /"assets" /"CertificateOfCompletion_Python Essential Training_page-0001.png"
QUALIFICATIONS_ii = current_dir /"assets" /"CertificateOfCompletion_Learning Python_page-0001.png"
QUALIFICATIONS_iii = current_dir /"assets" /"CertificateOfCompletion_Python for Data Science and Machine Learning Essential Training Part 1_page-0001.png"
QUALIFICATIONS_iv = current_dir /"assets" /"CertificateOfCompletion_Python for Data Science and Machine Learning Essential Training Part 2_page-0001.png"
QUALIFICATIONS_v =  current_dir /"assets" /"CertificateOfCompletion_Python for Data Science Essential Training Part 1_page-0001.png"
QUALIFICATIONS_vi = current_dir /"assets" /"CertificateOfCompletion_Python for Data Science Essential Training Part 2 _page-0001.png"
QUALIFICATIONS_vii = current_dir /"assets" /"CertificateOfCompletion_Python for NonProgrammers-1.png"
QUALIFICATIONS_viii = current_dir /"assets" /"CertificateOfCompletion_Using Large Datasets with pandas-1.png"
QUALIFICATIONS_XIV = current_dir /"assets" /"CertificateOfCompletion_Advanced Power BI DAX Language Formulas and Calculations-1.png"
QUALIFICATIONS_XV = current_dir /"assets" /"CertificateOfCompletion_Statistics Foundations 1 The Basics_page-0001.png"



# --- GENERAL SETTINGS ---
Page_TITLE = "My Portfolio"
PAGE_ICON = "🌐"
NAME = "Hi, my name is Matt 👋🏼"
TITLE = "Transforming Data into Decisions: A Data Scientist's Story"
DESCRIPTION = "Data is the canvas, and analytics is my brush. This portfolio is a reflection of my journey—a blend of creativity, science, and problem-solving to transform data into impactful solutions."
EMAIL = "mirhashemim7@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/mirmahdi-mirhashemi",
    "GitHub": "https://github.com/Mahdi90s",
}

# PROJECT = {
#     "A": "--",
#     "B": "--"
    
# }

st.set_page_config (page_title=Page_TITLE, page_icon=PAGE_ICON, layout='wide', initial_sidebar_state='expanded')




def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://lottie.host/291c3c67-ed2d-48db-abb6-f5b86cef2d07/hl1SzeIeW3.json")


# --- LOAD CSS, PDF $ PROFILE PIC ---
with open (css_file) as f:
    st.markdown("<style>{}</style>". format(f.read()), unsafe_allow_html=True)
    
with open (resume_file, "rb") as pdf_c_file:
    PDFCbyte = pdf_c_file.read()
    
with open (coverlatter_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns([1, 6])
with col1:
    st.image (profile_pic, width=230)



    
with col2:
    st.subheader (NAME)
    st.title (TITLE)
    st.write (DESCRIPTION)
    st.download_button(
        label= "📃 Dowload Resume",
        data=PDFCbyte,
        file_name=coverlatter_file.name,
        mime="application/octet-stream",
    )
    st.download_button(
        label= "📃 Dowload Cover_Latter",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("✉️", EMAIL)
    
     # --- SOCIAL LINKS ---

    # Icon URLs
    icon_urls = {
        "LinkedIn": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
        "GitHub": "https://cdn-icons-png.flaticon.com/512/733/733553.png",  
    }

    # Generate HTML for icons
    items = " ".join(
        f'<a href="{link}" target="_blank" style="text-decoration: none; margin-right: 15px;">'
        f'<img src="{icon_urls[platform]}" alt="{platform}" style="width:24px; height:24px;">'
        f'</a>'
        for platform, link in SOCIAL_MEDIA.items()
    )

    # Render icons in Streamlit
    st.markdown(items, unsafe_allow_html=True)

with st.container():
    st.write("---", )
    left_column, right_column = st.columns(2)
    with left_column:
        st.header ("What I do")
        st.write ("""
                    I specialize in turning complex data into actionable insights that drive `decision-making` and innovation. As a `Data Science` Master's student with a strong background in financial analysis, I bring a unique blend of analytical skills and technical expertise to every project. I work with programming languages like `Python` and `R` to build predictive models, `SQL` to manage and query large datasets, and tools like `Power BI` to create compelling `data visualizations`. My focus areas include:

                    - ✔️ Developing `machine learning` models for financial forecasting and optimization.
                    - ✔️ Crafting `interactive dashboards` to visualize performance metrics and trends.
                    - ✔️ Applying data science techniques to solve real-world problems in healthcare, finance, and beyond.

                    I thrive on collaboration and delivering results that make a measurable impact, whether it's optimizing business operations, improving sales performance, or advancing innovation in the biopharmaceutical space.
                """)
                
        # --- EXPERIENCE & QUALIFICATIONS ---
    st.write ("#")
    st.subheader ("Experience & Qulifications")

    # --- skills ---
    st.write ("#")
    st.subheader ("My Expertise")
    st.write (
        """
    - 🟢	**Data Analysis Tools:** `Excel` , `Power BI` , `RStudio` , `VSCode`
    - 🟢	**Programming:**         `SQL` , `Python` , `DAX` , `R`, `MATLAB`
    - 🟢	**Analytical Skills:**   `Data Governance` , `Trend Analysis` , `Forecasting` , `Variance Analysis`
    - 🟢	**Dashboard Creation:**  `Financial Dashboards Highlighting Key Performance Indicators`
    - 🟢	**Technical Skills:**    `Data visualization` , `Data Modelling` , `Data Preprocessing` , `Data Governance` 

    """
    )



    # --- WORK HISTORY ---
    st.write ("#")
    st.subheader ("Work History")
    st.write ("---")

    # --- JOB 1
    st.write ("***Data Engineer / Data Analyst*** - EmadAra (Tehran)")
    st.write ("September 2023 - October 2024", "(`1 Yr, 1 Mo`)")
    st.write (
        """
    - ✅	Analysed financial performance and provided insights to improve `decision-making` processes.
    - ✅	Developed interactive dashboards using Power BI to track key financial metrics.
    - ✅	Assisted in budgeting, forecasting, and variance analysis.
    - ✅	Preprocesses raw data from SQL and created tables, applying `analytical thinking` to design and develop insightful dashboards.
    - ✅	Solved complex challenges by designing and implementing a streamlined sales and return process, resulting in a `30%` increase in sales.


    """
    )
    st.write ("##")

    # --- JOB 2
    st.write ("***Senior Sale Operations Specialist*** - RayaPakhsh (Tehran)")
    st.write ("May 2022 - August 2023", "(`1 Yr, 3 Mos`)")
    st.write (
        """
    - ✅	Controlled financial documents and created vital reports in `Excel` and `Power BI`.
    - ✅	Built and streamlined the selling process for improved accuracy.
    - ✅	Calculated employee salaries and monitored monthly cash flows in Excel with meticulous `attention to detail`, optimizing the payment process and making it `20%` faster.
    - ✅	Monitored the profit and loss gaps to ensure financial stability.
    - ✅	Managed and controlled the company's financial software system.
    - ✅	Trained new employees on financial processes and software systems, leveraging `strong influencing`. skills to ensure effective knowledge transfer and team alignment.

    """
    )
    st.write ("##")

    # --- JOB 3
    st.write ("***Software Engineer | Financial Analyst*** - HamrahanSystemGohar (Tehran)")
    st.write ("April 2018 - April 2022", "(`4 Yrs`)")
    st.write (
        """
    - ✅	Demonstrated strong `organizational skills` by managing financial software implementations for customers, resulting in a `13%` increase in customer satisfaction.
    - ✅	Delivered financial services and resolved customer issues related to software and accounting.
    - ✅	`Enhanced reporting` functionalities in the company's financial software.
    - ✅	Developed custom `financial reports` using `Excel` and `Power BI` for improved `decision-making`.
    - ✅	Conducted detailed financial analysis and `data interpretation` to support strategic business planning, streamlining the process to reduce completion time by `one week`.
    - ✅	Developed and maintained `financial models` for `budgeting` and `forecasting`.
    - ✅	Collaborated with senior management to provide key financial insights.

    """
    )

    # --- QULIFICATIONS ---
    st.write ("#")
    st.subheader ("Qulifications")
    st.write ("---")


    with st.container():
        a_col, b_col, c_col, d_col, e_col = st.columns(5)
        with a_col:
                    QUALIFICATIONS_i = Image.open(QUALIFICATIONS_i)
                    st.image(QUALIFICATIONS_i, caption="Python Essential Training", use_container_width=True)
                        
                    QUALIFICATIONS_ii = Image.open(QUALIFICATIONS_ii)
                    st.image(QUALIFICATIONS_ii, caption="Learning Python", use_container_width=True) 
                
                    QUALIFICATIONS_iii = Image.open(QUALIFICATIONS_iii)
                    st.image(QUALIFICATIONS_iii, caption="Python for Data Science and Machine Learning Essential Training P1", use_container_width=True) 
                    
                    QUALIFICATIONS_iv = Image.open(QUALIFICATIONS_iv)
                    st.image(QUALIFICATIONS_iv, caption="Python for Data Science and Machine Learning Essential Training P2", use_container_width=True) 
                    
                    QUALIFICATIONS_XIV = Image.open(QUALIFICATIONS_XIV)
                    st.image(QUALIFICATIONS_XIV, caption="Advanced Power BI DAX Language Formulas and Calculations", use_container_width=True) 

        with c_col:
                    QUALIFICATIONS_v = Image.open(QUALIFICATIONS_v)
                    st.image(QUALIFICATIONS_v, caption="Python for Data Science Essential Training P1", use_container_width=True) 

                    QUALIFICATIONS_vi = Image.open(QUALIFICATIONS_vi)
                    st.image(QUALIFICATIONS_vi, caption="Python for Data Science Essential Training P2", use_container_width=True) 

                    QUALIFICATIONS_vii = Image.open(QUALIFICATIONS_vii)
                    st.image(QUALIFICATIONS_vii, caption="Python for NonProgrammers", use_container_width=True) 
                
                    QUALIFICATIONS_viii = Image.open(QUALIFICATIONS_viii)
                    st.image(QUALIFICATIONS_viii, caption="Using Large Datasets with pandas", use_container_width=True)
                    
                    QUALIFICATIONS_XV = Image.open(QUALIFICATIONS_XV)
                    st.image(QUALIFICATIONS_XV, caption="Statistics Foundations 1 The Basics", use_container_width=True)
                    
                    
                    
                         
    # --- Projects & Accomplishments --- 
    # st.write ("#")
    # st.subheader ("Projects & Accomplishments")
    # st.write("---")
       
    # for project, link in PROJECT.items():
    #     st.write(f"[{project}]({link})")
     
     
     # --- EDUCATION HISTORY ---
    st.write ("#")
    st.subheader ("Where I've Studied")
    st.write ("---")

    # --- POSTGRADUCATE
    st.write ("**University of Essex - MSc. Data Science**")
    st.write ("October 2024 - October 2025")
    st.write ("GPA: ")
    st.write (
        """
    - ❇️ In the `Machine Learning` module, I became familiar with the fundamentals of machine learning, including `Support Vector Machines (SVM)`, `Decision Trees`, `Naive Bayes`, and both `supervised` and `unsupervised` learning techniques.
        - ✳️ I had the opportunity to apply these concepts by building a machine learning model in Python to predict sales. The model achieved an impressive `97%` accuracy in its predictions.
    - ❇️ The `Neural Networks` and `Deep Learning` module was particularly fascinating to me.
        - ✳️ For my final assignment, I built a neural network from scratch, without using any external libraries, and earned a score of `80`.
        - ✳️ In another deep learning project using `Google Colab`, I used multiple hidden layers to predict a company's sales for the next year, achieving top rankings on Kaggle for prediction accuracy.
    - ❇️ In the `Combinatorial Optimization` module, I gained a deeper understanding of mathematical optimization techniques and their application to real-world problems.
        - ✳️ I explored theories like `Mixed-Integer Linear Programming (MLP)`, `Linear Programming (LP)`, and `Linear Regression`, which significantly enhanced my ability to approach complex decision-making scenarios with mathematical rigor.

    """
    )
    st.write ("##")

    # --- UNDERGRADUATE
    st.write ("**Islamic Azad University - Finance & Accounting**")
    st.write ("September 2014 - March 2018")
    st.write ("GPA: `17.22 out 20.00` (`Top 5%` of the class)")
    st.write (
        """
    - ❇️ 	I gained extensive knowledge of `GOCE` and `IFRS` standards, with a particular focus on financial management, where I achieved a perfect score of `20/20`.
    - ❇️ 	My performance in financial management led to an invitation from one of my professors to work at his company.


    """
    )   
    
    
    with right_column:
        st_lottie (lottie_coding, height=400, key="coding")
