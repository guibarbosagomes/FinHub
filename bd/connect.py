#%%
import os
from sqlalchemy import create_engine, text, URL
from dotenv import load_dotenv

#%%

load_dotenv("../Env/.env")


#%%
engine = create_engine(os.getenv("DB_DIALECT") + "FINHUB", echo = True)
