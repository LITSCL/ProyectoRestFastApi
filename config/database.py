from sqlalchemy import create_engine

class DataBase:
    __conexion: object = create_engine("mysql+pymysql://root:root@localhost:3306/dbproyectorestfastapi").connect()
    
    def get_conexion(self) -> object:
        return self.__conexion
