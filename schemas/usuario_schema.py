from typing import List

from models.usuario import Usuario

def schema(usuario: Usuario) -> dict:
    return {
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email,
        "estado": usuario.estado
    }

def objeto_schema(usuario: Usuario) -> dict:
    return schema(usuario)
    
def lista_schema(usuarios: List[Usuario]) -> list:
    return [schema(usuario) for usuario in usuarios]