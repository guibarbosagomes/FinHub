import streamlit as st
from bd.select_data import check_login

if st.button("Voltar"):
    st.switch_page("main.py")

st.write("Login")

with st.form("login"):
    usuario = st.text_input("Usuário", placeholder = "Informe seu usuário, nome.sobrenome")
    senha = st.text_input("Senha", placeholder = "Informe sua senha")

    logar = st.form_submit_button("Logar", use_container_width=True)
    
    rec_senha = st.form_submit_button("Recuperar senha", use_container_width = True)
    
    if logar:
        if usuario and senha:
            if check_login(usuario, senha):
                st.session_state["usuario"] = usuario
                st.switch_page("pages/main2.py")

            else:
                st.warning("Usuário ou senha incorretos.")
        else:
            st.warning("Existem campos em branco !")
        
    elif rec_senha:
        st.switch_page("pages/recuperar_senha.py")

