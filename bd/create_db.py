#%%
from connect import engine
from table import usuario, empresa, meta_obj


#%%
print(">>CREATE DATABASE")
meta_obj.create_all( bind = engine )


# %%
