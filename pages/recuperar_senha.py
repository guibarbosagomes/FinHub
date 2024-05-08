import streamlit as st


if st.button("Voltar"):
    st.switch_page("main.py")

st.title("Recuperar senha")

with st.form("registrar"):
    empresa = st.selectbox("Empresa", ["LWSA", "Nextios", "Locaweb Varejo", "CPlug"], index = None, placeholder = "Selecione sua empresa")
    nome_completo = st.text_input("Nome", placeholder = "Informe seu nome completo")
    email = st.text_input("E-mail", placeholder = "Informe seu email")

    recuperar = st.form_submit_button("Registrar", use_container_width=True)

    if recuperar:
        # st.session_state["nome_completo"] = nome_completo
        st.switch_page("pages/main.py")