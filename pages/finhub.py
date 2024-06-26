import streamlit as st
from pages import home, sair, finhub_item1, finhub_item2, finhub_item3
from streamlit_option_menu import option_menu

with st.sidebar:
    app_fornecedores = option_menu(
        menu_title = "FinHub",
        options = ["Indicadores", "Real x Orçado", "Fornecedores", "Base Completa", "Voltar"],
        default_index=0,
    )

if app_fornecedores == "Indicadores":
    st.title("Indicadores")

if app_fornecedores  == "Real x Orçado":
    finhub_item2.app()

if app_fornecedores  == "Fornecedores":
    finhub_item3.app()

if app_fornecedores  == "Voltar":
    st.switch_page("pages/main2.py")

        