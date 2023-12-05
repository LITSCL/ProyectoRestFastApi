from fastapi import APIRouter
from typing import List

from models.usuario import Usuario
from controllers.usuario_controller import UsuarioController

uc: UsuarioController = UsuarioController()

router: object = APIRouter()

router.add_api_route("/api/usuario/save-usuario", uc.save_usuario, methods = ["POST"], response_model = int, tags = ["modelo_usuario"])
router.add_api_route("/api/usuario/get-usuarios", uc.get_usuarios, methods = ["GET"], response_model = List[Usuario], tags = ["modelo_usuario"])
router.add_api_route("/api/usuario/get-usuario/{key}", uc.get_usuario, methods = ["GET"], response_model = Usuario, tags = ["modelo_usuario"])
router.add_api_route("/api/usuario/update-usuario/{key}", uc.update_usuario, methods = ["PUT"], response_model = Usuario, tags = ["modelo_usuario"])
router.add_api_route("/api/usuario/delete-usuario/{key}", uc.delete_usuario, methods = ["DELETE"], response_model = Usuario, tags = ["modelo_usuario"])

rutas_usuario: object = router