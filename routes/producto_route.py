from fastapi import APIRouter
from typing import List

from models.producto import Producto
from controllers.producto_controller import ProductoController

pc: ProductoController = ProductoController()

router: object = APIRouter()

router.add_api_route("/api/producto/save-producto", pc.save_producto, methods = ["POST"], response_model = str, tags = ["modelo_producto"])
router.add_api_route("/api/producto/get-productos", pc.get_productos, methods = ["GET"], response_model = List[Producto], tags = ["modelo_producto"])
router.add_api_route("/api/producto/get-producto/{key}", pc.get_producto, methods = ["GET"], response_model = Producto, tags = ["modelo_producto"])
router.add_api_route("/api/producto/update-producto/{key}", pc.update_producto, methods = ["PUT"], response_model = Producto, tags = ["modelo_producto"])
router.add_api_route("/api/producto/delete-producto/{key}", pc.delete_producto, methods = ["DELETE"], response_model = Producto, tags = ["modelo_producto"])

rutas_producto: object = router