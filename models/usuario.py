from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Table, Column, MetaData
from sqlalchemy.sql.sqltypes import Integer, String, Boolean

from config.database import DataBase

db: object = DataBase().get_conexion()
md: object = MetaData()

class Usuario(BaseModel):
    id: Optional[int] = None
    nombre: str = None
    email: str = None
    estado: bool = None

tabla_usuario: object = Table("usuario", md,
    Column("id", Integer, primary_key = True),
    Column("nombre", String(45)),
    Column("email", String(45)),
    Column("estado", Boolean)
)

md.create_all(db)