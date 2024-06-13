#%%

import bcrypt

from sqlalchemy import select
from bd.table import usuario, empresa
from bd.connect import engine


from bd.insert import check_password

from datetime import datetime


#%%
def check_email(email):
    
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

def busca_senha():

    
        
#%%
def check_login(nome_usuario, senha):

    stmt = select(usuario.c.nome_usuario).where(usuario.c.nome_usuario == nome_usuario)

    with engine.connect() as conn:
        result = conn.execute(stmt)
        user = result.fetchone()

    if user:
        return True
    else:
        return False

