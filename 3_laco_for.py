import streamlit as st

st.title("Contagem regressiva")

for i in range(10, 0, -1):
    st.write(i)