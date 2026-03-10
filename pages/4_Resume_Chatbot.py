import streamlit as st
from chatbot.chatbot import agent_response

# 1. Configurações da Página
st.set_page_config(page_title="Antoniel AI - Portfólio")
st.title("🤖 Converse com o meu Currículo")
st.markdown(
    "Olá! Eu sou o assistente virtual do **Antoniel**. Pergunte-me sobre ele, habilidades, experiências ou formação!")

# 2. Inicialização da Memória (Session State)
# Se for a primeira vez que o usuário abre a página, criamos a lista de mensagens
if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {"role": "assistant", "content": "Como posso te ajudar a conhecer melhor o perfil do Antoniel?"}
    ]

# 3. Renderização do Histórico
# Desenha na tela todas as mensagens que já estão salvas na memória
for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 4. A Caixa de Texto (Input) e a Lógica de Resposta
pergunta = st.chat_input("Ex: Onde ele estudou?")

if pergunta:
    # A. Mostra a pergunta do usuário na tela e salva na memória
    with st.chat_message("user"):
        st.markdown(pergunta)
    st.session_state.mensagens.append({"role": "user", "content": pergunta})

    # B. Chama a SUA função do chatbot.py (A mágica acontece aqui!)
    with st.chat_message("assistant"):
        # Mostra um "Pensando..." enquanto o Gemini processa
        with st.spinner("Analisando o currículo..."):
            response = agent_response(pergunta)
            st.markdown(response)

    # C. Salva a resposta da IA na memória para não sumir no próximo recarregamento
    st.session_state.mensagens.append({"role": "assistant", "content": response})
