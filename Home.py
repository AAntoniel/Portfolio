import streamlit as st

lang = st.sidebar.radio("Language / Idioma", ["EN-US", "PT-BR"])

if lang == "EN-US":
    st.title("Antoniel's Portfolio 📚")

    st.write("## Welcome to my portfolio!")
    st.write("This portfolio is structured to demonstrate a versatile range of my data science competencies.")

    st.divider()

    # --- Time Series Project Section ---
    st.page_link("pages/1_Time_Series_Project.py", label="🔥📈 **Time Series Project: A Technical Deep Dive**")

    st.write("⏱️*Est. Read Time: 20–25 min*")

    st.write("""
        This project provides a comprehensive evaluation of daily fire occurrences within the Amazon region 
        through advanced time series forecasting. Utilizing a dataset spanning 2020 to 2024, the analysis 
        identifies the stochastic cycles and temporal dependencies that characterize environmental crises in Northern 
        Brazil. The methodology involves a comparative performance study between classical statistical forecasting (ARIMA) 
        and machine learning algorithms (XGBoost), employing Sliding Window to ensure predictive integrity. 
    """)

    st.divider()

    # --- Heart Disease Project Section ---
    st.page_link("pages/2_Heart_Disease_Project.py", label="❤️📊 **Heart Disease Project: Risk Classification & SEMMA Methodology**")

    st.write("⏱️*Est. Read Time: 10–15 min*")

    st.write("""
        This project showcases the end-to-end development of a heart disease classification system following the SEMMA methodology. It 
        features a decoupled architecture, using FastAPI to serve the model as an independent service, ensuring high scalability 
        and a clean separation between data logic and the user interface.
    """)

    st.divider()

    # --- Heart Disease App Section ---
    st.page_link("pages/3_Heart_Disease_App.py", label="❤️📱 **Heart Disease Interactive Screening App**")

    st.write("⏱️*Est. Read Time: < 5 min*")

    st.write("""
        This is the final application built after the "Heart Disease Project". It serves 
        as a risk assessment tool and is **not** a substitute for medical diagnosis. You can experiment with
        your own or hypothetical data. If the model detects anything unusual, it will highlight it, and in 
        such cases, consulting a medical professional may be advisable. 
    """)

    st.divider()

else:
    st.title("Portfólio de Antoniel 📚")

    st.write("## Bem vindo ao meu portfólio!")
    st.write("Este portfólio foi estruturado para demonstrar a versatilidade das minhas competências em ciência de dados.")

    st.divider()

    # --- Time Series Project Section ---
    st.page_link("pages/1_Time_Series_Project.py", label="🔥📈 **Projeto de Séries Temporais: Análise Técnica Detalhada**")

    st.write("⏱️*Leitura estimada: 20–25 min*")

    st.write("""
            Este projeto apresenta uma avaliação abrangente das ocorrências diárias de queimadas na região amazônica por meio 
            de previsões avançadas de séries temporais. Utilizando um conjunto de dados que abrange o período de 2020 a 2024, 
            a análise identifica os ciclos estocásticos e as dependências temporais que caracterizam as crises ambientais no 
            Norte do Brasil. A metodologia envolve um estudo comparativo de desempenho entre modelos estatísticos clássicos 
            (ARIMA) e algoritmos de machine learning (XGBoost), empregando a técnica de Sliding Window para garantir a integridade 
            preditiva. 
        """)

    st.divider()

    # --- Heart Disease Project Section ---
    st.page_link("pages/2_Heart_Disease_Project.py",
                 label="❤️📊 **Projeto de Doença Cardíaca: Classificação de Risco com Metodologia SEMMA**")

    st.write("⏱️*Leitura estimada: 10–15 min*")

    st.write("""
            Este projeto apresenta o desenvolvimento completo de um sistema de classificação de doenças cardíacas seguindo a 
            metodologia SEMMA. Ele apresenta uma arquitetura desacoplada, utilizando FastAPI para servir o modelo como um serviço independente, 
            garantindo alta escalabilidade e uma separação clara entre a lógica de dados e a interface do usuário.
        """)

    st.divider()

    # --- Heart Disease App Section ---
    st.page_link("pages/3_Heart_Disease_App.py", label="❤️📱 **App Interativo: Triagem de Doenças Cardíacas**")

    st.write("⏱️*Leitura estimada: < 5 min*")

    st.write("""
            Esta é a aplicação final desenvolvida a partir do 'Projeto de Doença Cardíaca'. Ela funciona como uma 
            ferramenta de avaliação de risco e **não** substitui o diagnóstico médico. Você pode testar o modelo com dados 
            próprios ou hipotéticos. Caso o modelo detecte qualquer padrão incomum, ele irá destacá-lo, e, nesses casos,
            é recomendável consultar um profissional de saúde.
        """)

    st.divider()