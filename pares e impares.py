import streamlit as st

st.title("Atividade: Verificando pares e ímpares")

pares = 0
impares = 0

for i in range(1,6):
    numero = st.number_input(f"Digite o {i}° número: ", step=1)
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

if st.button("Verificar"):
    st.info(f"Quantidade de pares: {pares}")
    st.info(f"Quantidade de ímpares: {impares}")