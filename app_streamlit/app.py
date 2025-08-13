import streamlit as st
from transformers import pipeline

st.title("Clasificador de Texto en Español")
texto = st.text_area("Escribe un texto:")

if st.button("Clasificar"):
    clasificador = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    resultado = clasificador(texto)
    st.write(resultado)