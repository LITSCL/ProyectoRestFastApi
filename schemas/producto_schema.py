from typing import List

from models.producto import Producto

def schema(producto: Producto) -> dict:
    return {
        "codigo": producto.codigo,
        "nombre": producto.nombre,
        "precio": producto.precio,
    }

def objeto_schema(producto: Producto) -> dict:
    return schema(producto)
    
def lista_schema(productos: List[Producto]) -> list:
    return [schema(producto) for producto in productos]