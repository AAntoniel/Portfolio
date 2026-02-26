import streamlit as st
import pandas as pd
import numpy as np
from feature_engine import discretisation, encoding
import requests

url = 'https://heart-disease-api-rp94.onrender.com/predict'

lang = st.sidebar.radio("Language / Idioma", ["EN-US", "PT-BR"])

if lang == "EN-US":
    st.title("❤️ Heart Disease Risk Calculator")
    st.markdown("### A Data Science Portfolio Project")

    st.warning(
        "⚠️ **DISCLAIMER:** This application is for **educational purposes only**. It does not replace a professional medical diagnosis. If you have health concerns, please consult a doctor."
    )

    st.divider()
    st.header("Patient Information")

    expander = st.expander("**Variable Descriptions (Click to learn more)**")
    with expander:
        st.markdown(
            """
            **1. Age:**
            The patient's age in years. Risk of heart disease generally increases with age.
    
            **2. Biological Sex:**
            Biological sex assigned at birth (Male or Female). Statistics show different risk profiles for men and women.
            <br>
            <br>
            **A Quick Note on Gender and Data** 
            
            I want everyone to feel welcome and included when using this tool. 
            <br>
            This risk model requires you to select **Male** or **Female** because the **original medical research and datasets** used for 
            training are limited to these two biological categories.
            <br>
            This input is used **only** for calculating established biological risk factors (like hormonal influences and risk onset age), and 
            **in no way** is intended to exclude or ignore the diversity of gender identities. 
            <br>
            Thank you for understanding these limitations in the source data; I am fully committed to inclusivity in my work.
    
            **3. Chest Pain Type:**
            * **Typical Angina:** Chest pain caused by reduced blood flow to the heart (usually feels like pressure/squeezing).
            * **Atypical Angina:** Chest pain that doesn't fit the "classic" description but is still suspicious.
            * **Non-anginal Pain:** Pain not related to the heart (e.g., muscle strain, rib pain).
            * **Asymptomatic:** No chest pain present.
    
            **4. Resting Blood Pressure:**
            The top number (systolic) of your blood pressure reading when sitting quietly (mm Hg).
            * *Normal:* < 120
            * *Elevated:* 120-129
            * *Hypertension:* > 130
    
            **5. Serum Cholesterol:**
            Total cholesterol level in the blood (mg/dL). High levels can lead to plaque buildup in arteries.
            * *Desirable:* < 200
            * *High:* > 240
    
            **6. Max Heart Rate Achieved:**
            The highest number of heartbeats per minute reached during maximum physical exertion (like running on a treadmill).
    
            **7. Exercise Induced Angina:**
            Do you feel chest pain or tightness specifically when you exercise or exert yourself? (Yes/No).
            """,
            unsafe_allow_html=True,
        )

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("What is your age?", min_value=18, max_value=100, value=50)
        sex = st.radio("What is your biological sex?", ["Female", "Male"])
        sex_bin = 1 if sex == "Male" else 0

        chest_pain_opt = st.selectbox(
            "Chest Pain Type",
            ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"],
        )
        # Mapeamento reverso para o modelo
        cp_mapping = {
            "Typical Angina": 1,
            "Atypical Angina": 2,
            "Non-anginal Pain": 3,
            "Asymptomatic": 4,
        }
        chest_pain = cp_mapping[chest_pain_opt]

    with col2:
        restbps = st.slider("Resting Blood Pressure (mm Hg)", 70, 200, 120)
        chol = st.slider("Serum Cholesterol (mg/dl)", 70, 700, 200)
        max_heart_rate = st.slider("Max Heart Rate Achieved", 50, 220, 150)

        exc_angina = st.radio("Exercise Induced Angina?", ["No", "Yes"])
        exc_angina_bin = 1 if exc_angina == "Yes" else 0

