# Verificando a média
# Solicite ao usuário a média do aluno
# Se maior ou igual a 7, mostre como aprovado
# Caso contrário, mostre como reprovado.

import streamlit as st

st.title("Verificando a média")

media = st.number_input("Digite sua média: ", min_value=0, max_value=10, step=1)

if st.button("Verificar"):
    if media >=7:
        st.success("Aprovado.")
    else:
        st.error("Reprovado.")

else:
    st.info("Por favor, digite sua média")

# sucess - verde
# warning - amarelo
# info - azul
# error - vermelho


