import streamlit as st

lang = st.sidebar.radio("Language / Idioma", ["EN-US", "PT-BR"])

if lang == "EN-US":

    st.title("📈Time Series Project of Fires in Amazon Biome in Brazil")

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
        "output_TS/imgs/dataset.png",
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
        "output_TS/imgs/Dist_by_biomes.png",
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
        "output_TS/imgs/Dist_by_regions.png",
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
        "output_TS/imgs/TS_by_amaz_cerr_daily.png",
        # use_container_width=True,
    )

    st.write(
        """
        Visual inspection confirms that while both regions share similar seasonal patterns, the magnitude of the Amazon fires is significantly higher, as anticipated. 
        In 2022 and 2024, some daily occurrences surpassed 3,000 incidents, highlighting a severe, recurring annual crisis.
    
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
        "output_TS/imgs/Res_norm_amaz.png",
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
        "output_TS/imgs/Amaz_ts_dec.png",
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
        "output_TS/imgs/Amaz_ACF_PACF.png",
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
        "output_TS/imgs/Sliding_window.png",
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
            "output_TS/imgs/hips.png",
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
        
        While the aggregate metrics provide a global overview of annual performance, the pronounced cycle identified during the exploratory phase necessitates a 
        more granular evaluation. Analyzing model accuracy on a monthly basis offers deeper insight into how the forecasting architectures respond to shifting environmental 
        conditions. The distribution of these errors and their seasonal variance are visualized in the box-plot below, highlighting periods of increased volatility and model 
        sensitivity.
    """
    )

    st.image(
        "output_TS/imgs/Boxplot_by_months.png",
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
        "output_TS/imgs/Real_pred_comp.png",
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
else:
    st.title("📈Projeto de Séries Temporais sobre Queimadas no Bioma Amazônia")

    st.write(
        """
        Esta página detalha o comportamento das queimadas na Amazônia por meio de uma análise visual robusta, 
        descrevendo todas as etapas, incluindo o tratamento de dados, a otimização de algoritmos e a avaliação de desempenho.

        Repositório: https://github.com/AAntoniel/Fires_brazil

        Base de dados: https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/anual/Brasil_sat_ref/
        """
    )

    st.divider()

    # 1. Project Summary
    st.header("📌 1. Resumo do Projeto")

    st.write(
        """
        Este projeto tem como objetivo analisar as séries temporais de queimadas no bioma Amazônia, no Brasil.

        O objetivo principal foi avaliar o impacto ambiental desses focos de incêndio, ao mesmo tempo em que se testavam 
        os limites preditivos e a profundidade de informações que podem ser extraídas exclusivamente a partir de dados 
        de séries temporais univariadas.

        ✔️ **Dataset:** Dados de queimadas no Brasil do Inpe  
        ✔️ **Task:** Análise de séries temporais  
        ✔️ **Modelos:** Arima e XGBoost  
    """
    )

    st.divider()

    # 2. Dataset Overview
    st.header("📊 2. Visão Geral dos Dados e Pré-processamento")

    st.write(
        """
        Abaixo está um breve resumo sobre a base de dados utilizada no projeto.

        - **Linhas:** 278299
        - **Colunas:** 9
    """
    )

    st.image(
        "output_TS/imgs/dataset.png",
        # use_container_width=True,
    )

    st.write(
        """
        O conjunto de dados abrange todas as regiões brasileiras, no período de 2020 a 2024. Ele já passou por pré-processamento e não apresenta valores ausentes ou 
        inconsistências, não necessitando de nenhuma técnica de imputação. No entanto, uma etapa específica de pré-processamento foi aplicada para excluir o 
        dia 29 de fevereiro dos anos bissextos, padronizando assim a frequência da série temporal.
    """
    )

    st.divider()

    # 3. Dataset Overview
    st.header("🧠 3. Análise Exploratória")

    st.write(
        """
        Antes de estruturar os dados para a modelagem de séries temporais, foi realizada uma análise exploratória para compreender os comportamentos dos dados. 
        A primeira investigação focou nos seis principais biomas brasileiros para identificar tendências ambientais em nível macro.

        #### Análise por biomas

        Apesar de o dataset conter dados detalhados por estado e cidade, o grande volume de valores únicos dificulta uma visão panorâmica do país. Por outro lado, 
        para aplicações práticas (como na gestão de desastres em governos locais), esta metodologia pode ser adaptada para focar em análises regionais específicas. 

    """
    )

    st.image(
        "output_TS/imgs/Dist_by_biomes.png",
        # use_container_width=True,
    )

    st.write(
        """
        Os dados revelam uma concentração crítica de incidentes no bioma Amazônia, que representa quase 50% de todas as queimadas registradas. O Cerrado 
        aparece logo em seguida como a segunda região mais atingida, contribuindo com aproximadamente 30% do volume total.

        #### Análise por regiões

        Seguindo esta visão geral por bioma, foi realizado um detalhamento por regiões, conforme apresentado abaixo: 
    """
    )

    st.image(
        "output_TS/imgs/Dist_by_regions.png",
        # use_container_width=True,
    )

    st.write(
        """
        O detalhamento regional corrobora os achados obtidos em nível de bioma. A Região Norte apresenta a situação mais crítica, seguida pelo Nordeste e Centro-Oeste. 
        Esse alinhamento é geograficamente esperado: no Brasil, o bioma Amazônia está localizado predominantemente no Norte, enquanto o Cerrado estende-se por grandes 
        porções do Centro-Oeste e Nordeste.

        #### Análise da série temporal

        Dada a gravidade da situação nestas regiões, foram construídas séries temporais individuais para os biomas Amazônia e Cerrado. O objetivo principal desta comparação 
        foi identificar semelhanças no comportamento temporal.

        **Nota**: Esta análise comparativa serve como uma etapa preliminar. Nas seções seguintes, a fase final de modelagem foca em uma série específica, 
        em vez de utilizar ambos os conjuntos de dados.

    """
    )

    st.image(
        "output_TS/imgs/TS_by_amaz_cerr_daily.png",
        # use_container_width=True,
    )

    st.write(
        """
        A inspeção visual confirma que, embora ambas as regiões compartilhem padrões sazonais semelhantes, a magnitude das queimadas na Amazônia é significativamente 
        maior, como previsto. Em 2022 e 2024, algumas ocorrências diárias ultrapassaram os 3.000 focos, evidenciando uma crise anual grave e recorrente.

        Sob uma perspectiva estratégica, a identificação precisa desses períodos críticos é vital. Ela pode auxiliar o corpo de bombeiros e as brigadas voluntárias na 
        otimização da alocação de recursos e na melhoria da eficiência operacional durante os períodos de maior risco.

        A série temporal da Amazônia foi selecionada para as fases de modelagem subsequentes. Para garantir a robustez, a metodologia transitou da inspeção visual 
        qualitativa para uma análise quantitativa, validando as propriedades dos dados por meio de testes estatísticos

        É importante destacar que o conjunto de dados foi dividido em conjuntos de treinamento e teste antes da análise. O período de treinamento abrange os dados de 
        janeiro de 2020 a dezembro de 2023, enquanto o ano de 2024 foi reservado como conjunto de teste. Todos os diagnósticos exploratórios e testes estatísticos 
        subsequentes foram realizados exclusivamente nos dados de treinamento para evitar o data leakage e garantir que o modelo seja validado 
        com observações nunca vistas.

        #### Norma dos Resíduos

        O primeiro desafio foi verificar a presença de um componente sazonal ou cíclico. A análise visual sugeriu fortemente um padrão anual, mas o ruído 
        intrínseco aos dados diários dificultou uma confirmação com 100% de certeza. Para validar essa periodicidade, foi realizada uma análise da Norma dos Resíduos. Este 
        método testa a correlação da série temporal em defasagens específicas através do ajuste de um modelo de Regressão Linear. A métrica utilizada (a raiz quadrada 
        da soma dos quadrados dos resíduos) quantifica o erro de previsão. Consequentemente, o lag que apresenta a menor norma indica o ajuste sazonal mais forte.
    """
    )

    st.image(
        "output_TS/imgs/Res_norm_amaz.png",
        # use_container_width=True,
    )

    st.write(
        """
        Os resultados mostraram que o lag de 365 dias produziu a menor norma residual, porém a diferença não foi significativa o suficiente para confirmar uma sazonalidade 
        anua. Em vez disso, os resultados para os lags de 7, 30 e 365 dias sugerem ciclos de queimadas de curto, médio e longo prazo, provavelmente impulsionados por 
        fatores ambientais, como as épocas de pouca ou muita chuva. O lag de 180 dias fornece a evidência mais forte para este ciclo, atuando como um 'indicador inverso', onde períodos 
        de alta atividade são seguidos por períodos de baixa atividade seis meses depois. Por fim, o padrão é estocástico: podemos confirmar a existência do ciclo, 
        mas prever a magnitude exata da atividade de fogo em um dia específico continua sendo um desafio devido à variabilidade.

        #### Decomposição da série temporal

        Após a análise inicial, a série temporal foi decomposta em seus três componentes fundamentais: Tendência, Sazonalidade e Resíduos. Utilizou-se uma 
        abordagem de decomposição clássica com uma média móvel de 365 dias para estimar a tendência. Esse tamanho específico de janela foi selecionado com base no ciclo 
        anual identificado anteriormente, garantindo que o processo de suavização considere uma rotação anual completa.
    """
    )

    st.image(
        "output_TS/imgs/Amaz_ts_dec.png",
        # use_container_width=True,
    )

    st.write(
        """
        O componente de tendência revela uma variabilidade significativa ano a ano. Por exemplo, 2021 apresenta um declínio perceptível para um patamar de base de 
        aproximadamente 200 queimadas diárias. No entanto, em 2022, esse número aumentou, ultrapassando os 300 focos diários. Dado o impacto ecológico, mesmo aumentos 
        aparentemente pequenos são significativos, e, no monitoramento ambiental, qualquer deslocamento para cima representa um desvio crítico em relação aos objetivos de
        minimização de queimadas.

        O componente sazonal revela uma forma de onda periódica regular, porém, essa regularidade é, em grande parte, resultado do período de 365 dias especificado durante a 
        decomposição aditiva. Ao definir a janela nesse intervalo, o modelo é matematicamente orientado a extrair um padrão anual. Apesar de ser uma função dos parâmetros do 
        modelo, esse resultado valida a existência de um ciclo anual nítido subjacente à alta variância inerente dos dados brutos.

        A análise dos resíduos valida ainda mais essas conclusões. Embora a decomposição consiga capturar um perfil sazonal médio, o componente residual mantém uma variância 
        significativa e padrões não aleatórios. Isso indica que o modelo captura o comportamento anual médio, mas falha em capturar picos anômalos de alta magnitude na atividade 
        diária de queimadas.

        Por fim, isso reforça a conclusão de que, embora a sazonalidade de 365 dias seja um indicador confiável para prever 'quando' as queimadas ocorrerão, ela é um 
        preditor 'fraco' para a magnitude dos eventos de queimadas, que parecem ser impulsionados por fatores estocásticos e mais voláteis.

        #### ACF e PACF

        Para concluir a fase exploratória da série, foram examinadas as Funções de Autocorrelação (ACF) e Autocorrelação Parcial (PACF). Enquanto o método da Norma Residual 
        foi utilizado para identificar periodicidades de longo prazo (como 180 ou 365 dias), a ACF e a PACF focam em dependências locais. Esse processo é vital para 
        capturar a dinâmica temporal imediata e quantificar a influência direta das observações históricas na atividade de queimadas atual, um passo crítico para definir a ordem 
        de potenciais modelos autorregressivos.
    """
    )

    st.image(
        "output_TS/imgs/Amaz_ACF_PACF.png",
        # use_container_width=True,
    )

    st.write(
        """
        O gráfico da ACF apresenta um decaimento lento e gradual. Mesmo na defasagem 41, as correlações permanecem positivas e estatisticamente significativas. 
        Essa correlação persistente indica que a série é não estacionária, o que significa que suas propriedades estatísticas mudam ao longo do tempo.

        A análise da PACF revela uma dinâmica diferente. Ao contrário da ACF, a PACF isola a correlação direta entre o valor atual e um lag anterior específico, 
        removendo a influência das defasagens intermediárias. Observam-se picos significativos nos lags 1 e 2, seguidos de um corte abrupto, com picos menores voltando a aparecer nos lags 5 e 7. No contexto de um modelo ARIMA, 
        esse corte brusco após as defasagens iniciais é um indicador clássico de um processo Autorregressivo (AR).

        "Por fim, a análise da ACF e PACF confirma dois pontos críticos: a série exige diferenciação devido à sua não estacionariedade e possui um comportamente
        autorregressiva claro nos lags 1, 2 e 5. Esses insights serão fundamentais para a estratégia de previsão, pois definem a janela de valores passados necessária 
        para que o modelo capture com precisão as flutuações diárias dos focos de incêndio no bioma.
    """
    )

    st.write(
        """
        #### Conclusão da análise exploratória

        A fase exploratória confirma que a atividade de fogo na Amazônia não é aleatória, mas segue um ciclo complexo, estocástico e de longo prazo. A análise 
        identificou um ciclo dominante de 365 dias (anual), acompanhado de um ciclo 'inverso' significativo de 180 dias, provavelmente associado a variações sazonais 
        nos regimes pluviométricos.

        Enquanto esses ciclos de longo prazo fornecem um baseline, os diagnósticos de ACF/PACF revelaram dependências críticas de curto prazo. Com base 
        nessas informações, a próxima fase envolve a implementação dos modelos ARIMA e XGBoost para prever a série, combinando métodos estatísticos clássicos e machine 
        learning para capturar essas dinâmicas temporais.
    """
    )

    st.divider()

    # 4. Model Implementation
    st.header("📉 4. Implementação dos Modelos")

    st.write(
        """
        A fase de modelagem começou com a normalização dos dados usando o *MinMaxScaler* do *Scikit-learn*. Esse processo redimensiona os dados para um intervalo entre 0 e 1, 
        o que melhora a eficiência computacional e a estabilidade numérica durante a otimização.

        Além disso, a aplicação de uma escala uniforme garante que tanto o modelo ARIMA quanto o XGBoost sejam avaliados sob condições idênticas, permitindo uma comparação 
        justa de seu poder preditivo. Para evitar data leakage, o scaler foi ajustado exclusivamente no conjunto de treinamento (2020–2023) e, 
        posteriormente, aplicado aos dados de teste de 2024.

        #### Avaliação do modelo

        Para avaliar os modelos de forma eficaz, foi implementada uma técnica de Janela Deslizante (Sliding Window). Na análise de séries temporais, manter a ordem 
        cronológica é crucial, pois o embaralhamento dos dados acarretaria na perda das dependências temporais que o modelo visa capturar.

        Esta abordagem utiliza duas janelas distintas: uma janela de treinamento (histórico) e uma janela de validação (horizonte de previsão). Conforme o processo 
        avança pelo conjunto de dados, a janela de treinamento desliza por um tamanho de passo fixo, incorporando novos dados enquanto descarta os mais antigos. 
        É importante mencionar que o modelo é retreinado a cada passo, garantindo que as previsões sejam sempre baseadas nas informações mais recentes disponíveis antes da 
        origem da previsão.

        A imagem abaixo apresenta uma representação visual de como a técnica funciona, com a janela de treinamento em azul e a de validação em laranja:
    """
    )

    st.image(
        "output_TS/imgs/Sliding_window.png",
        # use_container_width=True,
    )

    st.write(
        """
        #### Otimização dos modelos

        A otimização de hiperparâmetros foi conduzida utilizando os dados de 2023 tanto para treinamento quanto para validação dentro da estrutura de janela deslizante. 
        Um intervalo de parâmetros potenciais foi testado (conforme ilustrado abaixo), e apenas as configurações que alcançaram o menor Erro Médio Quadrático 
        (RMSE) foram selecionadas para a avaliação final no conjunto de teste de 2024.

        Embora ambos os modelos dependam exclusivamente da série temporal original, eles processam as informações de maneira distinta: o modelo ARIMA utiliza diretamente 
        os valores brutos e índices temporais, enquanto o XGBoost exigiu um feature engineering específico para extrair padrões temporais em um 
        formato tabular. O poder preditivo de ambos os modelos deriva inteiramente das propriedades da série temporal, sem o uso de variáveis exógenas.

        A estratégia de seleção de hiperparâmetros diferiu para cada modelo. Para o ARIMA, os parâmetros foram derivados diretamente dos diagnósticos estatísticos anteriores. 
        Para o XGBoost, utilizou-se uma gama de valores padrão comumente estabelecidos em pesquisas acadêmicas e tutoriais da indústria.
    """
    )

    col1, col2, col3 = st.columns(3)

    with col2:
        st.image(
            "output_TS/imgs/hips.png",
            # use_container_width=True,
        )

    st.divider()

    # 5. Results
    st.header("🎯 5. Performances dos modelos e resultados")

    st.write(
        """
        #### Melhores modelos encontrados
        Após a fase de otimização de hiperparâmetros, as configurações ideais para cada modelo foram identificadas. Esses parâmetros, selecionados com base no 
        desempenho dentro da janela de validação de 2023, estão resumidos abaixo:

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
        #### Avaliação dos modelos
        Os modelos ARIMA e XGBoost otimizados foram aplicados aos dados de 2024 para avaliar sua confiabilidade de previsão em cenários reais. Para determinar qual 
        arquitetura melhor capturou a dinâmica complexa da série de incêndios, as seguintes métricas de avaliação foram calculadas. Estes resultados oferecem uma 
        comparação direta das abordagens estatística e de aprendizado de máquina em um ambiente de alta volatilidade.

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
        As métricas de avaliação indicam que o XGBoost supera o modelo ARIMA, fornecendo previsões que estão, em média, mais próximas das observações registradas. Além disso, 
        o menor desvio padrão dos resíduos do XGBoost sugere maior estabilidade preditiva, visto que o modelo é menos propenso a anomalias extremas de previsão em comparação 
        ao ARIMA.

        No entanto, sob uma perspectiva ecológica, a magnitude absoluta dos erros permanece significativa. Ambos os modelos foram fortemente impactados pela estocasticidade 
        inerente dos dados. Isso é evidenciado pelo fato de que o desvio padrão dos erros excedeu as próprias métricas, indicando que a alta variação diária é a principal 
        influência à precisão preditiva neste ambiente volátil.

        Embora as métricas individuais forneçam uma visão panorâmica do desempenho anual, o ciclo identificada durante a fase exploratória exige uma avaliação 
        mais granular. Analisar a precisão do modelo mensalmente oferece uma compreensão mais profunda de como as arquiteturas de previsão respondem às mudanças nas condições 
        ambientais. A distribuição desses erros e sua variância sazonal estão visualizadas no box-plot abaixo, destacando períodos de maior variação e sensibilidade do modelo.
    """
    )

    st.image(
        "output_TS/imgs/Boxplot_by_months.png",
        # use_container_width=True,
    )

    st.write(
        """
        A distribuição mensal de erros destaca que a dificuldade preditiva está intrinsecamente ligada ao ciclo sazonal. De janeiro a junho, ambos os modelos demonstram uma 
        precisão quase perfeita, e, esse alto desempenho é atribuído à baixa intensidade de incêndios característica da estação chuvosa. Prever períodos de atividade insignificante, 
        frequentemente representados por zero ocorrências, apresenta um desafio mínimo para as arquiteturas. No entanto, o período de julho a dezembro representa a fase de 
        alta complexidade, com a degradação de desempenho mais significativa ocorrendo em agosto e setembro.

        Durante a estação crítica de incêndios, o comportamento divergente dos modelos torna-se evidente. As magnitudes dos erros começam a escalar em julho para ambas as 
        arquiteturas. O modelo ARIMA (azul) exibe um declínio contínuo na precisão que persiste até setembro. Em contraste, embora o XGBoost (laranja) apresente seu pico 
        de erro em agosto, ele demonstra uma resiliência superior ao se estabilizar de forma mais eficaz de setembro até o final do ano. A análise mensal confirma que o XGBoost 
        é mais robusto nos períodos de maior volatilidade do bioma em comparação ao ARIMA.

        Para concluir a análise de desempenho, os valores previstos para o conjunto de teste de 2024 foram plotados juntamente com os dados reais e são apresentados abaixo:
    """
    )

    st.image(
        "output_TS/imgs/Real_pred_comp.png",
        # use_container_width=True,
    )

    st.write(
        """
        A comparação visual das previsões de 2024 revela um nítido trade-off entre estabilidade do modelo e sensibilidade aos picos. O XGBoost (verde) demonstra robustez 
        superior e consistência física ao filtrar com sucesso o ruído de alta frequência e evitar valores negativos, no entanto, exibe um "efeito teto", subestimando 
        sistematicamente a magnitude dos picos sazonais extremos. Por outro lado, o modelo ARIMA (laranja) captura a intensidade desses picos de forma mais eficaz, mas 
        introduz uma volatilidade significativa. Essa sensibilidade leva a flutuações "nervosas" e previsões negativas, valores impossíveis durante a baixa temporada. Em 
        última análise, o XGBoost oferece um baseline conservador mais confiável para o planejamento estratégico, enquanto o ARIMA serve como um indicador mais sensível, 
        porém mais ruidoso, de potenciais eventos atípicos de alta intensidade.
    """
    )

    st.divider()

    # 6. Conclusion
    st.header("📖 6. Conclusão")

    st.write(
        """
        A análise demonstra que a previsão de eventos ambientais com alta variabilidade, como queimadas na Amazônia, exige um equilíbrio entre sensibilidade estatística e estabilidade 
        operacional. Embora o modelo XGBoost tenha se mostrado uma ferramenta mais confiável para o monitoramento de tendências gerais devido à sua consistência física e 
        capacidades de filtragem de ruído, ele teve dificuldade em capturar a magnitude total de eventos extremos. Por outro lado, a capacidade do ARIMA de sinalizar picos de 
        alta intensidade, apesar de seu ruído inerente e flutuações negativas, sugere que os modelos clássicos ainda possuem valor como indicadores de alerta, antecedendo dias 
        atípicos.

        Em resumo, a análise de séries temporais revela que a atividade de fogo na Amazônia é caracterizada por dinâmicas temporais altamente sofisticadas e complexas. O bioma 
        está sujeito a um ciclo anual de incêncidios crítico, acentuado por um comportamento estocástico de alta frequência. Ao restringir o estudo a uma abordagem univariada, os 
        modelos foram forçados a lidar com um ruído irredutível significativo, e, consequentemente, em um contexto ecológico profissional, a precisão preditiva atual permanece 
        abaixo do limite necessário para uma implementação operacional de alto risco. Essas descobertas estabelecem um roteiro claro para pesquisas futuras. Aumentar a eficácia
        dos modelos provavelmente exigirá a integração de variáveis ambientais exógenas, como precipitação e umidade por exemplo, juntamente com a exploração de arquiteturas mais avançadas.
        Tais melhorias são essenciais para reduzir as magnitudes dos erros, particularmente durante os períodos mais críticos de intensidade de queimadas.
    """
    )

    st.divider()

    st.write(
        "**Obrigado por ler este trabalho! Sinta-se a vontade para conferir outros projetos no menu lateral da página.**"
    )
