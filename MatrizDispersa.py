from NodoEncabezado import NodoEncabezado
from ListaEncabezado import ListaEncabezado
from NodoCeldas import NodoCeldas
import os

# This class represents a sparse matrix.
class MatrizDispersa:
    def __init__(self) -> None:
        self.capa = 0
        self.filas = ListaEncabezado("FILAS")
        self.columnas = ListaEncabezado("COLUMNAS")

    def insertar(self, nodoCeldas: NodoCeldas):
        encabezadoFila = self.filas.getEncabezado(nodoCeldas.fila)
        encabezadoCol = self.columnas.getEncabezado(nodoCeldas.col)

        if encabezadoFila == None:
            encabezadoFila = NodoEncabezado(nodoCeldas.fila)
            self.filas.insertarEncabezado(encabezadoFila)
        if encabezadoCol == None:
            encabezadoCol = NodoEncabezado(nodoCeldas.col)
            self.columnas.insertarEncabezado(encabezadoCol)
        


        if encabezadoFila.acceso == None:
            encabezadoFila.acceso = nodoCeldas
        else:
            aux = encabezadoFila.acceso

            while aux != None:
                if nodoCeldas.col < aux.col:
                    nodoCeldas.derecha = aux
                    nodoCeldas.izquierda = aux.izquierda
                    aux.izquierda.derecha = nodoCeldas
                    aux.izquierda = nodoCeldas
                    break
                else:
                    if aux.derecha == None:
                        aux.derecha = nodoCeldas
                        nodoCeldas.izquierda = aux
                        break
                    else:
                        aux = aux.derecha



        if encabezadoCol.acceso == None:
            encabezadoCol.acceso = nodoCeldas
        else:

            if nodoCeldas.fila < encabezadoCol.acceso.fila:
                nodoCeldas.abajo = encabezadoCol.acceso
                encabezadoCol.acceso.arriba = nodoCeldas
                encabezadoCol.acceso = nodoCeldas
            else:
                aux2 = encabezadoCol.acceso

                while aux2 != None:
                    if nodoCeldas.fila < aux2.fila:
                        nodoCeldas.abajo = aux2
                        nodoCeldas.arriba = aux.arriba
                        aux2.arriba.abajo = nodoCeldas
                        aux2.arriba = nodoCeldas
                        break
                    else:
                        if aux2.abajo == None:
                            aux2.abajo = nodoCeldas
                            nodoCeldas.arriba = aux2
                            break
                        else:
                            aux2 = aux2.abajo

    def graficarDot(self, nombre,muestra):
        """
        It creates a .txt file with the graphviz code, then it converts it to a .pdf file.
        I'm trying to make a function that does the same thing, but with a graphviz object instead of a
        .txt file.
        I've tried this:
        <code>def graficarDot(self, nombre,muestra):
                
                grafo = 'digraph T{ \nnode[shape=box fontname="Arial" fillcolor="white" style=filled ]'
                grafo += '\nroot[label = \"Dato: '+ str(self.capa) +'\", group=1]\n'
                grafo += '''label = "{}" \nfontname="Arial Black" \nfontsize="15pt" \n
                            \n'''.format(muestra)
        
        :param nombre: name of the file
        :param muestra: the name of the graph
        """
        
        grafo = 'digraph T{ \nnode[shape=box fontname="Arial" fillcolor="white" style=filled ]'
        grafo += '\nroot[label = \"Dato: '+ str(self.capa) +'\", group=1]\n'
        grafo += '''label = "{}" \nfontname="Arial Black" \nfontsize="15pt" \n
                    \n'''.format(muestra)

        
        x_fila = self.filas.primero
        while x_fila != None:
            grafo += 'F{}[label="F{}",fillcolor="plum",group=1];\n'.format(x_fila.dato, x_fila.dato)
            x_fila = x_fila.siguiente

        
        x_fila = self.filas.primero
        while x_fila != None:
            if x_fila.siguiente != None:
                grafo += 'F{}->F{};\n'.format(x_fila.dato, x_fila.siguiente.dato)
                grafo += 'F{}->F{};\n'.format(x_fila.siguiente.dato, x_fila.dato)
            x_fila = x_fila.siguiente

        
        y_columna = self.columnas.primero
        while y_columna != None:
            group = int(y_columna.dato)+1
            grafo += 'C{}[label="C{}",fillcolor="powderblue",group={}];\n'.format(y_columna.dato, y_columna.dato, str(group))
            y_columna = y_columna.siguiente
        

        cont = 0
        y_columna = self.columnas.primero
        while y_columna is not None:
            if y_columna.siguiente is not None:
                grafo += 'C{}->C{}\n'.format(y_columna.dato, y_columna.siguiente.dato)
                grafo += 'C{}->C{}\n'.format(y_columna.siguiente.dato, y_columna.dato)
            cont += 1
            y_columna = y_columna.siguiente

        
        y_columna = self.columnas.primero
        x_fila = self.filas.primero
        grafo += 'root->F{};\n root->C{};\n'.format(x_fila.dato, y_columna.dato)
        grafo += '{rank=same;root;'
        cont = 0
        y_columna = self.columnas.primero
        while y_columna != None:
            grafo += 'C{};'.format(y_columna.dato)
            cont += 1
            y_columna = y_columna.siguiente
        grafo += '}\n'
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        while aux != None:
            cont += 1
            while aux2 != None:
                
                if aux2.dato != None:
                    color=aux2.dato
                    color=color.replace("\"\"","")
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="{}"];\n'.format(aux2.fila, aux2.col, aux2.organismo, int(aux2.col)+1,color)          
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        while aux is not None:
            rank = '{'+f'rank = same;F{aux.dato};' 
            cont = 0
            while aux2 != None:
                if cont == 0:
                    grafo += 'F{}->N{}_{};\n'.format(aux.dato, aux2.fila, aux2.col)
                    grafo += 'N{}_{}->F{};\n'.format(aux2.fila, aux2.col, aux.dato)
                    cont += 1
                if aux2.derecha != None:
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.fila, aux2.col, aux2.derecha.fila, aux2.derecha.col)
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.derecha.fila, aux2.derecha.col, aux2.fila, aux2.col)

                rank += 'N{}_{};'.format(aux2.fila, aux2.col)
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
            grafo += rank+'}\n'
        aux = self.columnas.primero
        aux2 = aux.acceso
        cont = 0
        while aux != None:
            cont = 0
            grafo += ''
            while aux2 != None:
                if cont == 0:
                    grafo += 'C{}->N{}_{};\n'.format(aux.dato, aux2.fila, aux2.col)
                    grafo += 'N{}_{}->C{};\n'.format(aux2.fila, aux2.col, aux.dato) 
                    cont += 1
                if aux2.abajo != None:
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.abajo.fila, aux2.abajo.col, aux2.fila, aux2.col)
                    grafo += 'N{}_{}->N{}_{};\n'.format( aux2.fila, aux2.col,aux2.abajo.fila, aux2.abajo.col)
                aux2 = aux2.abajo
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        grafo += '}'


        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as f:
            f.write(grafo)
        result = "matriz_{}.pdf".format(nombre)
        os.system("dot -Tpdf " + dot + " -o " + result)