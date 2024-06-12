import streamlit as st
from streamlit_option_menu import option_menu
from pages import home, sair, fornecedores

with st.sidebar:
    app = option_menu(
        menu_title = "Menu" ,
        options = ["Home", "Analises", "Fornecedores", "Ajuda", "Sair"],
        default_index=0,
    )

if app == "Home":
    home.app()

if app == "Fornecedores":
    fornecedores.app()

if app == "Sair":
    sair.app()