# Scripts para inicializar tabelas no banco
# Para rodar o script remova o arquivo select da pasta bd
#%%
from connect_local import engine
from table import usuario, empresa, meta_obj


#%%
print(">>CREATE DATABASE")
meta_obj.create_all( bind = engine )


# %%
