from NodoSimple import NodoS
from NodoSimple import NodoS22
import xml.etree.ElementTree as ET
from xml.dom import minidom

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
                cadena += "("  + " "+ nodoAux.codigo + " " + nodoAux.nombre + " " + nodoAux.color+" )"

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
        while nodoAux.codigo != codigo:
            contador=contador+1
            if nodoAux.siguiente is not None:
                
                nodoAux = nodoAux.siguiente
            else:
                return None
        
        return True

    def color(self,codigo):
        nodoAux = self.primero
        contador=0
        while nodoAux.codigo != codigo:
            contador=contador+1
            if nodoAux.siguiente is not None:
                
                nodoAux = nodoAux.siguiente
            else:
                return None
        
        return nodoAux.color
    
    def xmlOrganismos(self):
        elemento_1 = ET.Element('datosMarte')
        elemento_2 = ET.SubElement(elemento_1, "listaOrganismos")
        
        actual=self.primero

        while actual != None:
            elemento_21 = ET.SubElement(elemento_2, "organismo")
            elemento_211 = ET.SubElement(elemento_21, "codigo")
            elemento_212 = ET.SubElement(elemento_21, "nombre")
            elemento_213 = ET.SubElement(elemento_21, "color")
            elemento_211.text=actual.codigo
            elemento_212.text=actual.nombre
            elemento_213.text=actual.color
            
            actual = actual.siguiente
        
        
        return elemento_1
        


##############################################################################
class ListaSimpleEnlazada22:
    def __init__(self) -> None:
        self.primero = NodoS22()
        self.ultimo = NodoS22()

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
                cadena += "(" + nodoAux.codigo + " " + nodoAux.descripcion +" "+ nodoAux.filas +" "+ nodoAux.columnas + " )"

                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        
        print(cadena)


    def CodigoMuestra(self):
        contador=0
        nodoAux = self.primero
        cadena = ''
        while True:
            if nodoAux.codigo is not None:
                contador=contador+1
                cadena += "| "+str(contador)+". " + nodoAux.codigo +", Descripción: "+ nodoAux.descripcion + " |"
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += "  "
                else:
                    break
            else:
                break
            
        print(cadena)

    def buscarMuestra(self, codigo):

        nodoAux = self.primero
        contador=0
        while str(nodoAux.codigo) != str(codigo):
            contador=contador+1
            if nodoAux.siguiente is not None:
                
                nodoAux = nodoAux.siguiente
            else:
                return None
        
        return True
    
    def m(self,nombre):
        
        nodoAux = self.primero
        contador=0
        while nodoAux.codigo != nombre:
            contador=contador+1
            
            if nodoAux.siguiente is not None:
                
                nodoAux = nodoAux.siguiente
            else:
                return None
        
        return int(nodoAux.filas)
    
    def n(self,nombre):
        
        nodoAux = self.primero
        contador=0
        while nodoAux.codigo != nombre:
            contador=contador+1
            
            if nodoAux.siguiente is not None:
                
                nodoAux = nodoAux.siguiente
            else:
                return None
        
        return int(nodoAux.columnas)
    
    
    def descripcion(self,nombre):
        
        nodoAux = self.primero
        contador="descripcion"
        while nodoAux.codigo != nombre:
            contador= nodoAux.descripcion
            
            if nodoAux.siguiente is not None:
                
                nodoAux = nodoAux.siguiente
            else:
                return None
        
        return nodoAux.descripcion
