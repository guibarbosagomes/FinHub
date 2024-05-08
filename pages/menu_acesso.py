from st_pages import Page, add_page_title, show_pages, hide_pages
import streamlit as st


st.title("Bem vindo ao FinHub")

opcao = st.selectbox("Selecione uma opção", ["Acessar", "Registrar"], index = None, placeholder = "Acessar ou registrar ?")

print(opcao)

if opcao == "Acessar":
    st.switch_page("logi.py")

elif opcao == "Registrar":
    show_pages(
        [
            Page("registrar.py", "Registrar")
            # The pages appear in the order you pass them

        ]
    )