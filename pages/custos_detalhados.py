import streamlit as st
from pages import custos_detalhados, home, sair, item1, item2, item3
from streamlit_option_menu import option_menu

st.title("Custos Detalhados")

with st.sidebar:
    app_fornecedores = option_menu(
        menu_title = "Fornecedores",
        options = ["Real x Orçado", "Fornecedores", "Clasf. de Fornecedores", "Base Completa", "Voltar"],
        default_index=0,
    )

if app_fornecedores == "Item1":
    item1.app()

if app_fornecedores  == "Item2":
    item2.app()

if app_fornecedores  == "Item3":
    item3.app()

if app_fornecedores  == "Voltar":
    st.switch_page("pages/main2.py")

        