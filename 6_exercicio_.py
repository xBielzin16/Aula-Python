import streamlit as st

st.title("Atividade - Cálculos")

n1 = st.number_input("Digite o primeiro número: ")
n2 = st.number_input("Digite o segundo número: ")

media = (n1 + n2) / 2
soma = n1 + n2
produto = n1 * n2
min_value = min(n1,n2)
max_value = max(n1,n2)

if st.button("Verificar"):
    if n1 and n2:
        st.write(f"Sua média é: {media}")
        st.write(f"A soma é: {soma}")
        st.write(f"O produto é: {produto}")
        st.write(f"O menor valor é: {min_value}")
        st.write(f"O maior valor é: {max_value}")

else:
 st.info("Informe os números.")
