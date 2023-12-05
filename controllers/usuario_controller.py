from fastapi import HTTPException

from config.database import DataBase
from models.usuario import Usuario, tabla_usuario
from helpers.validacion_helper import ValidacionHelper
from schemas.usuario_schema import objeto_schema, lista_schema

class UsuarioController:
    __db: object = DataBase().get_conexion()
    __query: object = None
    
    async def save_usuario(self, usuario: Usuario) -> int:
        validacion_email: bool = ValidacionHelper().validar_cadena(usuario.email)
        if (validacion_email == False):
            raise HTTPException(status_code = 400, detail = "SERVIDOR: Error de validación")
        usuario_obtenido: dict = dict(usuario)
        usuario_obtenido.pop("id")
        try:
            self.__query = self.__db.execute((tabla_usuario).insert().values(usuario_obtenido))
        except:
            raise HTTPException(status_code = 400, detail = "SERVIDOR: Ya existe un usuario con el email " + usuario_obtenido["email"])
        self.__db.commit()
        resultado: int = self.__query.inserted_primary_key[0]
        return resultado
    
    async def get_usuarios(self) -> list:
        self.__query = self.__db.execute((tabla_usuario).select()).fetchall()
        resultado: list = lista_schema(self.__query)
        return resultado
    
    async def get_usuario(self, key: int) -> dict:
        self.__query = self.__db.execute((tabla_usuario).select().where(key == tabla_usuario.c.id)).first()
        if (not self.__query):
            raise HTTPException(status_code = 404, detail = "SERVIDOR: No existe el usuario con el id " + str(key))
        resultado: dict = objeto_schema(self.__query)
        return resultado
    
    async def update_usuario(self, key: int, usuario: Usuario) -> dict:
        usuario_obtenido: dict = objeto_schema(usuario)
        self.__query = self.__db.execute((tabla_usuario).select().where(key == tabla_usuario.c.id)).first()
        if (not self.__query):
            raise HTTPException(status_code = 404, detail = "SERVIDOR: No existe el usuario con el id " + str(key))
        try:
            self.__query = self.__db.execute((tabla_usuario).update().values(usuario_obtenido).where(key == tabla_usuario.c.id))
        except:
            raise HTTPException(status_code = 500, detail = "SERVIDOR: Error al registrar el usuario")
        self.__query = self.__db.execute((tabla_usuario).select().where(key == tabla_usuario.c.id)).first()
        if (not self.__query):
            raise HTTPException(status_code = 404, detail = "SERVIDOR: Ocurrió un error al retornar la acualización del usuario con el id " + str(key))
        self.__db.commit()
        resultado: dict = objeto_schema(self.__query)
        return resultado
    
    async def delete_usuario(self, key: int) -> dict:
        self.__query = self.__db.execute((tabla_usuario).select().where(key == tabla_usuario.c.id)).first()
        if (not self.__query):
            raise HTTPException(status_code = 404, detail = "SERVIDOR: No existe el usuario con el id " + str(key))
        usuario_obtenido: dict = objeto_schema(self.__query)
        
        #Esto es un borrado lógico, simplemente se actualiza una columna del registro (Se esta actualizando la columna "estado").
        """
        usuario_obtenido["estado"] = False
        query = self.__db.execute((tabla_usuario).update().values(usuario_obtenido).where(key == tabla_usuario.c.id))
        query = self.__db.execute((tabla_usuario).select().where(key == tabla_usuario.c.id)).first()
        """
        
        try:
            self.__query = self.__db.execute((tabla_usuario).delete().where(key == tabla_usuario.c.id))
        except:
            raise HTTPException(status_code = 500, detail = "SERVIDOR: Error al eliminar el usuario")
        self.__db.commit()
        resultado: dict = usuario_obtenido
        return resultado
    
