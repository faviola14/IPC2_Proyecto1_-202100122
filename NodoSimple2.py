
class NodoS2:
    def __init__(self, fila= None, columna = None, codigoOrganismo = None, muestra =None) -> None:
        self.fila=fila 
        self.columna = columna
        self.codigoOrganismo = codigoOrganismo
        self.muestra = muestra
        self.siguiente = None
        