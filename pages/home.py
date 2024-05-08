import streamlit as st

def app():
    st.title("Home")

    st.write(f"Bem vindo,", st.session_state["usuario"])