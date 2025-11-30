import streamlit as st
import requests

st.title("Salesforce RAG Chatbot (Locale)")
input_question = st.text_input("Fai una domanda:")

if st.button("Invia"):
    with st.spinner(""):
        try:
            response = requests.post("http://localhost:8000/ask", json={"question": input_question})
            st.write(response.json()["answer"])
            if response.status_code == 200:
                st.success("")
            else:
                st.error("Qualcosa è andato storto. Si prega di riprovare...")
        except Exception as e:
            st.error(f"Errore nella richiesta: {e}")