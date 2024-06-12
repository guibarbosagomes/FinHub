import streamlit as st


def app():
    st.title("Fornecedores")

    st.write(f"Bem vindo,", st.session_state["usuario"])