import streamlit as st

st.title("(In construction)📈Time Series Projects of Fires in Amazon Biome in Brazil")

st.write(
    """
    This page presents a comprehensive, visual analysis of fire trends within the Brazilian Amazon Biome, covering the full 
    pipeline from data preparation to model optimization and evaluation.
    
    Repository: https://github.com/AAntoniel/-In-construction-Fires_brazil

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
    
    It's important to highlight that the dataset was partitioned into training and testing sets prior to analysis. The training period covers data from January 2020 
    to December 2023, while 2024 was reserved as the test set. All subsequent exploratory diagnostics and statistical tests were conducted exclusively on the training 
    data to prevent data leakage and ensure the model is validated against entirely unseen observations.
    
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

st.write(
    """
    The trend component reveals significant year-over-year variability. For instance, 2021 shows a noticeable decline to a baseline of approximately 200 daily fires. However, 
    in 2022, this figure increased, surpassing 300 daily incidents. Given the ecological impact, even seemingly small increases are significant, in environmental monitoring, 
    any upward shift represents a critical deviation from fire-minimization objectives.
    
    The seasonal component reveals a regular periodic waveform, however, this regularity is largely a result of the 365-day period specified during the additive decomposition.
    By defining the window at this interval, the model is mathematically guided to extract an annual pattern. Despite being a function of the model's parameters, this result 
    validates the existence of a clear yearly cycle underlying the high inherent variance of the raw data.
    
    The analysis of the residuals further validates these conclusions. While the decomposition successfully isolates a mean seasonal profile, the residual component retains
    significant variance and non-random patterns. This indicates that the model captures the average annual rhythm but fails to encompass high-magnitude, anomalous spikes 
    in daily fire activity.

    Ultimately, this reinforces the finding that while 365-day seasonality is a reliable indicator for timing, but it's a 'weak' predictor for the magnitude of fire events, which 
    appear to be driven by more volatile, stochastic factors.
    
    #### ACF and PACF
    
    To conclude the exploratory phase of the series, the Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) were examined. While the Residual Norm method was 
    utilized to identify long-term macro-periodicities (such as 180 or 365 days), the ACF and PACF focus on local dependencies. This process is vital for capturing immediate temporal 
    dynamics and quantifying the direct influence of historical observations on current fire activity, a critical step for defining the order of potential autoregressive models.
"""
)

st.image(
    "output/imgs/Amaz_ACF_PACF.png",
    # use_container_width=True,
)

st.write(
    """
    The ACF plot exhibits a slow and gradual decay. Even at lag 41, the correlations remain positive and statistically significant. 
    This persistent correlation indicates that the series is non-stationary, meaning its statistical properties change over time.
    
    The PACF analysis reveals a different dynamic. Unlike the ACF, the PACF isolates the direct correlation between the current value and a specific previous lag 
    by removing the influence of intervening lags.
    
    Significant spikes are observed at lags 1 and 2, followed by a sharp cutoff, with smaller significant peaks reappearing at lags 5 and 7. In an ARIMA 
    framework, this sharp cutoff after the initial lags is a classic indicator of an Autoregressive (AR) process.
    
    Ultimately, the ACF and PACF analysis confirms two critical points: the series requires differencing due to non-stationarity, and it possesses a clear autoregressive 
    signature at lags 1, 2, 5. These insights will be fundamental to the forecasting strategy, as they define the 'look-back' window required for the model to accurately 
    capture the daily fluctuations of fire incidents in the biome.
"""
)

st.write(
    """
    #### Conclusion of the exploratory analysis
    
    The exploratory phase confirms that fire activity in the Amazon is not random, but follows a complex, stochastic long-term cycle. The analysis 
    identified a dominant 365-day (annual) cycle alongside a significant 180-day "inverse" cycle, likely tied to seasonal rainfall shifts.

    While these long-term cycles provide a baseline, the ACF/PACF diagnostics revealed critical short-term dependencies.
    With all that information, the next phase involves the implementation of ARIMA and XGBoost models to forecast the series, leveraging both classical 
    statistical methods and machine learning to capture these temporal dynamics.
"""
)

st.divider()

# 4. Model Implementation
st.header("📉 4. Model Implementation")

st.write(
    """
    The modeling phase began with data normalization using the *MinMaxScaler* from *Scikit-learn*. This process scales the data to a range between 0 and 1, 
    which improves computational efficiency and numerical stability during optimization.

    Furthermore, applying a uniform scale ensures that both the ARIMA and XGBoost models are evaluated under identical conditions, allowing for a fair comparison 
    of their predictive power. To prevent data leakage, the scaler was fitted exclusively on the training set (2020–2023) and subsequently applied to the 2024 test data.
    
    #### Model evaluation
    
    To evaluate the models effectively, a Sliding Window technique was implemented. In time series analysis, maintaining chronological order is crucial, as shuffling the 
    data would destroy the temporal dependencies the model aims to capture.

    This approach utilizes two distinct windows: a training window (history) and a validation window (forecast horizon). As the process 'walks' forward through the dataset,
    the training window slides by a fixed step size, incorporating new data points while discarding the oldest. It's important to mention that the model is retrained at each step, ensuring 
    that the predictions are always based on the most recent information available before the forecast origin.
    
    The image below shows a visual representation on how the technique works, with the training window in blue and the validation in orange:
"""
)

st.image(
    "output/imgs/Sliding_window.png",
    # use_container_width=True,
)

st.write(
    """
    #### Model Optimization
    
    Hyperparameter optimization was conducted using the 2023 data for both training and validation within the sliding window framework. A grid of potential 
    parameters was tested (as illustrated below), and only the configurations achieving the lowest Root Mean Squared Error (RMSE) were selected for the final 
    evaluation on the 2024 test set.

    While both models rely exclusively on the original time series, they process the information differently: the ARIMA model utilizes the raw values and temporal 
    indices directly, whereas XGBoost required specific feature engineering to extract temporal patterns into a tabular format. No external or exogenous variables 
    used, the predictive power of both models is derived entirely from the internal properties of the fire series.
    
    The hyperparameter selection strategy differed for each model. For ARIMA, the parameters were derived directly from the previous statistical diagnostics. 
    For XGBoost, it was utilized a range of standard values commonly established in academic research and industry tutorials.
"""
)

col1, col2, col3 = st.columns(3)

with col2:
    st.image(
        "output/imgs/hips.png",
        # use_container_width=True,
    )

st.divider()

# 5. Results
st.header("🎯 5. Results and Model performance")
