class NodoEncabezado:
    def __init__(self, dato = None) -> None:
        self.dato = dato
        self.siguiente = None
        self.anterior = None
        self.acceso = None