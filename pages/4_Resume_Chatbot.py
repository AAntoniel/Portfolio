import streamlit as st
from chatbot.chatbot import agent_response

st.set_page_config(page_title="Antoniel AI - Portfólio")
st.title("🤖 Converse com o meu Currículo")
st.markdown(
    "Olá! Eu sou o assistente virtual do **Antoniel**. Pergunte-me sobre ele, habilidades, experiências ou formação!")

# (Session State)
# Se for a primeira vez que o usuário abre a página, criamos uma lista de mensagens
if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {"role": "assistant", "content": "Como posso te ajudar a conhecer melhor o perfil do Antoniel?"}
    ]

# Deixa na tela todas as mensagens que já estão salvas na memória
for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# A Caixa de Texto (Input) e a Lógica de Resposta
pergunta = st.chat_input("Ex: Onde ele estudou?")

if pergunta:
    # Mostra a pergunta do usuário na tela e salva na memória
    with st.chat_message("user"):
        st.markdown(pergunta)
    st.session_state.mensagens.append({"role": "user", "content": pergunta})

    # Chama a função agent_response
    with st.chat_message("assistant"):
        with st.spinner("Analisando o currículo..."):
            response = agent_response(pergunta)
            st.markdown(response)

    # Salva a resposta da IA na memória para não sumir no próximo recarregamento
    st.session_state.mensagens.append({"role": "assistant", "content": response})
