import streamlit as st
from streamlit_option_menu import option_menu
from pages import home, sair, finhub


if "usuario" in st.session_state:
    with st.sidebar:
        app = option_menu(
            menu_title = "Menu" ,
            options = ["Home", "FinHub", "Receita Varejo", "---", "Administracao", "Sair"],
            default_index=0,
        )

    if app == "Home":
        home.app()

    if app  == "FinHub":
        st.switch_page("pages/finhub.py")


    if app == "Sair":
        sair.app()
else:
    st.switch_page("pages/menu_acesso.py")