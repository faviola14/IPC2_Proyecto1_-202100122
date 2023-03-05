from NodoEncabezado import NodoEncabezado

class ListaEncabezado:
    def __init__(self, tipo = None) -> None:
        self.tipo = tipo
        self.primero: NodoEncabezado = None
        self.ultimo: NodoEncabezado = None
        self.size = 0

    
    def insertarEncabezado(self, nuevoEncabezado: NodoEncabezado):
        self.size += 1
        if self.primero == None:
            self.primero = nuevoEncabezado
            self.ultimo = nuevoEncabezado
        else:

            if nuevoEncabezado.dato < self.primero.dato:
                nuevoEncabezado.siguiente = self.primero
                self.primero.anterior = nuevoEncabezado
                self.primero = nuevoEncabezado
            elif nuevoEncabezado.dato > self.ultimo.dato:
                self.ultimo.siguiente = nuevoEncabezado
                nuevoEncabezado.anterior = self.ultimo
                self.ultimo = nuevoEncabezado
            else:
                aux = self.primero

                while aux != None:                   
                    if nuevoEncabezado.dato < aux.dato:
                        nuevoEncabezado.siguiente = aux
                        nuevoEncabezado.anterior = aux.anterior
                        aux.anterior.siguiente = nuevoEncabezado
                        aux.anterior = nuevoEncabezado
                        break
                    elif nuevoEncabezado.dato > aux.dato:
                        aux = aux.siguiente
                    else:
                        break

    def mostrarEncabezado(self): 
        aux = self.primero
        while aux != None:
            print("Encabezado de {0} en posicion {1}".format(self.tipo, aux.dato))
            aux = aux.siguiente

    def getEncabezado(self, dato):
        aux = self.primero
        while aux != None:
            if dato == aux.dato:
                return aux
            aux =  aux.siguiente
        return None
()


