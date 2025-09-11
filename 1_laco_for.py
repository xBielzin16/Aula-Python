# Escrever um algoritimo que mostra os
# números pares entre 100 e 120.


import streamlit as st
import time

st.title("Atividade: 1")


st.header("Laço de repetição: For")

if st.button("Iniciar"):
    for i in range(100,121,2):
        st.success(i)
        time.sleep(2)
    st.header("FIM.")