else:
    st.title("❤️ Calculadora de Risco de Doença Cardíaca")
    st.markdown("### Um Projeto de Portfólio de Ciência de Dados")

    st.warning(
        "⚠️ **AVISO LEGAL**: Esta aplicação destina-se apenas a fins **educativos**. Ela não substitui um diagnóstico médico profissional. Em caso de dúvidas ou sintomas, procure orientação médica profissional."
    )

    st.divider()
    st.header("Informações do paciente")

    expander = st.expander("**Descrição das variáveis (Clique para saber mais)**")
    with expander:
        st.markdown(
            """
            **1. Idade:**
            A idade do paciente em anos. Estatisticamente, a probabilidade de desenvolver problemas cardíacos tende a ser maior em faixas etárias mais elevadas.

            **2. Sexo Biológico:**
            Refere-se ao sexo biológico definido ao nascer (Masculino ou Feminino). Dados estatísticos indicam que homens e mulheres apresentam diferentes padrões de risco cardiovascular.
            <br>
            <br>
            **Uma Observação Importante sobre Gênero e Ciência de Dados** 

            Queremos garantir que todos se sintam incluídos e bem-vindos ao utilizar este aplicativo.
            <br>
            A necessidade de selecionar entre **Masculino** ou **Feminino** neste modelo deve-se ao fato de que os **estudos clínicos e bancos de dados originais** usados no 
            treinamento do algoritmo restringem-se a essas duas categorias biológicas.
            <br>
            O preenchimento deste campo serve apenas para o cálculo de fatores de risco biológicos estabelecidos (como influências hormonais e a idade de início do risco) e, de forma 
            alguma, tem o intuito de excluir ou ignorar a diversidade das identidades de gênero.
            <br>
            Agradeço a sua compreensão sobre esta limitação nos dados de origem e reafirmo meu compromisso com a inclusão.

            **3. Tipo de Dor no Peito:**
            * **Angina Típica:** Dor no peito causada pela redução do fluxo sanguíneo para o coração. Costuma ser sentida como um aperto ou pressão no peito.
            * **Angina Atípica:** Dor no peito que foge dos padrões tradicionais, mas que ainda assim levanta suspeitas médicas importantes.
            * **Dor Não Anginosa:** Refere-se a dores no peito que não têm origem cardíaca, podendo ser causadas por tensões musculares ou dores nas costelas.
            * **Assintomático:** Sem presença de dor no peito.

            **4. Pressão Arterial em Repouso:**
            O valor superior (sistólica) da sua medição de pressão arterial quando em repouso (mmHg).
            * *Normal:* < 120
            * *Elevado:* 120-129
            * *Hipertensão:* > 130

            **5. Colesterol:**
            Nível de colesterol total no sangue (mg/dL). Níveis elevados podem levar ao acúmulo de placas nas artérias.
            * *Recomendado:* < 200
            * *Alto:* > 240

            **6. Frequência Cardíaca Máxima Atingida:**
            O número máximo de batimentos por minuto atingido sob esforço físico intenso (ex: corrida em esteira).

            **7. Angina Induzida por Exercício:**
            Você sente dor ou aperto no peito especificamente quando pratica exercícios ou faz algum esforço físico? (Sim/Não)
            """,
            unsafe_allow_html=True,
        )

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Qual a sua idade?", min_value=18, max_value=100, value=50)
        sex = st.radio("Qual o seu sexo biológico?", ["Feminino", "Masculino"])
        sex_bin = 1 if sex == "Masculino" else 0

        chest_pain_opt = st.selectbox(
            "Tipo de Dor no Peito",
            ["Angina Típica", "Angina Atípica", "Dor Não Anginosa", "Assintomático"],
        )
        # Mapeamento reverso para o modelo
        cp_mapping = {
            "Angina Típica": 1,
            "Angina Atípica": 2,
            "Dor Não Anginosa": 3,
            "Assintomático": 4,
        }
        chest_pain = cp_mapping[chest_pain_opt]

    with col2:
        restbps = st.slider("Pressão Arterial em Repouso (mm Hg)", 70, 200, 120)
        chol = st.slider("Colesterol (mg/dl)", 70, 700, 200)
        max_heart_rate = st.slider("Frequência Cardíaca Máxima Atingida", 50, 220, 150)

        exc_angina = st.radio("Angina Induzida por Exercício?", ["Não", "Sim"])
        exc_angina_bin = 1 if exc_angina == "Sim" else 0

# prediction
user_input_dict = {
        "age": age,
        "sex": sex_bin,
        "chest_pain": chest_pain,
        "restbps": restbps,
        "chol": chol,
        "max_heart_rate": max_heart_rate,
        "exc_angina": exc_angina_bin,
    }

st.markdown("---")

button_text = "**Calculate Risk**" if lang == "EN-US" else "**Calcular Risco**"
spinner_text = "Making prediction..." if lang == "EN-US" else "Realizando a previsão..."

if st.button(button_text):
    with st.spinner(spinner_text):
        try:
            response = requests.post(url, json=user_input_dict)
            response.raise_for_status()  # Verifies api errors

            result = response.json()
            proba = result["Prediction"]

            if proba < 0.3:
                st.success(f"🟢 **{'Low Risk' if lang == 'EN-US' else 'Baixo Risco'}:** {proba:.1%}")
                st.write(
                    "**Great! Your profile suggests a healthy heart condition.**" if lang == "EN-US" else "**Excelente!** Seu perfil sugere uma condição cardíaca saudável.")

            elif 0.3 <= proba < 0.7:
                st.warning(f"🟡 **{'Moderate Risk' if lang == 'EN-US' else 'Risco Moderado'}:** {proba:.1%}")
                st.write(
                    "**Attention:** Your profile shows some risk factors." if lang == "EN-US" else "**Atenção:** Seu perfil apresenta alguns fatores de risco.")
                st.info(
                    "**Recommendation**: Schedule a routine check-up with a cardiologist to be sure." if lang == "EN-US" else "**Recomendação**: Procure um cardiologista para realizar exames de rotina e tirar suas dúvidas."
                )

            else:
                st.error(f"🔴 **{'High Risk' if lang == 'EN-US' else 'Risco Alto'}:** {proba:.1%}")
                st.write(
                    "**Alert:** Your profile strongly resembles patients with heart disease." if lang == "EN-US" else "**Alerta:** Seu perfil apresenta fortes semelhanças com o histórico de doenças cardíacas.")
                st.warning(
                    "**Recommendation**: Please consult a doctor immediately for clinical exams." if lang == "EN-US"  else "**Recomendação**: Por favor, consulte um médico o quanto antes para realizar exames diagnósticos."
                )

        except requests.exceptions.RequestException as e:
            st.error("Error connecting to the API." if lang == "EN-US" else "Erro ao conectar com a API.")

st.divider()

if lang == "EN-US":
    st.write(
        """
        **Thank you for reading and trying the app! If you want to check how was the construction of this app, please read the 'Heart Disease Project' in the side bar.**

        **Feel free to also explore the other pages in the sidebar.**
    """
    )
else:
    st.write(
            """
            **Obrigado por ler e testar o app! Se quiser ver como foi o processo de construção deste projeto, por favor, leia a seção 'Heart Disease Project' na barra lateral.**
    
            **Sinta-se a vontade para explorar as outras páginas no menu lateral.**
        """
    )