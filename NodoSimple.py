
class NodoS:
    def __init__(self, codigo = None, nombre = None, color=None) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.color = color
        self.siguiente = None

class NodoS22:
    def __init__(self,codigo = None, descripcion = None, filas = None, columnas = None) -> None:
        self.codigo= codigo
        self.descripcion = descripcion
        self.filas = filas
        self.columnas = columnas

        self.siguiente = None