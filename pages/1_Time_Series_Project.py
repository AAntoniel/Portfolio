import streamlit as st

st.title("(In construction)📈Time Series Projects of Fires in Amazonia Biome in Brazil")

st.write(
    """
    This page presents a comprehensive, visual analysis of fire trends within the Brazilian Amazon Biome, covering the full 
    pipeline from data preparation to model optimization and evaluation.
    
    Repository: No link yet

    Dataset: No link yet
    """
)

st.divider()

# 1. Project Summary
st.header("📌 1. Project Summary")

st.write(
    """
    This project aims to analyse the fires time series of the Amazon biome in Brazil.

    The primary objective was to assess the environmental impact of these fires while evaluating the predictive limits and information 
    depth extractable solely from univariate time series data.

    ✔️ **Dataset:** UCI Heart Disease  
    ✔️ **Task:** Binary Classification  
    ✔️ **Model Type:** Random Forest  
"""
)

st.divider()

# 2. Dataset Overview
st.header("📊 2. Dataset Overview and pre-processing")

st.write(
    """
    Below is a brief presentation of the dataset used in this project.

    - **Rows:** 278299
    - **Columns:** 9
"""
)

st.image(
    "output/imgs/dataset.png",
    # use_container_width=True,
)

st.write(
    """
    The dataset utilized is pre-processed and free of missing values or inconsistencies. It covers all Brazilian regions,
    from 2020 to 2024. No imputation was required. However, a specific preprocessing step was applied to exclude February 
    29th from leap years, standardizing the time series frequency. 
"""
)

st.divider()

# 3. Dataset Overview
st.header("🧠 3. Exploratory analysis")

st.write(
    """
    Prior to structuring the data for time series modeling, an exploratory analysis was conducted to establish baseline behaviors. 
    The investigation focused on Brazil's six major biomes to identify macro-level environmental trends.

    While the dataset includes granular data for states and cities, the high high number of unique values of these variables makes them 
    less suitable for a country-wide overview. However, in a real-world deployment (e.g., for local government disaster management), 
    this same methodology could easily be adapted for state-specific drilling down. 
    
"""
)

# st.image(
#     "output/imgs/Dist_by_biomes.pdf",
#     # use_container_width=True,
# )

st.divider()
