#%%
#%%
import random
import string

import bcrypt
from sqlalchemy import insert
from bd.table import usuario, empresa, recuperacao_senha
from bd.connect import engine
from envio_email.enviar_email import enviar_email_registro

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
def insert_usuario(nome_completo, dt_nascimento, nome_usuario, senha, email):

    stmt = insert(usuario).values(
                            nome_completo = nome_completo,
                            dt_nascimento = dt_nascimento,
                            nome_usuario = nome_usuario,
                            senha = hash_password(senha),
                            email = email,
                            dt_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            )

    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()
        ## Envio de email apos inclusão no banco
        enviar_email_registro(email, nome_completo, dt_nascimento, nome_usuario, email, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
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


def generate_random_code(length=5):
    ## Função que gera informações randomicas do codigo secreto

    # Definir os caracteres possíveis (números e letras maiúsculas e minúsculas)
    characters = string.ascii_letters + string.digits
    # Gerar um código aleatório de 6 dígitos
    random_code = ''.join(random.choices(characters, k=length))
    return random_code



def insert_recuperar_senha(id_usuario):
    # Cria uma linha na tabela de recuperação de senha e gera um codigo secreto que vai ser enviado por email na solicitação
    codigo_secreto = generate_random_code()

    stmt = insert(recuperacao_senha).values(id_usuario = id_usuario,
                                            cod_secreto = codigo_secreto,
                                            status = True,
                                            dt_solicitacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            )
    
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

        return codigo_secreto
    
    return False


# %%