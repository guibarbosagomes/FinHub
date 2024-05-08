#%%
import bcrypt
from sqlalchemy import insert
from bd.table import usuario, empresa
from bd.connect import engine


from datetime import datetime

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
def insert_usuario(nome_completo, nome_usuario, senha, email):

    stmt = insert(usuario).values(
                            nome_completo = nome_completo,
                            nome_usuario = nome_usuario,
                            senha = hash_password(senha),
                            email = email,
                            dt_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            )

    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()
        
    return True

# %%

def insert_empresa(cod_empresa, desc_empresa):
     
    stmt = insert(empresa).values(cod_empresa = cod_empresa,
                                desc_empresa = desc_empresa
                            )


    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()
        
    return True
# %%