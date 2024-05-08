import streamlit as st
from bd.insert import insert_usuario
from bd.select import check_email


if st.button("Voltar"):
    st.switch_page("main.py")

st.title("Registrar")

with st.form("registrar", clear_on_submit = False):

    nome_completo = st.text_input("Nome", placeholder = "Nome completo")
    usuario = st.text_input("Usuário", placeholder = "nome.sobrenome")
    email = st.text_input("E-mail", placeholder = "exemplo@locaweb.com.br")
    senha = st.text_input("Senha", placeholder = "Informe uma senha com pelo menos 6 digitos", type="password")
    repetir_senha = st.text_input("Confirmar senha", placeholder = "Confirme a senha com pelo menos 6 digitos", type= "password")

    registrar = st.form_submit_button("Registrar", use_container_width=True)

    if registrar:
        # st.session_state["nome_completo"] = nome_completo
        # st.switch_page("pages/main2.py")

            if nome_completo and usuario and email and senha and repetir_senha:
                if check_email(email):
                    if senha == repetir_senha:
                        if len(senha) > 6 and len(repetir_senha) > 6:
                            insert_usuario(nome_completo, usuario, senha, email)
                            st.session_state["usuario"] = "usuario"
                            st.success("Usuário criado com sucesso. Volte a página para fazer login.")
                        else:
                            st.warning("As senhas devem ter pelo menos 6 digitos !")
                    else:
                        st.warning("As senhas devem ser identicas !")
                else:
                    st.warning("Email já cadastrado !")   
            else:
                st.warning("Existem campos vazios !")