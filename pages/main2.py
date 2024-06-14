import streamlit as st
from streamlit_option_menu import option_menu
from pages import custos_detalhados, home, sair


if "usuario" in st.session_state:
    with st.sidebar:
        app = option_menu(
            menu_title = "Menu" ,
            options = ["Home", "FinHub", "Fornecedores", "Receita Varejo", "---", "Administracao", "Sair"],
            default_index=0,
        )

    if app == "Home":
        home.app()

    if app  == "Custos Detalhados":
        st.switch_page("pages/custos_detalhados.py")


    if app == "Sair":
        sair.app()
else:
    st.switch_page("pages/menu_acesso.py")