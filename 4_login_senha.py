import streamlit as st

st.title("Laço de repetição: While")

st.write("Crie um programa que solicite ao usuário seu login e uma senha. " \
"O programa deve continuar pedindo o login e a senha até que ambos estejam corretos.")

login_correto = "biel"
senha_correta = "2805"

st.session_state.setdefault("campo", False)
st.session_state.setdefault("tentativas", 0)

while  True:
    break

login = st.text_input("Digite seu login: ", disabled=st.session_state.campo)
senha = st.text_input("Digite sua senha: ", type="password", disabled=st.session_state.campo)

if st.button("Entrar"):
    if login == login_correto and senha == senha_correta:
        st.success("Acesso permitido.")
    else:
        st.session_state.tentativas += 1
        if st.session_state.tentativas <= 3:
            st.warning(f"Login ou senha incorretos, tentativas: {st.session_state.tentativas}")
        else:
            st.error("Número de tentativas inválida.")
            st.session_state.campo = True