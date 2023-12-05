from fastapi import HTTPException

from config.database import DataBase
from models.producto import Producto, tabla_producto
from helpers.validacion_helper import ValidacionHelper
from schemas.producto_schema import objeto_schema, lista_schema

class ProductoController:
    __db: object = DataBase().get_conexion()
    __query: object = None
    
    async def save_producto(self, producto: Producto) -> str:
        validacion_codigo: bool = ValidacionHelper().validar_cadena(producto.codigo)
        if (validacion_codigo == False):
            raise HTTPException(status_code = 400, detail = "SERVIDOR: Error de validación")
        producto_obtenido: dict = dict(producto)
        try:
            self.__query = self.__db.execute((tabla_producto).insert().values(producto_obtenido))
        except:
            raise HTTPException(status_code = 500, detail = "SERVIDOR: Error al registrar el producto")
        self.__db.commit()
        resultado: str = self.__query.inserted_primary_key[0]
        return resultado
    
    async def get_productos(self) -> list:
        self.__query = self.__db.execute((tabla_producto).select()).fetchall()
        resultado: list = lista_schema(self.__query)
        return resultado
    
    async def get_producto(self, key: str) -> dict:
        self.__query = self.__db.execute((tabla_producto).select().where(key == tabla_producto.c.codigo)).first()
        if (not self.__query):
            raise HTTPException(status_code = 404, detail = "SERVIDOR: No existe el producto con el codigo " + key)
        resultado: dict = objeto_schema(self.__query)
        return resultado
    
    async def update_producto(self, key: str, producto: Producto) -> dict:
        producto_obtenido: dict = objeto_schema(producto)
        self.__query = self.__db.execute((tabla_producto).select().where(key == tabla_producto.c.codigo)).first()
        if (not self.__query):
            raise HTTPException(status_code = 404, detail = "SERVIDOR: No existe el producto con el codigo " + key)
        try:
            self.__query = self.__db.execute((tabla_producto).update().values(producto_obtenido).where(key == tabla_producto.c.codigo))
        except:
            raise HTTPException(status_code = 500, detail = "SERVIDOR: Error al registrar el producto")
        self.__query = self.__db.execute((tabla_producto).select().where(key == tabla_producto.c.codigo)).first()
        if (not self.__query):
            raise HTTPException(status_code = 404, detail = "SERVIDOR: Ocurrió un error al retornar la acualización del producto con el codigo " + key)
        self.__db.commit()
        resultado: dict = objeto_schema(self.__query)
        return resultado
    
    async def delete_producto(self, key: str) -> dict:
        self.__query = self.__db.execute((tabla_producto).select().where(key == tabla_producto.c.codigo)).first()
        if (not self.__query):
            raise HTTPException(status_code = 404, detail = "SERVIDOR: No existe el producto con el codigo " + key)
        producto_obtenido: dict = objeto_schema(self.__query)
        try:
            self.__query = self.__db.execute((tabla_producto).delete().where(key == tabla_producto.c.codigo))
        except:
            raise HTTPException(status_code = 500, detail = "SERVIDOR: Error al eliminar el producto")
        self.__db.commit()
        resultado: dict = producto_obtenido
        return resultado
    
