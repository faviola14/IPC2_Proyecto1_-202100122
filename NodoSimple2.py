from ListaSimple import ListaSimpleEnlazada
class NodoS2:
    def __init__(self, periodos= None, m = None) -> None:
        self.datos= ListaSimpleEnlazada()
        self.periodos = periodos
        self.m = m
        self.siguiente = None
        self.rejilla = ListaSimpleEnlazada()