class NodoCeldas:
    def __init__(self, fila = None, col = None, dato = None, organismo=None) -> None:
        self.fila = fila
        self.col = col
        self.dato = dato
        self.organismo = organismo
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None
        