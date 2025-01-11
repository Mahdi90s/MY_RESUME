import requests
import streamlit as st
from pathlib import Path
from PIL import Image
from streamlit_lottie import st_lottie

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir /"styles" /"main.css"
resume_file = current_dir /"assets" /"Mirmahdi Mirhashemi CV.pdf"
coverlatter_file = current_dir /"assets" /"Mirmahdi Mirhashemi Cover Latter.pdf"
profile_pic = current_dir /"assets" /"2189.png"



# --- GENERAL SETTINGS ---
Page_TITLE = "My Portfolio"
PAGE_ICON = "🌐"
NAME = "Hi, my name is Mahdi 👋🏼"
TITLE = "Transforming Data into Decisions: A Data Scientist’s Story"
DESCRIPTION = "Data is the canvas, and analytics is my brush. This portfolio is a reflection of my journey—a blend of creativity, science, and problem-solving to transform data into impactful solutions."
EMAIL = "mirhashemim7@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/mirmahdi-mirhashemi",
    "GitHub": "https://github.com/Mahdi90s",
}

PROJECT = {
    "A": "1",
    "B": "2"
    
}

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
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.download_button(
        label= "📃 Dowload Cover_Latter",
        data=PDFCbyte,
        file_name=coverlatter_file.name,
        mime="application/octet-stream",
    )
    st.write("✉️", EMAIL)
    
     # --- SOCIAL LINKS ---

    # Icon URLs
    icon_urls = {
        "LinkedIn": "https://cdn-icons-png.flaticon.com/512/174/174857.png",  # LinkedIn icon
        "GitHub": "https://cdn-icons-png.flaticon.com/512/733/733553.png",      # GitHub icon
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
I specialize in turning complex data into actionable insights that drive decision-making and innovation. As a Data Science Master's student with a strong background in financial analysis, I bring a unique blend of analytical skills and technical expertise to every project. I work with programming languages like Python and R to build predictive models, SQL to manage and query large datasets, and tools like Power BI to create compelling data visualizations. My focus areas include:

- ✔️ Developing machine learning models for financial forecasting and optimization.
- ✔️ Crafting interactive dashboards to visualize performance metrics and trends.
- ✔️ Applying data science techniques to solve real-world problems in healthcare, finance, and beyond.

I thrive on collaboration and delivering results that make a measurable impact, whether it's optimizing business operations, improving sales performance, or advancing innovation in the biopharmaceutical space.
                     """)
                
        # --- EXPERIENCE & QUALIFICATIONS ---
        st.write ("#")
        st.subheader ("Experience & Qulifications")
        st.write (
            """
        - A
        - B
        - C

        """
        )




        # --- skills ---
        st.write ("#")
        st.subheader ("Hard Skills")
        st.write (
            """
        - 1
        - 2
        - 3

        """
        )



        # --- WORK HISTORY ---
        st.write ("#")
        st.subheader ("work History")
        st.write ("---")

        # --- JOB 1
        st.write ("**Data Analyst**")
        st.write ("02/2020 - Present")
        st.write (
            """
        - D
        - DD
        - DDDD
        """
        )

        # --- JOB 2
        st.write ("**Data Analyst**")
        st.write ("02/2020 - Present")
        st.write (
            """
        - D
        - DD
        - DDDD
        """
        )

        # --- JOB 3
        st.write ("**Data Analyst**")
        st.write ("02/2020 - Present")
        st.write (
            """
        - D
        - DD
        - DDDD
        """
        )



        # --- Projects & Accomplishments --- 
        st.write ("#")
        st.subheader ("Projects & Accomplishments")
        st.write("---")
        for project, link in PROJECT.items():
            st.write(f"[{project}]({link})")
    
    with right_column:
        st_lottie (lottie_coding, height=300, key="coding")