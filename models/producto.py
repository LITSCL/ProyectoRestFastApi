from pydantic import BaseModel
from sqlalchemy import Table, Column, MetaData
from sqlalchemy.sql.sqltypes import Double, String

from config.database import DataBase

db: object = DataBase().get_conexion()
md: object = MetaData()

class Producto(BaseModel):
    codigo: str = None
    nombre: str = None
    precio: float = None

tabla_producto: object = Table("producto", md,
    Column("codigo", String(45), primary_key = True),
    Column("nombre", String(45)),
    Column("precio", Double)
)

md.create_all(db)