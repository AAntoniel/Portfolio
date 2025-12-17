import streamlit as st

st.title("(In construction)📈Time Series Projects of Fires in Amazon Biome in Brazil")

st.write(
    """
    This page presents a comprehensive, visual analysis of fire trends within the Brazilian Amazon Biome, covering the full 
    pipeline from data preparation to model optimization and evaluation.
    
    Repository: No link yet

    Dataset: https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/anual/Brasil_sat_ref/
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

    ✔️ **Dataset:** Fires in Brazil from Inpe  
    ✔️ **Task:** Time Series Analysis  
    ✔️ **Model Type:** Arima and XGBoost  
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
    The first investigation focused on Brazil's six major biomes to identify macro-level environmental trends.
    
    #### Analysis by biomes

    While the dataset includes granular data for states and cities, the high high number of unique values of these variables makes them 
    less suitable for a country-wide overview. However, in a real-world deployment (e.g., for local government disaster management), 
    this same methodology could easily be adapted for state-specific drilling down. 
    
"""
)

st.image(
    "output/imgs/Dist_by_biomes.png",
    # use_container_width=True,
)

st.write(
    """
    The data reveals a critical concentration of incidents within the Amazon biome, which accounts for nearly 50% of all recorded 
    fires. The Cerrado follows as the second most affected area, contributing approximately 30% to the total volume.
    
    #### Analysis by Regions
    
    Following this biome-level overview, a breakdown by Geographic Region was conducted, as presented below: 
"""
)

st.image(
    "output/imgs/Dist_by_regions.png",
    # use_container_width=True,
)

st.write(
    """
    The regional breakdown corroborates the biome-level findings. The North region exhibits the most critical situation, followed by the Northeast and Center-West.
    This alignment is expected geographically: in Brazil, the Amazon biome is predominantly located in the North, while the Cerrado extends across significant portions of the 
    Center-West and Northeast. 
    
    #### Time series analysis
    
    Given the severity of the situation in these regions, individual time series were constructed for the Amazon and Cerrado biomes. The primary objective of this comparison 
    was to identify similarities in temporal behavior (seasonality and trend).
    
    **Note**: This comparative analysis serves as a preliminary step; as detailed in the subsequent sections, the final modeling phase focuses on a specific selection rather 
    than both datasets.
    
"""
)

st.image(
    "output/imgs/TS_by_amaz_cerr_daily.png",
    # use_container_width=True,
)

st.write(
    """
    Visual inspection confirms that while both regions share similar seasonal patterns, the magnitude of the Amazon fires is significantly higher, as anticipated. 
    In 2022 and 2024, daily occurrences surpassed 3,000 incidents, highlighting a severe, recurring annual crisis.

    From a strategic perspective, pinpointing these critical periods is vital. It can help firefighters and volunteer corps to optimize resource allocation 
    and improve operational efficiency during peak danger periods.
    
    The Amazon time series was selected for the subsequent modeling phases. To ensure robustness, the methodology transitioned from qualitative visual inspection to a 
    quantitative analysis, validating the data properties through statistical testing.
    
    #### Residual Norm
    
    The first challenge was to verify the presence of a seasonal component versus a cyclic one. Visual analysis strongly suggested a yearly pattern, but the noise 
    inherent in daily data made it difficult to confirm with 100% certainty.
    To validate this periodicity, a Residual Norm analysis was conducted. This method tests the correlation of the time series at specific lags by 
    fitting a Linear Regression model. The metric used (the square root of the sum of squared errors) quantifies the prediction 
    error. Consequently, the lag that yields the lowest residual norm indicates the strongest seasonal fit.
"""
)

st.image(
    "output/imgs/Res_norm_amaz.png",
    # use_container_width=True,
)

st.write(
    """
    Results showed that a 365-day lag produced the lowest residual norm, yet the difference was not significant enough to confirm strict annual seasonality. Instead, 
    the results for the 7, 30, and 365-day lags suggest short, medium, and long-term fire cycles, likely driven by environmental factors like rainfall patterns.
    The 180-day lag provides the strongest evidence for this cycle, acting as an 'inverse' indicator where high-activity periods are followed by low-activity 
    periods six months later. Ultimately, the pattern is stochastic, we can confirm the existence of the cycle, but predicting the exact magnitude of fire activity 
    on any given day remains a challenge due to inherent variability.
    
    #### Time series decomposition
    
    Following the initial analysis, the time series was decomposed into its three fundamental components: Trend, Seasonality, and Residuals. A classical decomposition 
    approach was applied using a 365-day moving average to estimate the trend. This specific window size was selected based on the previously identified annual cycle, 
    ensuring that the smoothing process accounts for a full yearly rotation.
"""
)

st.image(
    "output/imgs/Amaz_ts_dec.png",
    # use_container_width=True,
)

st.divider()
