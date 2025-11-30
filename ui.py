import streamlit as st
import requests

st.title("Salesforce RAG Chatbot (Locale)")
q = st.text_input("Fai una domanda:")

if st.button("Invia"):
    r = requests.post("http://localhost:8000/ask", json={"question": q})
    st.write(r.json()["answer"])