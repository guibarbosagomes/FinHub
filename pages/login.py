import streamlit as st

if st.button("Voltar"):
    st.switch_page("main.py")

st.write("Login")

with st.form("login", clear_on_submit = True):
    usuario = st.text_input("usuario", placeholder = "Informe seu usuário")
    senha = st.text_input("senha", placeholder = "Informe sua senha")

    logar = st.form_submit_button("Logar", use_container_width=True)

    if logar:
        st.session_state["user_id"] = usuario
        
    
    st.markdown("[Recuperar senha ?](%s)" % "https://localhost")

