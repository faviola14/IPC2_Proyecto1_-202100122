from NodoSimple2 import NodoS2
import xml.etree.ElementTree as ET
from xml.dom import minidom

# It's a linked list with two data fields
class ListaSimpleEnlazada2:
    def __init__(self) -> None:
        self.primero = NodoS2()
        #self.ultimo = NodoS2()

    
    '''def agregar(self, nuevoNodo):
        
        if self.primero==None:
            self.primero == nuevoNodo
            self.ultimo = nuevoNodo
            return
        
        nodoTmp= self.primero
        
        while nodoTmp.siguiente !=None:
            nodoTmp =nodoTmp.siguiente
            
        nodoTmp.siguiente = nuevoNodo'''
        
    '''def agregar(self, dato):
        if self.primero is None:
            self.primero = dato
            return 
        actual = self.primero 
        while actual.siguiente:
            actual= actual.siguiente
        actual.siguiente= dato'''
        
        
        
    '''def agregar(self, data):
        new_node = data
        
        if self.primero is None:
            self.primero = new_node
            return

        last_node = self.primero
        while last_node.siguiente is not None:
            last_node = last_node.siguiente

        last_node.siguiente = new_node'''
    

    def agregar(self, dato):
        if self.primero is None:
            self.primero = dato
            self.ultimo = dato
            
        elif self.primero.siguiente is None:
            self.primero.siguiente = dato
            self.ultimo = dato
        else:
            self.ultimo.siguiente = dato
            self.ultimo = dato
    
        

    '''def print(self):

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
        
        print(cadena)'''
        


    def print(self):
        actual=self.primero

        while actual != None:
            print ('({}  {}  {} {} {} ) -> '.format(actual.fila, actual.columna,actual.codigoOrganismo, actual.color, actual.muestra),end="")
            actual = actual.siguiente
            


    def fila(self):
        nodoAux = self.primero
        cadena = ''
        while True:
            if nodoAux.fila is not None:
                return nodoAux.fila
            else:
                break
        print(cadena)
    
    def organismo(self, x,y):
        contador="hola"
        if self.primero is None:
            return contador
        
        if str(self.primero.fila) == str(x) and self.primero.columna == str(y):
            contador =str(self.primero.codigoOrganismo)
            return contador

        prev_node = self.primero
        curr_node = self.primero.siguiente
        while curr_node is not None:
            if curr_node.fila == str(x) and curr_node.columna == str(y):
                contador =str(curr_node.codigoOrganismo)

                return contador
            prev_node = curr_node
            curr_node = curr_node.siguiente
            
        return contador
    
    
    
    
    '''def organismo(self,fila, columna):
        contador="hola"
        nodoAux = self.primero
        while True:
            if nodoAux.fila is not None:
                
                if nodoAux.fila ==str(fila)  and nodoAux.columna == str(columna):
                    contador =str(nodoAux.codigoOrganismo)
                
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                else:
                    break
            else:
                break
        return contador'''
    
    '''def Existe(self,x,y):

        contador=0
        nodoAux = self.primero
        while True:
            if nodoAux.fila is not None:
                
                if nodoAux.fila ==str(x) and nodoAux.columna == str(y):
                    contador =1
                
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                else:
                    break
            else:
                break
        return contador'''

    def Existe(self, x,y):
        contador=0
        if self.primero is None:
            return contador
        
        if self.primero.fila == str(x) and self.primero.columna == str(y):
            contador =1
            return contador

        prev_node = self.primero
        curr_node = self.primero.siguiente
        while curr_node is not None:
            if curr_node.fila == str(x) and curr_node.columna == str(y):
                contador =1

                return contador
            prev_node = curr_node
            curr_node = curr_node.siguiente
            
        return contador



    def color(self, x,y):
        contador="hola"
        if self.primero is None:
            return contador
        
        if self.primero.fila == str(x) and self.primero.columna == str(y):
            contador =str(self.primero.color)
            return contador

        prev_node = self.primero
        curr_node = self.primero.siguiente
        while curr_node is not None:
            if curr_node.fila == str(x) and curr_node.columna == str(y):
                contador =str(curr_node.color)

                return contador
            prev_node = curr_node
            curr_node = curr_node.siguiente
            
        return contador
    
    
    '''def color(self,fila, columna):
        contador="hola"
        nodoAux = self.primero
        while True:
            if nodoAux.fila is not None:
                
                if nodoAux.fila ==str(fila)  and nodoAux.columna == str(columna):
                    contador =str(nodoAux.color)
                
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                else:
                    break
            else:
                break
        return contador'''
    
    '''def eliminar(self,x, y):
        actual =self.primero
        anterior=None

        while actual and actual.fila == str(x) and actual.columna == str(y):
            anterior=actual
            actual=actual.siguiente

        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None'''
    
    '''def eliminar(self, x, y):
        aux1 = self.primero
        aux2 = None
        while(aux1!=None):
            if(aux1.fila == str(x) and aux1.columna == str(y)):
                if(aux1 == self.primero):
                    aux1 = aux1.siguiente
                    ##self.cabecera = self.cabecera.siguiente
                    break;
                elif(aux1.siguiente == None):
                    aux2.siguiente = None
                else:
                    aux2.siguiente = aux1.siguiente
                    aux1.siguiente = None
                    break;
            else:
                aux2 = aux1
                aux1 = aux1.siguiente'''
                
    def eliminar(self, x,y):
        
        if self.primero is None:
            return

        
        if self.primero.fila == str(x) and self.primero.columna == str(y):
            self.primero= self.primero.siguiente
            return

        
        prev_node = self.primero
        curr_node = self.primero.siguiente
        while curr_node is not None:
            if curr_node.fila == str(x) and curr_node.columna == str(y):
                prev_node.siguiente = curr_node.siguiente
                return
            prev_node = curr_node
            curr_node = curr_node.siguiente

        return


    def xmlMuestras(self,muestra,descripcion,m,n):
        elemento_1 = ET.Element('datosMarte')
        elemento_3 = ET.SubElement(elemento_1, "listaMuestras")
        elemento_31 = ET.SubElement(elemento_3, "muestra")
        elemento_311 = ET.SubElement(elemento_31, "codigo")
        elemento_312 = ET.SubElement(elemento_31, "descripcion")
        elemento_313 = ET.SubElement(elemento_31, "filas")
        elemento_314 = ET.SubElement(elemento_31, "columnas")
        
        elemento_311.text=muestra
        elemento_312.text=descripcion
        elemento_313.text=m
        elemento_314.text=n
        
        elemento_3141 = ET.SubElement(elemento_314, "listadoCeldasVivas")
        
        actual=self.primero

        while actual != None:
            elemento_31411 = ET.SubElement(elemento_3141, "celdaViva")
            elemento_314111 = ET.SubElement(elemento_31411, "fila")
            elemento_314112 = ET.SubElement(elemento_31411, "columna")
            elemento_314113 = ET.SubElement(elemento_31411, "codigoOrganismo")
            
            elemento_314111.text =str(actual.fila)
            elemento_314112.text =str(actual.columna)
            elemento_314113.text =str(actual.codigoOrganismo)
            
            actual = actual.siguiente
        
        return elemento_1