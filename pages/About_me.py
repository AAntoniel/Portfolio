import streamlit as st

st.title("About me (IN CONSTRUCTION)")

st.write(
    """
    My name is Antoniel Kleber Stefaniak. I was born in 2001 and have been passionate about technology for as long as I can remember. I am a data-driven 
    professional with a Bachelor’s degree in Software Engineering, concluded in 2022 at Ugv - University Center, and a Master’s degree with a specialization 
    in Applied Artificial Intelligence from the Federal University of Santa Catarina (UFSC), finished in 2025.
    
    #### **Work experiences**
       
    *IN CONSTRUCTION*
       
    #### **Research & Publications**
    
    A key project of my career was my Master’s research, where I developed a comparative research using Classical Statistical models, Machine Learning, 
    and Large Language Models (LLMs) to forecast water demand in a coastal tourist city in Brazil. I am proud to share that a portion of this research was 
    accepted and published by Springer Nature for the BRACIS 2024 conference.
    
    *Link*: Stefaniak, A.K., et al. (2025). "A Case Study on Water Demand Forecasting in a Coastal Tourist City." Intelligent Systems. BRACIS 2024. Springer, Cham. https://doi.org/10.1007/978-3-031-79035-5_1
    """
)

st.write("### 🛠️ Technical Skills")

# Create a 4-column grid
cols = st.columns(4)

# Card 1: Python
with cols[0]:
    with st.container(border=True):
        st.image(
            "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"
        )
        st.caption("Python")

# Card 2: Scikit-Learn
with cols[1]:
    with st.container(border=True):
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/3/30/Google_Sheets_logo_%282014-2020%29.svg"
        )
        st.caption("Excel/GoogleSheets")

# Card 3: XGBoost (or similar)
with cols[2]:
    with st.container(border=True):
        st.image(
            "https://www.svgrepo.com/show/223056/sheets-sheet.svg"
        )
        st.caption("BI Tools")

# Card 4: Streamlit
with cols[3]:
    with st.container(border=True):
        st.image(
            "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg"
        )
        st.caption("Git/GitHub")

st.write(
    """
    #### **Explore My Portfolio**
    
    Beyond my academic research, I enjoy applying data science to diverse real-world challenges. This portfolio features projects that span the entire data lifecycle—from 
    in-depth statistical analysis to building and deploying functional applications for real-world usage. I invite you to explore my work through the menu on the side.
"""
)
