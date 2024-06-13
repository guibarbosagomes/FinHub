import streamlit as st
from bd.insert import insert_usuario
from bd.select import check_email
from envio_email.enviar_email import enviar_email_registro
from datetime import datetime

if st.button("Voltar"):
    st.switch_page("main.py")

st.title("Registrar")

with st.form("registrar", clear_on_submit = False):

    nome_completo = st.text_input("Nome", placeholder = "Nome completo")
    
    dt_nascimento = st.date_input("Data de nascimento", value= None, format="DD/MM/YYYY", min_value = datetime(1950,1,1))

    usuario = st.text_input("Usuário", placeholder = "nome.sobrenome")
    email = st.text_input("E-mail", placeholder = "exemplo@locaweb.com.br")
    senha = st.text_input("Senha", placeholder = "Informe uma senha com pelo menos 6 digitos", type="password")
    repetir_senha = st.text_input("Confirmar senha", placeholder = "Confirme a senha com pelo menos 6 digitos", type= "password")
    
    registrar = st.form_submit_button("Registrar", use_container_width=True)

    if registrar:
        # st.session_state["nome_completo"] = nome_completo
        # st.switch_page("pages/main2.py")

            if nome_completo and usuario and email and senha and repetir_senha and dt_nascimento:
                if check_email(email):
                    if senha == repetir_senha:
                        if len(senha) >= 6 and len(repetir_senha) >= 6:
                            insert_usuario(nome_completo, dt_nascimento.strftime("%Y-%m-%d %H:%M:%S"), usuario, senha, email)
                            
                            st.session_state["usuario"] = "usuario"
                            
                            msg = """
                                <div style="text-align: center;">
                                Usuário cadastrado com sucesso.</br>
                                Seus dados foram enviados por email.</br>
                                Clique em <b>Voltar</b> para acessar.
                                </br>
                                </br>
                                </div>
                                """
                                                     
                            st.markdown(msg, unsafe_allow_html=True)
                        else:
                            st.warning("As senhas devem ter pelo menos 6 digitos !")
                    else:
                        st.warning("As senhas devem ser identicas !")
                else:
                    st.warning("Email já cadastrado !")   
            else:
                st.warning("Existem campos vazios !")