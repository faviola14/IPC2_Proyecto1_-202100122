from NodoSimple2 import NodoS2

# It's a linked list with two data fields
class ListaSimpleEnlazada2:
    def __init__(self) -> None:
        self.primero = NodoS2()
        self.ultimo = NodoS2()

    def agregar(self, dato):
        if self.primero.codigoOrganismo is None:
            self.primero = dato
            self.ultimo = dato
        elif self.primero.siguiente is None:
            self.primero.siguiente = dato
            self.ultimo = dato
        else:
            self.ultimo.siguiente = dato
            self.ultimo = dato

    def print(self):

        nodoAux = self.primero
        cadena = ''
        while True:
            if nodoAux.codigoOrganismo is not None:
                cadena += "(" + nodoAux.fila + " " + nodoAux.columna +" " + nodoAux.codigoOrganismo + ")"

                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        
        print(cadena)

    def fila(self):
        nodoAux = self.primero
        cadena = ''
        while True:
            if nodoAux.fila is not None:
                return nodoAux.fila
            else:
                break
        print(cadena)