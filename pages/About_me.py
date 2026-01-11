83% of storage used … If you run out, you can't create, edit, and upload files. Get 200 GB for R$14.99/mo.
import streamlit as st

st.title("About me")

# -- About me section --
st.write(
    """
    My name is Antoniel Kleber Stefaniak. I was born in 2001 and have been passionate about technology for as long as I can remember. This lifelong interest has shaped me 
    into a dedicated, data-driven professional who values precision and continuous growth.
    
    #### 🎸Beyond the code
    
    When I’m not at my desk working with data or developing software, I find balance through creative and technical hobbies that keep my mind active. I am a passionate 
    music enthusiast and a collector of CDs and LPs. Beyond listening, I dedicate time to studying music theory and practicing the electric guitar.
    
    I am also currently learning how to draw. This helps me develop a sharper eye for detail and provides a creative outlet that contrasts with my technical work.
    
    As someone who values a focused and calm environment, I spend much of my free time immersed in books. Whether it's fiction or technical literature, reading 
    is my favorite way to explore new perspectives.
    
    Below, you can find more information about me, my academic background, work experiences and technical skills. 
    """
)

# -- Graduation section --
st.write("#### 🎓Academic Background")
col1, col2 = st.columns(2)

with st.container(border=True):
    st.markdown("##### **Master with specialization in Applied AI** | UFSC (2025)")
    st.write("Focused on advanced predictive modeling and time series analysis.")

with st.container(border=True):
    st.markdown("##### **Bachelor in Software Engineering** | Ugv (2022)")
    st.write("Core training in software architecture and system development.")


# -- Professional experience section --
st.write("#### 💼Professional Experience")

col_a, col_b = st.columns(2)

with col_a:
    with st.container(border=True, height=250):  # Fixed height keeps boxes aligned
        st.markdown("##### **Data Analysis and Data Scientist**")
        st.write("**Whirlpool | 2025 - Current**")
        st.write(
            """
        - Maintained and enhanced company cost reduction systems.
        - Implemented analytical and AI solutions, optimizing processes and increasing operational efficiency.
        - Generated strategic insights through data analysis, supporting executive decision-making.
        - Introduced automation tools for critical tasks, significantly optimizing execution time. 
        """
        )

with col_b:
    with st.container(border=True, height=250):
        st.markdown("##### **Teaching Assistantship**")
        st.write("**UFSC | 2024**")
        st.write(
            """
        - Developed and delivered lectures on statistical methods.
        - Taught an introduction to time series analysis: characteristics, components and fundamental concepts.
        - Covered forecasting models, including ARIMA and its extensions.
        - Led a case study focusing on stock market applications.
        """
        )

col_a, col_b = st.columns(2)

with col_a:
    with st.container(border=True, height=250):  # Fixed height keeps boxes aligned
        st.markdown("##### **IT Intern and Support Specialist**")
        st.write("**Intellectual Distribution Center (CDI)| 2021 - 2022**")
        st.write(
            """
        - Assisted with computer hardware configuration and general IT department routines.
        - Supported operating system and network configuration.
        - Managed software installation, monitoring and regular data backups.
        - Provided technical support in the computer lab.
        """
        )


# -- Key project section --
st.write(
    """   
    #### 📜**Research & Publications**
    
    A key project of my career was my Master’s research, where I developed a comparative research using Classical Statistical models, Machine Learning, 
    and Large Language Models (LLMs) to forecast water demand in a coastal tourist city in Brazil. I am proud to share that a portion of this research was 
    accepted and published by Springer Nature for the BRACIS 2024 conference.
    
    *Link*: Stefaniak, A.K., et al. (2025). "A Case Study on Water Demand Forecasting in a Coastal Tourist City." Intelligent Systems. BRACIS 2024. Springer, Cham. https://doi.org/10.1007/978-3-031-79035-5_1
    """
)

st.write("#### 🛠️Technical Skills")

cols = st.columns(4)

with cols[0]:
    # Python
    with st.container(border=True):
        st.image(
            "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"
        )
        st.write("Python")

with cols[1]:
    # Sheets
    with st.container(border=True):
        st.image("https://www.svgrepo.com/show/223056/sheets-sheet.svg")
        st.write("Excel/GoogleSheets")


with cols[2]:
    # lookerstudio
    with st.container(border=True):
        st.image("https://www.svgrepo.com/show/354012/looker-icon.svg")
        st.write("LookerStudio")


with cols[3]:
    # Git
    with st.container(border=True):
        st.image(
            "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg"
        )
        st.write("Git/GitHub")

st.write("#### 📚Currently studying")

cols = st.columns(4)

with cols[0]:
    # SQL
    with st.container(border=True):
        st.image(
            "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/azuresqldatabase/azuresqldatabase-original.svg"
        )
        st.write("SQL")

with cols[1]:
    # Stats.
    with st.container(border=True):
        st.image("https://www.svgrepo.com/show/313344/statistics.svg")
        st.write("Statistics")

st.write(
    """
    #### **🚀Explore My Portfolio**
    
    Beyond my academic research, I enjoy applying data science to diverse real-world challenges. This portfolio features projects that span the entire data lifecycle, from 
    in-depth statistical analysis to building and deploying functional applications for real-world usage. I invite you to explore my work through the menu on the side.
"""
)

st.markdown("---")
st.write("### 📫 Contact & Socials")
st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    # LinkedIn
    st.markdown("""
        <div style="text-align: center;">
            <a href="https://www.linkedin.com/in/antoniel-k-stefaniak/" target="_blank">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="50">
            </a>
            <p style="margin-bottom: 0px; margin-top: 10px;">GitHub</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    # GitHub
    st.markdown("""
        <div style="text-align: center;">
            <a href="https://github.com/AAntoniel" target="_blank">
                <img src="https://www.svgrepo.com/show/439171/github.svg" width="50" style="filter: invert(100%) if_dark_mode;">
            </a>
            <p style="margin-bottom: 0px; margin-top: 10px;">GitHub</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    # Email
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" width="50">
            <p style="margin-bottom: 0px; margin-top: 10px;">Email</p>
            <p style="font-size: 16px;">antonielstefaniak@gmail.com</p>
        </div>
        """,
        unsafe_allow_html=True
    )

