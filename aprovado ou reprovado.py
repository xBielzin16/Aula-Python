import streamlit as st

st.title("Atividade: Verificando resultado")

QUANTIDAD_NOTAS = 3
soma = 0

for i in range(QUANTIDAD_NOTAS):
    nota = st.number_input(f"Digite a {i+1}ª nota: ")
    soma = soma + nota

media = soma / QUANTIDAD_NOTAS

if st.button("Mostrar resultado"):
    st.info(f"Média: {media}")
    if media >= 7:
        st.success(f"Aprovado")
    elif media >= 4:
        st.warning(f"Recuperação")
    else:
        st.error(f"Reprovado")

