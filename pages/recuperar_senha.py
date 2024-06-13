import streamlit as st
from datetime import datetime

if st.button("Voltar"):
    st.switch_page("main.py")

st.title("Recuperar senha")

with st.form("registrar"):
    dt_nascimento = st.date_input("Data de nascimento", value= None, format="DD/MM/YYYY", min_value = datetime(1950,1,1))
    email = st.text_input("E-mail", placeholder = "Informe seu email")

    recuperar = st.form_submit_button("Enviar para email", use_container_width=True)

    if recuperar:
        if dt_nascimento and email:
                            
            st.session_state["usuario"] = "usuario"
            
            msg = """
                <div style="text-align: center;">
                    Dados enviados para o email.
                </br>
                </br>
                </div>
                """
                                                    
            st.markdown(msg, unsafe_allow_html=True)
        else:
            st.warning("Existem campos vazios !")

                
        # st.session_state["nome_completo"] = nome_completo
