#%%
import random
import string

import bcrypt
from sqlalchemy import insert, update
from bd.table import usuario, empresa, recuperacao_senha
from bd.insert_data import hash_password
from bd.connect import engine
from envio_email.enviar_email import enviar_email_registro

from datetime import datetime


#%%
def update_senha(id_usuario, senha):
    # Função que atualiza senha no banco
    
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

def update_status_recuperar_senha(codigo):

    stmt = update(recuperacao_senha).values(
                            status = False,
                            dt_alteracao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            ).where(
                                recuperacao_senha.c.cod_secreto == codigo
                            )

    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

        return True
    
    return False
    