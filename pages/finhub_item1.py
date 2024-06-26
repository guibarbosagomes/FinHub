import streamlit as st

def app():
    st.title("Indicadores")

    st.write(f"Bem vindo,", st.session_state["usuario"])
