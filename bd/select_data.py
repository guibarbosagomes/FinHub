#%%

import bcrypt

from sqlalchemy import select, func
from bd.table import usuario, empresa, recuperacao_senha
from bd.connect import engine
from envio_email.enviar_email import enviar_email_rec_senha

from bd.insert_data import insert_recuperar_senha, check_password

from datetime import datetime


#%%
def check_email(email):
    # Função criada para checkar o email do cadastro
    emails = []

    stmt = select(usuario.c.email)
    with engine.connect() as conn:
        result = conn.execute(stmt)

        for row in result:
            emails.append(row.email)
    
    if email not in emails:
        return True
    else:
        return False
        

def check_login(nom_usuario, senha):
    # Função criada para checkar o processo de login
    stmt = select(usuario.c.nome_usuario, usuario.c.senha).where(usuario.c.nome_usuario == nom_usuario)

    with engine.connect() as conn:
        result = conn.execute(stmt).fetchone()

    if result:
        if check_password(senha, result[1]):
            return True
    else:
        False



def check_email_dt_nascimento(email, dt_nascimento):
    # Se as informações de email e data de nascimento fornecidas no formulário estiverem corretas, 
    # envia um email com um codigo secreto para recuperar senha.
    smt = select(usuario).where(usuario.c.email == email, usuario.c.dt_nascimento == dt_nascimento)

    with engine.connect() as con:
        result = con.execute(smt).fetchone()
        
    if result:
        # Envia email com o codigo e inclui na tabela de recuperar_senha
        enviar_email_rec_senha(result.email, insert_recuperar_senha(result.id))



def check_codigo_secreto(codigo):
    # Função que verifica o codigo secreto e retorna o id do usuário

    smt = select(recuperacao_senha).where(recuperacao_senha.c.cod_secreto == codigo, recuperacao_senha.c.status == True)

    with engine.connect() as con:
        result = con.execute(smt).fetchone()
        
    if result:
        return result.id_usuario
    else:
        return False