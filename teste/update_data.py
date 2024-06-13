#%%
import random
import string

import bcrypt
from sqlalchemy import insert, update
from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, Text, Boolean, Date

from connect import engine

from datetime import datetime

meta_obj = MetaData()

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

def hash_password(password):
   password_bytes = password.encode('utf-8')
   hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
   return hashed_password


#%%
def check_password(password, hashed_password):
    result = bcrypt.checkpw(password.encode('utf8'), bytes(hashed_password.replace("b'", "").replace("'", ""), 'utf-8'))
    return result


#%%
def update_senha(id_usuario, senha):

    stmt = update(usuario).values(
                            senha = hash_password(senha),
                            ).where(
                                usuario.c.id == id_usuario
                            )

    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

        return True
    
    return False

# %%

update_senha(3, "guilherme")

#%%
