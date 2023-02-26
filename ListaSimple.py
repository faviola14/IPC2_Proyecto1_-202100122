from NodoSimple import NodoS

# It's a linked list of nodes, where each node is a linked list of data.
class ListaSimpleEnlazada:
    def __init__(self) -> None:
        self.primero = NodoS()
        self.ultimo = NodoS()

    def agregar(self, dato):

        if self.primero.codigo is None:
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
            if nodoAux.codigo is not None:
                cadena += "(" + nodoAux.codigo + " " + nodoAux.nombre + ")"

                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        
        print(cadena)


    def NombreOrganismos(self):
        contador=0
        nodoAux = self.primero
        cadena = ''
        while True:
            if nodoAux.codigo is not None:
                contador=contador+1
                cadena += "| "+str(contador)+". " + nodoAux.nombre +", Código: "+ nodoAux.codigo + " |"
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += "  "
                else:
                    break
            else:
                break
            
        print(cadena)

    def buscarOrganismo(self, codigo):

        nodoAux = self.primero
        contador=0
        while nodoAux.datos.primero.codigo != codigo:
            contador=contador+1
            if nodoAux.siguiente is not None:
                
                nodoAux = nodoAux.siguiente
            else:
                return None
        
        return True

    def m(self,codigo):
        nodoAux = self.primero
        contador=0
        while nodoAux.datos.primero.codigo != codigo:
            contador=contador+1
            if nodoAux.siguiente is not None:
                
                nodoAux = nodoAux.siguiente
            else:
                return None
        
        return nodoAux.nombre