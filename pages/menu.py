import streamlit as st
from streamlit_option_menu import option_menu


def show_menu():
    with st.sidebar:
        app = option_menu(
            menu_title = "Menu" ,
            options = ["Home", "Fornecedores", "Ajuda", "Sair"],
            default_index=0,
        )
    
    return app