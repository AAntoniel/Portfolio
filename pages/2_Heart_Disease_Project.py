import streamlit as st
import pandas as pd

st.title("❤️Heart Disease - Project Overview")

st.write(
    """
    This section provides a complete, clear, and visual explanation of the Heart Disease Prediction project — from
    data preparation to model evaluation and the final application.
    A escolha pelo dados de problemas cardíacos se deu pela vontado de criar um app simples, de fácil interpretação
    e que tivesse alguma utilidade além de um simples projeto de portfólio.
    Essa página irá explicar o que foi feito, sem entrar em muitos detalhes técnicos de código. Caso seja de interesse,
    O código completo pode ser conferido em: https://github.com/AAntoniel/Heart_disease

    Os dados utilizados são públicos e estão disponíveis em: https://archive.ics.uci.edu/ml/datasets/heart+disease
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
    use_container_width=True,
)

st.write(
    """
    O início dos tratamentos dos dados iniciou com a coluna target, que continha números diferentes de 0 e 1, 
    pois são possíveis tipos diferentes de doenças. O projeto atual buscou simplificar isso em uma classificação 
    binária, ou seja 0 = não possui doença; 1 = possui doença. Para essa variável, esse foi o único tratamento.

    Depois passando para as features, primeiramente foi a vez de verificar, valores 0s sem sentidos. Nas colunas como
    colesteról e pressão sanguínea em repouso, existiam marcações com 0, o que não faz sentido, pois uma pessoa
    sem essas medições não tem outro status a não ser morto. Esse valores 0s foram substituídos por NaNs, ou *Not
    a Number*, que, a grosso modo, pode ser classificado como valor faltante. Esse passo é necessário para o próximo
    passo, que é a imputação de valores faltantes. 

    Verificando os valores faltantes, observamos o seguinte:
"""
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("images_hd/missing_values.png", width=200)

st.write(
    """
    Para evitar distorções e tentar preservar o comportamento real dos dados, foi utilizada uma imputação condicional 
    baseada em sexo e tipo de dor no peito. Essa abordagem reduz viés, preserva diferenças clínicas entre grupos 
    e melhora a qualidade preditiva do modelo.

    Para as variáveis **numéricas** sendo elas as colunas *restbps,chol,max_heart_rate,oldpeak*, foi imputada a mediana
    dessas condições, já que ela não tem influência de valores atípicos. Já para as variáveis **categóricas**, colunas
    *fast_blood_sug, rest_electcard, exc_angina, slope, n_fl_maj_ves, thal*, a moda dessas condições foi escolhida.

    Essas variáveis foram apenas escolhas do autor, porém diversas outras formas de imputação podem ser empregadas,
    seja por diferentes variáveis ou diferentes técnicas.

    Após isso, sobrou apenas um linha com valores faltantes que foi excluída da base, pois não teria tanta influência
    no valor final e não valeria o esforço de imputar apenas mais uma linha de informação. Se verificar novamente os valores
    faltantes, obtém-se o seguinte:
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
    Dataset split into target and features and also in train and test splits
    Os dados foram estratificados para garantir a variabilidade e a proporção igual entre os targets de train e test 

    ### **E – Explore**
    No explore, as variáveis foram analisadas medindo sua influência em relação ao target com um *feature importances*. Inicialmente tudo 
    o que tinha uma acumulada menor do que 1 foi selecionado. O modelo ficou robusto, porém, a usabilidade para um usuário comum ficou difícil
    pois o modelo dependia muito de variáveis médicas avançadas para detectar uma doença.   
    Então, para facilitar a usabilidade do modelo, as variáveis *chol, max_heart_rate, chest_pain, sex, restbps, age, exc_angina* foram deixadas
    de forana hora do treinamento do modelo.
"""
)

st.write(
    """
    ### **M – Modify and M - Modeling**
    #### Modify
    Nesse passo, foi necessária transformar os dados em uma maneira que a máquina consiga entendê-los, então a primeira coisa foi discretizar
    as variáveis numéricas.
    Em resumo, discretizar é o processo de transformar variáveis contínuas em categorias para melhorar interpretação, e, em 
    alguns casos, aumentar a capacidade preditiva do modelo.
    Após a discretização é aplicado o *OneHotEncoder*, que então converte variáveis categóricas em colunas binárias, permitindo 
    que modelos os trabalhem com simples categorias de *sim* e *não*
    
    #### Modeling
    Com os dados prontos para uso, basta configurar o modelo. O modelo escolhido aqui foi o RandomForest. 
    Um GridSearch simples foi realizado, testando todas as combinações possíveis dos seguintes hiperparâmetros:
"""
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("images_hd/hips.png", width=550)

st.write(
    """
    ### **M – Modify and M - Modeling**
    #### Modify
    Nesse passo, foi necessária transformar os dados em uma maneira que a máquina consiga entendê-los, então a primeira coisa foi discretizar
    as variáveis numéricas.
    Em resumo, discretizar é o processo de transformar variáveis contínuas em categorias para melhorar interpretação, e, em 
    alguns casos, aumentar a capacidade preditiva do modelo.
    Após a discretização é aplicado o *OneHotEncoder*, que então converte variáveis categóricas em colunas binárias, permitindo 
    que modelos os trabalhem com simples categorias de *sim* e *não*
    
    #### Modeling
    Com os dados prontos para uso, basta configurar o modelo. O modelo escolhido aqui foi o RandomForest. 
    Um GridSearch simples foi realizado, testando todas as combinações possíveis dos seguintes hiperparâmetros:
"""
)

st.write(
    """
    ### **M – Modify and M - Modeling**
    
"""
)

st.divider()

# 4. Model Performance
st.write(
    """
    ### **A – Assess**
    - Final evaluation using test set  
    - Performance metrics and confusion matrix  
"""
)


st.header("📈 4. Model Performance")

st.write(
    """
Below are the main evaluation metrics used to assess model performance.
"""
)

# Create columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Accuracy", "XX%")

with col2:
    st.metric("Precision", "XX%")

with col3:
    st.metric("Recall", "XX%")

with col4:
    st.metric("F1-Score", "XX%")

st.divider()


# 5. Final App
st.header("💡 5. Interactive App")

st.write(
    """
The final classification model is available as an interactive app where users can test different inputs and see predictions in real-time.

👉 **Try the app using the sidebar (Heart Disease App)**  
"""
)

st.divider()

st.write(
    "Thank you for reading! Feel free to explore the app or the other pages in the sidebar."
)
