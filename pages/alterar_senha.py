import streamlit as st
from datetime import datetime
from bd.select_data import check_codigo_secreto
from bd.update_data import update_senha, update_status_recuperar_senha

if st.button("Voltar"):
    st.switch_page("main.py")

st.title("Alterar senha")

with st.form("alterar_senha"):
    codigo_secreto = st.text_input("Código secreto", placeholder = "Informe o codigo enviado para seu email")
    senha = st.text_input("Senha", placeholder = "Informe uma senha com pelo menos 6 digitos", type="password")
    repetir_senha = st.text_input("Confirmar senha", placeholder = "Confirme a senha com pelo menos 6 digitos", type= "password")
    
    alterar = st.form_submit_button("Alterar senha.", use_container_width=True)

    if alterar:
        
        if codigo_secreto and senha and repetir_senha:
            if check_codigo_secreto(codigo_secreto):
                if senha == repetir_senha:
                            if len(senha) >= 6 and len(repetir_senha) >= 6:
                                
                                if update_senha(check_codigo_secreto(codigo_secreto), senha) & update_status_recuperar_senha(codigo_secreto):
                                    # A função check_codigo_secreto retorna o id do usuário caso esteja de acordo com o código
                                    msg = """
                                        <div style="text-align: center;">
                                        Senha alterada com sucesso.</br>
                                        Clique em Voltar para acessar.
                                        </br>
                                        </br>
                                        </div>
                                        """
                                    st.markdown(msg, unsafe_allow_html=True)
                                else:
                                     st.error("Erro ao atualizar a senha !")
                            else:
                                st.warning("As senhas devem ter pelo menos 6 digitos !")
                else:
                            st.warning("As senhas devem ser identicas !")
            else:
                st.warning("O Código informado não existe ou esta expirado !")
        else:
            st.warning("Existem campos vazios !")

                
        # st.session_state["nome_completo"] = nome_completo
