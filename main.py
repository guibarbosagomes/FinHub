import streamlit as st
from streamlit_option_menu import option_menu

class MultiApp:

    def __init__(self) -> None:
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title" : title,
            "function" : function
        })

    def run():
        st.title("Bem vindo ao FinHub")

        opcao = st.selectbox("Selecione uma opção", ["Acessar", "Registrar"], index = None, placeholder = "Acessar ou registrar ?")

        if opcao == "Acessar":
            st.switch_page("pages/login.py")

        if opcao == "Registrar":
            st.switch_page("pages/registrar.py")


    run()


