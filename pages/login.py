import streamlit as st
from bd.select import check_login

if st.button("Voltar"):
    st.switch_page("main.py")

st.write("Login")

with st.form("login", clear_on_submit = True):
    usuario = st.text_input("Usuário", placeholder = "Informe seu usuário")
    senha = st.text_input("Senha", placeholder = "Informe sua senha")

    logar = st.form_submit_button("Logar", use_container_width=True)

    if logar:
        if usuario and senha:
            if check_login(usuario, senha):
                st.session_state["usuario"] = usuario
                st.switch_page("pages/main2.py")

            else:
                st.warning("Usuário ou senha incorretos.")
        else:
            st.warning("Existem campos em branco !")
        
    msg = """
        <div style="text-align: center;">
            <a href="http://localhost:8501/recuperar_senha" target="_blank"> Recuperar senha ?</a>
        </div>
    """
    st.markdown(msg, unsafe_allow_html=True)

