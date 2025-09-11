# Escrever um algoritimo que mostre os
# números ímpares entre 1 e 20.

import streamlit as st
import time

st.title("Atividade: 2")

st.header("Contagem de números ímpares entre 1 e 20.")

if st.button("Iniciar"):
    for i in range(1,20 +1,2):
        st.success(i)
        time.sleep(1)
    st.header("FIM")