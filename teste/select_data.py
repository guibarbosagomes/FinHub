
#%%

import bcrypt
from sqlalchemy import select, func
from connect import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, Text, Boolean, Date

from datetime import datetime

#%%
meta_obj = MetaData()


#%%
usuario = Table(
    "usuario",
    meta_obj,
    Column("id", Integer, primary_key = True, autoincrement = True),
    Column("nome_completo", String(30), nullable = False ),
    Column("dt_nascimento", DateTime, nullable = False ),
    Column("nome_usuario", String(50), nullable = False ),
    Column("email", String(50), nullable = False),
    Column("senha", Text, nullable = False),
    Column("dt_cadastro", DateTime, nullable = False )
)

empresa = Table(
    "empresa",
    meta_obj,
    Column("id", Integer, primary_key = True, autoincrement = True),
    Column("cod_empresa", String(10), nullable = False ),
    Column("desc_empresa", String(50), nullable = False ),
)


recuperacao_senha = Table(
    "recuperacao_senha",
    meta_obj,
    Column("id", Integer, primary_key = True, autoincrement = True),
    Column("id_usuario", Integer),
    Column("cod_secreto", String(50), nullable = False ),
    Column("status", Boolean, nullable = False ),
    Column("dt_solicitacao", Date, nullable = False ),
)

#%%
def check_email_dt_nascimento(email, dt_nascimento):
    # Se as informações de email e data de nascimento fornecidas no formulário estiverem corretas, 
    # envia um email com um codigo secreto para recuperar senha.
    smt = select(usuario).where(usuario.c.email == email, usuario.c.dt_nascimento == dt_nascimento)

    with engine.connect() as con:
        result = con.execute(smt).fetchone()
    
    return result.id_usuario

# %%
def check_codigo_secreto(codigo):

    smt = select(recuperacao_senha).where(recuperacao_senha.c.cod_secreto == codigo, recuperacao_senha.c.status == True)

    with engine.connect() as con:
        result = con.execute(smt).fetchone()
        
    if result:
        return result.id_usuario
    
#%%
def check_password(password, hashed_password):
    result = bcrypt.checkpw(password.encode('utf8'), bytes(hashed_password.replace("b'", "").replace("'", ""), 'utf-8'))
    return result

#%%

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


#%%

check_login("hiago.gomes", "guilherme")

