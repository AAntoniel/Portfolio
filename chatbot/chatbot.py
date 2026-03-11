from dotenv import load_dotenv
import os
import streamlit as st

from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma

from datetime import datetime

load_dotenv()
# os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
if "GEMINI_API_KEY" in st.secrets:
    os.environ["GOOGLE_API_KEY"] = st.secrets["GEMINI_API_KEY"]
elif os.getenv("GEMINI_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
else:
    st.error("Chave da API não encontrada! Verifique o .env ou o Streamlit Secrets.")

emb = GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001')

def retrieve(quest):
    db = Chroma(
        persist_directory = 'chatbot/chroma_db',
        embedding_function = emb
    )

    results = db.similarity_search(
        query = quest,
        k=2
    )


    # Results retorna uma lista de objetos, mas o modelo não le objetos, e sim textos. Abaixo, extrai-se apenas os textos.  Passa os metadados, 
    # Como os títulos e junta com o conteúdo para dar o contexto completo para a IA
    retrieve_texts = []

    for doc in results:
        title = " > ".join(doc.metadata.values())
        complete_content = f"[{title}]\n{doc.page_content}"

        retrieve_texts.append(complete_content)

    retrieve_context = "\n\n".join(retrieve_texts)

    return retrieve_context


model = ChatGoogleGenerativeAI(
    model = "gemini-3.1-flash-lite-preview",
    temperature = 0.2,
)

today = datetime.now().strftime("%B de %Y")

template = ChatPromptTemplate.from_messages([
    ("system", """Você é o assistente virtual do Antoniel. Responda as perguntas dos rcrutadores de forma profissional e simpátca, usando apenas o contexto 
                  fornecido abaixo.
     
                  INFORMAÇÃO TEMPORAL IMPORTANTE: A data de hoje é {today}. Compare essa data com as presentes nos contextos para utilizar o tempo
                  verbal correto.
     
                  CONTEXTO DO CURRÍCULO: {context}. 
     
                  Se a resposta não existir no contexto, diga que não sabe."""),
    ("human", "{user_input}")
])

def agent_response(question):
    try:
        context = retrieve(question)

        prompt_value = template.invoke({
            "context": context,
            "user_input": question,
            "today": today
        })

        response = model.invoke(prompt_value)

        return response.content[0]['text']

    except Exception as e:
        return f"Desculpe, ocorreu um erro ao consultar o currículo. {e}"