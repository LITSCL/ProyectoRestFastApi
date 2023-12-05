class ValidacionHelper:
    
    def validar_cadena(self, cadena: str) -> bool:
        try:
            if (len(cadena) > 0):
                return True
            else:
                return False
        except:
            return False