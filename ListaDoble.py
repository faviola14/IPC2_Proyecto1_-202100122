from NodoDoble import NodoD
import os

# It creates a double linked list, and it has a method to print the list, a method to check if a node
# exists, and a method to create a graph of the list.
class ListaDoble:
    def __init__(self) -> None:
        self.primero = NodoD()
        self.ultimo = NodoD()

    
    def agregar(self, dato):

        if self.primero.dato is None:
            self.primero = dato
            self.ultimo = dato
        elif self.primero.siguiente is None:
            self.primero.siguiente = dato
            dato.anterior = self.primero
            self.ultimo = dato
        else:
            self.ultimo.siguiente = dato
            dato.anterior = self.ultimo
            self.ultimo = dato


    def print(self):

        nodoAux = self.primero
        cadena = ''
        while True:
            if nodoAux.dato is not None:
                cadena += "(" + str(nodoAux.x) + " " + str(nodoAux.y) + " " + str(nodoAux.dato) +  ")"
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        print(cadena)     


    def Existe(self,x,y):

        contador=0
        nodoAux = self.primero
        while True:
            if nodoAux.dato is not None:
                
                if nodoAux.x ==str(x) and nodoAux.y == str(y):
                    contador =1
                
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                else:
                    break
            else:
                break
        return contador

    def graficar(self):

        aux = self.primero
        contador = 0
        cadena = ""
        file = open("grafica2.dot", "w")
        cadena = cadena + "digraph G{ \n"
        while(aux!=None):
            cadena = cadena + "Node"+str(contador)+"[label=\""+str(aux.dato)+"\"];\n"
            if(aux!=self.primero):
                cadena = cadena + "Node"+str(contador-1)+" -> Node"+str(contador)+";\n"
                cadena = cadena + "Node"+str(contador)+" -> Node"+str(contador-1)+";\n"
            aux = aux.siguiente
            contador = contador + 1
        cadena = cadena + "}"
        file.write(cadena)
        file.close()
        os.system('dot -Tpng grafica2.dot -o grafica2.png')