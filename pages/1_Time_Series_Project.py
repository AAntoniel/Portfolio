import streamlit as st

st.title("📈Time Series Projects of Fires in Amazon Biome in Brazil")

st.write(
    """
    This page presents a comprehensive, visual analysis of fire trends within the Brazilian Amazon Biome, covering the full 
    pipeline from data preparation to model optimization and evaluation.
    
    Repository: https://github.com/AAntoniel/Fires_brazil

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

st.write(
    """
    #### Optimal Models
    Following the hyperparameter optimization phase, the optimal configurations for each model were identified. These parameters, 
    selected based on their performance within the 2023 validation window, are summarized below:
    
    ##### ARIMA
"""
)

# Create columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("AR(p)", "5")

with col2:
    st.metric("I(d)", "1")

with col3:
    st.metric("MA(q)", "41")

st.write(
    """
    ##### XGBoost
"""
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("n_estimators", "400")

with col2:
    st.metric("d_values", "8")

with col3:
    st.metric("q_values", "16")

st.write(
    """
    #### Model Evaluation
    The optimized ARIMA and XGBoost models were applied to the 2024 data to assess their real-world forecasting reliability. 
    To determine which architecture best captured the complex dynamics of the fire series, the following evaluation metrics were calculated. 
    These results offer a direct comparison of the statistical and machine learning approaches in a high-volatility environment:
    
    ##### ARIMA
"""
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("RMSE", "234.69")

with col2:
    st.metric("RMSE std", "254.48")

with col3:
    st.metric("MAE", "190.75")

with col4:
    st.metric("MAE std", "209.84")

st.write(
    """
    ##### XGBoost
"""
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("RMSE", "199.94")

with col2:
    st.metric("RMSE std", "224.88")

with col3:
    st.metric("MAE", "163.58")

with col4:
    st.metric("MAE std", "183.63")

st.write(
    """
    The evaluation metrics indicate that XGBoost outperforms the ARIMA model, providing predictions that are, on average, closer to the recorded observations. 
    Furthermore, the lower standard deviation of the XGBoost residuals suggests greater predictive stability, as the model is less prone to extreme forecasting 
    anomalies compared to ARIMA.

    However, from an ecological perspective, the absolute magnitude of the errors remains significant. Both models were heavily impacted by the inherent stochasticity 
    of the data. This is evidenced by the fact that the standard deviation of the errors exceeded the metrics themselves, confirming that high-variance 'noise' is a 
    primary constraint on predictive accuracy in this volatile environment.
    
    While the aggregate metrics provide a global overview of annual performance, the pronounced seasonality identified during the exploratory phase necessitates a 
    more granular evaluation. Analyzing model accuracy on a monthly basis offers deeper insight into how the forecasting architectures respond to shifting environmental 
    conditions. The distribution of these errors and their seasonal variance are visualized in the box-plot below, highlighting periods of increased volatility and model 
    sensitivity.
"""
)

st.image(
    "output/imgs/Boxplot_by_months.png",
    # use_container_width=True,
)

st.write(
    """
    The monthly error distribution highlights that predictive difficulty is intrinsically linked to the seasonal cycle. From 
    January to June, both models demonstrate near-perfect accuracy. This high performance is attributed to the low fire intensity characteristic of 
    the wet season, forecasting periods of negligible activity, often represented by zero occurrences, presents minimal challenge to the architectures. However, 
    the period from July to December represents the 'high-complexity' phase, with the most significant performance degradation occurring in August and September.
    
    During the critical fire season, the divergent behavior of the models becomes evident. Error magnitudes begin to escalate in July for both architectures. The 
    ARIMA (blue) model exhibits a sustained decline in accuracy that persists through September. In contrast, while XGBoost (orange) experiences its peak error in August, it 
    demonstrates superior resilience by stabilizing more effectively from September through the end of the year. Ultimately, the monthly breakdown confirms that 
    XGBoost maintains a more robust error profile during the biome's most volatile periods.
    
    To conclude the performance analysis, the predicted values for the 2024 test set were plotted alongside the actual incidents and it's presented below:
"""
)

st.image(
    "output/imgs/Real_pred_comp.png",
    # use_container_width=True,
)

st.write(
    """
    The visual comparison of the 2024 forecasts reveals a distinct trade-off between model stability and peak sensitivity. XGBoost (green) demonstrates superior 
    robustness and physical consistency by successfully filtering high-frequency noise and avoiding negative values, however, it exhibits a 'ceiling effect,' 
    systematically underestimating the magnitude of extreme seasonal peaks. On the other hand, the ARIMA model (orange) captures the intensity of these spikes more 
    effectively but introduces significant volatility. This sensitivity leads to 'nervous' fluctuations and physically impossible negative predictions during the 
    low season. Ultimately, XGBoost offers a more reliable conservative baseline for strategic planning, while ARIMA serves as a more sensitive, but noisier, 
    indicator of potential high-intensity outlier events.
"""
)

st.divider()

# 6. Conclusion
st.header("📖 6. Conclusion")

st.write(
    """
    The analysis demonstrates that forecasting volatile environmental events like fires in Amazon requires a balance between statistical sensitivity and operational 
    stability. While the XGBoost model proved to be the more reliable tool for general trend monitoring due to its physical consistency and noise-filtering capabilities, 
    it struggled to capture the full magnitude of extreme events. On the other hand, ARIMA's ability to signal high-intensity peaks—despite its inherent "noise" and negative 
    fluctuations—suggests that classical models still hold value as early-warning indicators for outlier days.
    
    In summary, the time series analysis reveals that fire activity in the Amazon is characterized by highly sophisticated and complex temporal dynamics. The biome is 
    subject to a critical annual fire cycle, underscored by high-frequency stochastic behavior. By restricting the study to a univariate approach, the models were forced 
    to contend with significant irreducible noise; consequently, within a professional ecological context, the current predictive precision remains below the threshold 
    required for high-stakes operational deployment. These findings establish a clear roadmap for future research. Enhancing model efficacy will likely require the 
    integration of exogenous environmental variables—such as precipitation and humidity—alongside the exploration of more advanced architectures. Such improvements are 
    essential to reducing error magnitudes, particularly during the most critical periods of fire intensity.
"""
)

st.divider()

st.write(
    "**Thank you for reading! Feel free to explore the other project pages in the sidebar.**"
)
