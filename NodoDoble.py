class NodoD:
    def __init__(self, nombre = None,x = None,y = None, dato = None, color = None) -> None:
        self.dato =dato
        self.x =x
        self.y =y
        self.nombre = nombre
        self.color = color
        self.siguiente = None
        self.anterior = None