import streamlit as st
import pandas as pd

lang = st.sidebar.radio("Language / Idioma", ["EN-US", "PT-BR"])

if lang == "EN-US":

    st.title("❤️Heart Disease - Project Overview")

    st.write(
        """
        This page provides a complete, clear, and visual explanation of the Heart Disease Prediction project, from
        data preparation to model evaluation and the final application.
        
        The selection of heart disease data was driven by the goal of building a user-friendly tool with real-world applicability. This 
        overview focuses on the implementation logic and results rather than low-level code structure. 
        
        Repository: https://github.com/AAntoniel/Heart_disease
    
        Dataset: https://archive.ics.uci.edu/ml/datasets/heart+disease
        """
    )

    st.divider()

    # 1. Project Summary
    st.header("📌 1. Project Summary")

    st.write(
        """
        This project aims to build a **machine learning model** capable of predicting the presence of heart disease 
        based on patient clinical information.
    
        The goal is to create a **risk assessment** tool that helps identify individuals who *might* be at risk, 
        assisting early assessment and awareness.
    
        ✔️ **Dataset:** UCI Heart Disease  
        ✔️ **Task:** Binary Classification  
        ✔️ **Model Type:** Random Forest  
        ✔️ **Pipeline:** Following the **SEMMA methodology**  
    """
    )

    st.divider()


    # 2. Dataset Overview
    st.header("📊 2. Dataset Overview and pre-processing")

    st.write(
        """
        Below is a brief description of the dataset used in this project.
    
        - **Rows:** 920
        - **Columns:** 14
        - **Target variable:** heart_disease (1 = disease, 0 = no disease)
    
        **Example of input features:**
        - Age 
        - Sex 
        - Chest Pain Type
        - Resting Blood Pressure  
        - Cholesterol
        - Fasting Blood Sugar
        - Resting Electrocardiographic Results  
        - Maximum Heart Rate    
        - Exercise-Induced Angina  
        - ST Depression  
        - Slope
        - Number of major vessels colored by fluoroscopy
        - Thalassemia
    """
    )

    st.image(
        "images_hd/heart_dis_dataset.png",
        # use_container_width=True,
    )

    st.write(
        """
        The start of the data preprocessing aimed the target variable. The original multi-class target was binarized to 
        simplify the problem: 0 represented the absence of disease, and 1 indicated its presence.
        
        After that, for the features, the dataset contained biologically impossible zero values for variables such as cholesterol and 
        resting blood pressure. These entries were treated as data errors and converted to NaNs (Not a Number) to facilitate 
        the subsequent imputation strategy. 
        
        The analysis of missing values revealed the following distribution:
    """
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image("images_hd/missing_values.png", width=200)

    st.write(
        """
        To preserve data integrity and maintain clinical distinctions between groups, a conditional imputation method was applied based on Sex and Chest Pain Type.
    
        - Numerical Variables (restbps, chol, max_heart_rate, oldpeak): Imputed using the median of the subgroups to minimize the influence of outliers.
    
        - Categorical Variables (fast_blood_sug, rest_electcard, exc_angina, etc.): Imputed using the mode (most frequent value).
        
        To prevent the distortion of underlying data patterns, this approach rejects global metrics in favor of subgroup-specific values. By rejecting dataset-wide 
        averages in favor of subgroup metrics, the methodology ensures that the imputed data remains representative for specific patient clusters.
    
        Following this process, one residual row containing missing values was removed from the dataset. The resulting data integrity check showed:
    """
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image("images_hd/missing_values2.png", width=150)

    st.divider()

    # 3. Methodology (SEMMA)
    st.header("🧠 3. Methodology – SEMMA Approach")

    st.write(
        """
        The entire workflow was structured following the **SEMMA methodology**, widely used for data mining:
    
        ### **S – Sample**
        Dataset split into target and features and also in train and test splits.
        Stratified sampling was applied during the train-test split to preserve the distribution of the target variable and ensure sample variability. 
    
        ### **E – Explore**
        In the exploration, the variables were analyzed by measuring their influence in relation to the target using a *tree.feature_importances_* approach. 
        The initial modeling utilizing comprehensive clinical data achieved excellent technical performance 
        (Precision: 88.4%, Recall: 90.8%). However, the reliance on complex medical data created a barrier for ordinary users.
        
        To prioritize accessibility, the project pivoted to a "Lite Model" trained exclusively on demographics and basic symptoms. The objective shifted from 
        providing a complex clinical diagnosis to acting as a preventive screening tool.
        
        While this simplification reduced Precision to 77.9% (increasing the rate of false positives), the most critical safety metric, Recall, remained 
        robust at 88.2%, a minimal drop of 2.6%. This results showed that basic variables can be powerful predictors. The final model accepts a more conservative, 
        "alarmist" threshold to ensure universal usability and guarantee that high-risk cases are successfully flagged for medical attention.
    """
    )

    st.write(
        """
        ### **M – Modify and M - Modeling**
        #### Modify
        To ensure machine readability, numerical features were first discretized, transforming continuous values into categorical 
        bins to enhance interpretability and predictive power. Subsequently, One-Hot Encoding was applied to convert these categorical 
        features into binary vectors (0 or 1), allowing the algorithm to process them as distinct logical inputs.
        
        #### Modeling
        With the dataset fully preprocessed, the Random Forest algorithm was selected for implementation. To maximize performance, a Grid Search 
        was conducted to exhaustively test all potential combinations of the following hyperparameters:
    """
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.image("images_hd/hips.png", width=550)

    st.write(
        """
        After the optimization process, the best performing configuration was identified as follows:
    """
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.image("images_hd/best_hips.png", width=550)


    # 4. Model Performance
    st.write(
        """
        ### **A – Assess**
        The optimal model was validated against the test dataset. Performance was measured using Accuracy, AUC, Recall, Precision and the ROC Curve; 
        detailed results and metric values are presented in Section 4.
    """
    )

    st.divider()

    st.header("📈 4. Model Performance")

    st.write(
        """
    Below are the main evaluation metrics used to assess model performance.
    """
    )

    # Create columns
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Accuracy train", "84.12%")

    with col2:
        st.metric("Precision train", "84.22%")

    with col3:
        st.metric("Recall train", "87.73%")

    with col4:
        st.metric("AUC Score train", "90.97%")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Accuracy test", "79.71%")

    with col2:
        st.metric("Precision test", "77.9%")

    with col3:
        st.metric("Recall test", "88.15%")

    with col4:
        st.metric("AUC Score test", "89.53%")

    st.write("Roc Curve")
    st.image("images_hd/roc_curve.png")

    st.divider()

    # 5. Conclusion
    st.header("5. Conclusion")

    st.write(
        """
        With a 89.53% of AUC, the model demonstrates excellent discriminative power on test data proving that it can effectively distinguish between healthy and at-risk 
        patients even without advanced medical variables.
        
        As a screening tool, the Recall was considered the critical metric, since the priority was minimizing False Negatives. The model successfully flags approximately 
        88 out of 100 positive cases, acting as a reliable safety net using only simple and common data.
        
        The model adopts a conservative bias, prioritizing sensitivity over surgical precision. While this increases the rate of False Positives (healthy individuals flagged as risk), 
        this behavior is intentional in preventive medicine: it is preferable to warn a healthy patient than to ignore a potentially fatal condition.
        
        With a global accuracy of ~80%, the project validates that basic demographic and symptomatic variables (e.g., age, chest pain) are powerful predictors for initial cardiac triage.
    """
    )

    st.divider()

    # 6. Final App
    st.header("💡 6. Interactive App")

    st.write(
        """
    The final classification model is available as an interactive app where users can test different inputs and see predictions in real-time.
    
    👉 **Try the app using the sidebar (Heart Disease App)**  
    """
    )

    st.divider()

    st.write(
        "**Thank you for reading! Feel free to explore the app or the other pages in the sidebar.**"
    )
else:
    st.title("❤️App de doenças cardíacas - Visão geral do projeto")

    st.write(
        """
        Esta página fornece uma explicação completa, clara e visual do projeto de Previsão de Doenças Cardíacas, desde a preparação dos dados até a 
        avaliação do modelo e a aplicação final.

        A seleção dos dados de doenças cardíacas foi motivada pelo objetivo de desenvolver uma ferramenta intuitiva com aplicabilidade prática real. 
        Esta visão geral concentra-se na lógica de implementação e nos resultados, em vez de focar nos detalhes técnicos da estrutura do código.

        Repositório: https://github.com/AAntoniel/Heart_disease

        Base de dados: https://archive.ics.uci.edu/ml/datasets/heart+disease
        """
    )

    st.divider()

    # 1. Project Summary
    st.header("📌 1. Resumo do Projeto")

    st.write(
        """
        Este projeto visa construir um modelo de **machine learning** capaz de prever a presença de doenças cardíacas com base nas informações clínicas dos pacientes.

        O objetivo é criar uma ferramenta de **avaliação de risco** que ajude a identificar indivíduos que *possam* estar em risco, auxiliando na avaliação precoce e na conscientização.

        ✔️ **Dataset:** UCI Heart Disease  
        ✔️ **Task:** Classificação binária  
        ✔️ **Model Type:** Random Forest  
        ✔️ **Pipeline:** Metodologia **SEMMA**  
    """
    )

    st.divider()

    # 2. Dataset Overview
    st.header("📊 2. Visão Geral dos Dados e Pré-processamento")

    st.write(
        """
        Abaixo está uma breve descrição do conjunto de dados utilizado neste projeto.

        - **Linhas:** 920
        - **Colunas:** 14
        - **Variável resposta:** heart_disease (1 = disease, 0 = no disease)

        **Exemplos de features:**
        - Age 
        - Sex 
        - Chest Pain Type
        - Resting Blood Pressure  
        - Cholesterol
        - Fasting Blood Sugar
        - Resting Electrocardiographic Results  
        - Maximum Heart Rate    
        - Exercise-Induced Angina  
        - ST Depression  
        - Slope
        - Number of major vessels colored by fluoroscopy
        - Thalassemia
    """
    )

    st.image(
        "images_hd/heart_dis_dataset.png",
        # use_container_width=True,
    )

    st.write(
        """
        A etapa inicial do pré-processamento de dados focou na variável alvo. O alvo original multiclasse foi convertido em um formato binário para simplificar o problema: 0 representa a 
        ausência da doença e 1 indica sua presença.

        Em seguida, em relação a features, o conjunto de dados continha valores zero biologicamente impossíveis para variáveis como colesterol e pressão arterial em repouso. 
        Esses casos foram tratados como erros de dados e convertidas em NaNs (Not a Number) para facilitar a estratégia de imputação subsequente. 

        A análise de valores faltantes revelou a seguinte distribuição:
    """
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image("images_hd/missing_values.png", width=200)

    st.write(
        """
        Para preservar a integridade dos dados e manter as distinções clínicas entre os grupos, foi aplicado um método de imputação condicional com base no sexo e no 
        tipo de dor torácica dos pacientes.

        - Variáveis Numéricas (restbps, chol, max_heart_rate, oldpeak): Imputadas utilizando a mediana dos subgrupos para minimizar a influência de outliers.

        - Variáveis Categóricas (fast_blood_sug, rest_electcard, exc_angina, etc.): Imputadas utilizando a moda (valor mais frequente).

        Para não distorcer os padrões dos dados, esta abordagem prioriza valores específicos de subgrupos em vez de métricas globais. Ao evitar médias gerais, a metodologia 
        garante que os dados imputados representem cada grupo de pacientes de maneira mais próxima a realidade.

        Concluída essa etapa, uma única linha remanescente com valores faltantes foi excluída do dataset. A verificação de integridade realizada em seguida demonstrou o seguinte:
    """
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image("images_hd/missing_values2.png", width=150)

    st.divider()

    # 3. Methodology (SEMMA)
    st.header("🧠 3. Metodologia – Abordagem SEMMA")

    st.write(
        """
        Todo o processo foi organizado de acordo com a metodologia SEMMA, uma abordagem amplamente consolidada na área de mineração de dados:

        ### **S – Sample**
        O conjunto de dados foi dividido em variável resposta e features, além das partições de treino e teste. A amostragem estratificada foi aplicada durante a divisão de 
        treino-teste para preservar a distribuição da variável resposta e garantir a variabilidade amostral. 

        ### **E – Explore**
        Na fase de exploração, as variáveis foram analisadas medindo sua influência em relação ao alvo por meio da abordagem **tree.feature_importances_**. A modelagem 
        inicial, utilizando dados clínicos abrangentes, alcançou um excelente desempenho técnico (Precisão: 88,4%, Recall: 90,8%). No entanto, a dependência de 
        dados médicos complexos dificultaria o uso da ferramenta por usuários comuns.

        Para priorizar a acessibilidade, o projeto migrou para um "Modelo Lite" treinado exclusivamente em dados demográficos e sintomas comuns. O objetivo mudou de fornecer 
        um diagnóstico clínico complexo para atuar como uma ferramenta de triagem preventiva.

        Embora essa simplificação tenha reduzido a Precisão para 77,9% (aumentando a taxa de falsos positivos), a métrica de segurança mais crítica, o Recall, permaneceu 
        robusta em 88,2%, com uma queda mínima de 2,6%. Esses resultados mostraram que mesmo variáveis básicas podem ser preditores poderosos. Assim, o modelo opta por uma postura 
        mais cautelosa e sensível, priorizando a identificação de possíveis riscos para que nenhum caso crítico passe despercebido, mesmo que isso resulte em uma abordagem mais 
        "alarmista".
    """
    )

    st.write(
        """
        ### **M – Modify e M - Modeling**
        #### Modify
        Com o intuito de otimizar o processamento pelos algoritmos, as variáveis numéricas passaram por um processo de discretização, convertendo dados contínuos em
        categorias para melhorar tanto a compreensão quanto a capacidade de previsão do modelo. Em seguida, utilizou-se a técnica de One-Hot Encoding para transformar 
        essas categorias em vetores binários, assegurando que o sistema trate cada informação como um dado lógico independente.

        #### Modeling
        Com o conjunto de dados totalmente pré-processado, o algoritmo Random Forest foi selecionado para a implementação. Para maximizar o desempenho, foi realizado
        um Grid Search para testar exaustivamente todas as combinações potenciais dos seguintes hiperparâmetros:
    """
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.image("images_hd/hips.png", width=550)

    st.write(
        """
        Após o processo de otimização, a configuração com a melhor perfomance encontrada foi:
    """
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.image("images_hd/best_hips.png", width=550)

    # 4. Model Performance
    st.write(
        """
        ### **A – Assess**
        O modelo otimizado foi validado com o conjunto de dados de teste. O desempenho foi mensurado utilizando as métricas Accuracy, AUC, Recall, 
        Precision e a ROC Curve. Os resultados detalhados e os valores das métricas são apresentados na Seção 4.
    """
    )

    st.divider()

    st.header("📈 4. Performance do modelo")

    st.write(
        """
    Abaixo estão as métricas de avaliação utilizadas para avaliar o desempenho do modelo. 
    """
    )

    # Create columns
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Accuracy train", "84.12%")

    with col2:
        st.metric("Precision train", "84.22%")

    with col3:
        st.metric("Recall train", "87.73%")

    with col4:
        st.metric("AUC Score train", "90.97%")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Accuracy test", "79.71%")

    with col2:
        st.metric("Precision test", "77.9%")

    with col3:
        st.metric("Recall test", "88.15%")

    with col4:
        st.metric("AUC Score test", "89.53%")

    st.write("Roc Curve")
    st.image("images_hd/roc_curve.png")

    st.divider()

    # 5. Conclusion
    st.header("5. Conclusão")

    st.write(
        """
        Com um AUC de 89,53%, o modelo demonstra um excelente poder discriminatório nos dados de teste, provando que consegue distinguir de forma eficaz entre pacientes 
        saudáveis e em risco, mesmo sem o uso de variáveis médicas avançadas.

        Como uma ferramenta de triagem, o Recall foi considerado a métrica crítica, visto que a prioridade era minimizar os Falsos Negativos. O modelo sinaliza com sucesso aproximadamente 88 
        em cada 100 casos positivos, atuando como uma rede de segurança confiável utilizando apenas dados simples e comuns.

        O modelo adota um viés conservador, priorizando a sensibilidade em detrimento de uma precisão cirúrgica. Embora isso aumente a taxa de Falsos Positivos (indivíduos
        saudáveis classificados com risco), esse comportamento é intencional na medicina preventiva: é preferível alertar um paciente saudável do que ignorar uma condição
        potencialmente fatal.

        Apresentando uma acurácia global de aproximadamente 80%, o projeto demonstra que indicadores demográficos e sintomas simples, como idade e dor no peito, funcionam como 
        preditores robustos para uma triagem cardíaca inicial.
    """
    )

    st.divider()

    # 6. Final App
    st.header("💡 6. App Interativo")

    st.write(
        """
        O modelo de classificação final está disponível como um aplicativo interativo,permitindo que os usuários experimentem diferentes variáveis e acompanhem os resultados das 
        predições instantaneamente.

    👉 **Você pode explorar as funcionalidades da ferramenta através da barra lateral (Heart Disease App)**  
    """
    )

    st.divider()

    st.write(
        "**Obrigado por ler este trabalho! Sinta-se a vontade para conferir outros projetos no menu lateral da página.**"
    )