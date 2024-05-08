from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, Text

meta_obj = MetaData()


usuario = Table(
    "usuario",
    meta_obj,
    Column("id", Integer, primary_key = True, autoincrement = True),
    Column("cod_empresa", String(30), nullable = False ),
    Column("nome", String(30), nullable = False ),
    Column("usuario", Text, nullable = False),
    Column("email", String(30), nullable = False),
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
