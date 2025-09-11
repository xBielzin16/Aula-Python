# Escreva um algoritmo que solicite do usuário
# um número e mostre a tabuada de multiplicação do número informado.

import streamlit as st
import time

st.title("Atividade: 3")

st.header("Tabuada de Multiplicação")

numero = st.number_input("Digite um número: ", min_value= 0, step=1)

if st.button("Iniciar"):
    for i in range(1,11):
        st.info(f"{numero} x {i} = {numero * i}")
        time.sleep(1)
    st.header("FIM.")

else:
    st.warning("Por favor, digite um número")