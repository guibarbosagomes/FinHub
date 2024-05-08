#%%
import os
from sqlalchemy import create_engine, text, URL
from dotenv import load_dotenv

#%%

load_dotenv()

#%%
url_object = URL.create(
    drivername=os.getenv('DB_DRIVE'),
    username=os.getenv('DB_USERNAME'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_DATABASE')
)

#%%
engine = create_engine(url_object, echo = True)
