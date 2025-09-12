import streamlit as st

st.title("Atividade: Verificando notas")

soma = 0

for i in range(4):
    nota = st.number_input(f"Digite a {i+1}ª nota: ")
    soma = soma + nota

media = soma / 4

if st.button("Verificar"):
    st.info(f"Média: {media}")