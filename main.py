import xml.etree.ElementTree as ET
from colorama import Fore
from tkinter import filedialog
from ListaSimple import ListaSimpleEnlazada
from ListaSimple2 import ListaSimpleEnlazada2
from ListaSimple import ListaSimpleEnlazada22
from ListaDoble import ListaDoble
from NodoDoble import  NodoD
from NodoSimple import  NodoS
from NodoSimple import  NodoS22
from NodoSimple2 import  NodoS2
from NodoCeldas import NodoCeldas
from MatrizDispersa import MatrizDispersa

muestra=""
listaOrganismos=ListaSimpleEnlazada()
listaMuestras=ListaSimpleEnlazada22()
celdasVivas=ListaSimpleEnlazada2()
rejilla=ListaDoble()
menu=0
filename1=""

#INICIO DEL PROGRAMA
def Inicio(listaO,listaM,menu,filename1,vivas,rejilla1,muestra):
    muestra=muestra
    
    listaOrganismos=ListaSimpleEnlazada()
    listaOrganismos=listaO
    listaMuestras=ListaSimpleEnlazada22()
    listaMuestras=listaM
    rejilla=ListaDoble()
    rejilla=rejilla1
    menu = menu
    
    celdasVivas=ListaSimpleEnlazada2()
    celdasVivas=vivas
    
    if menu==0:
    
        print(Fore.BLUE + "-----------------INICIO---------------")
        print(Fore.BLUE + "Elija su Archivo XML")
        
        
        filename1 = filedialog.askopenfilename(initialdir = "/", title = "Seleccione un Archivo XML", filetypes = (("XML files", "*.xml*"), ("All files", "*.*")))
        print(Fore.BLUE + filename1)
        listaOrganismos = cargarArchivo(filename1,muestra)
        #Inicio(listaOrganismos,listaMuestras,1,filename1,celdasVivas,rejilla,muestra)
        
    
    if menu==1:
        #listaOrganismos.print()
        #listaMuestras.print()
        print(Fore.RED +  "--------------ORGANISMOS---------------")
        #listaOrganismos.NombreOrganismos()
        #organismo = input(Fore.YELLOW + "Ingrese código del Organismo que desea Analizar\n")
        #if listaOrganismos.buscarOrganismo(organismo): 
        listaMuestras.CodigoMuestra()
        muestra = input(Fore.YELLOW + "Ingrese código de la Muestra que desea Analizar\n")
        if listaMuestras.buscarMuestra(muestra):
            celdasVivas = cargarVivas(filename1,muestra,listaOrganismos)
            celdasVivas.print()
            Inicio(listaOrganismos,listaMuestras,2,filename1,celdasVivas,rejilla,muestra)
        else:
            print(Fore.RED +  "El código ingresado no corresponde a ninguna muestra registrada")
            Inicio(listaOrganismos,listaMuestras,1,filename1,celdasVivas,rejilla,muestra)
        #else: 
        #    print(Fore.RED +  "El código ingresado no corresponde a ningún organismo registrado")
        #    Inicio(listaOrganismos,listaMuestras,1,filename1,celdasVivas,muestra)
    if menu==2:
        print(Fore.RED +  "--------------OPCIONES---------------")
        print(Fore.RED+  "1. Ver Rejilla inicial")
        print(Fore.RED+ "2. Generar Simulación")
        opc = input(Fore.YELLOW + "Seleccione una opción\n")
        if opc=='1' :
            print(Fore.BLUE+"-----------------------------------------------------------------------")
            rejilla=generarRejilla(celdasVivas, listaOrganismos,muestra,listaMuestras) 
            print("-----------------------------------------------------------------------")
            Inicio(listaOrganismos,listaMuestras,2,filename1,celdasVivas,rejilla,muestra)
        elif  opc=='2':
            print("---2---")
            
        else:
            print(Fore.RED +  "No es una opción correcta")
    




#CARGA DE ARCHIVO
def cargarArchivo(filename1,muestra):
    
    tree = ET.parse(filename1)
    organismos = tree.getroot()
    organismosLista = ListaSimpleEnlazada()
    muestras=ListaSimpleEnlazada22()
    celdasVivas=ListaSimpleEnlazada2()
    rejilla=ListaDoble()
    contador=0
    for organismo in organismos:
        contador=contador+1
        for datoP in organismo.iter('organismo'):
            nuevoOrganismo = NodoS(datoP.find('codigo').text, datoP.find('nombre').text,datoP.find('color').text)
            organismosLista.agregar(nuevoOrganismo)
            
    for organismo in organismos:
        
        for datoP1 in organismo.iter('muestra'):
            codigo=datoP1.find('codigo').text
            descripcion=datoP1.find('descripcion').text
            filas=datoP1.find('filas').text
            columnas=datoP1.find('columnas').text

            
            nuevaMuestra=NodoS22(codigo,descripcion,filas,columnas)
            muestras.agregar(nuevaMuestra)
            
    print(Fore.GREEN +  "Organismo agregado con éxito, Muestras Agregadas con éxito")
    Inicio(organismosLista,muestras,1,filename1,celdasVivas,rejilla,muestra)



#GENERAR Muestra
def generarRejilla(celdasVivasL, listaO,muestra,muestrasL):
    libres =0
    ocupadas=0
    rejilla=ListaDoble()
    celdasVivas=ListaSimpleEnlazada2()
    celdasVivas=celdasVivasL
    muestras=ListaSimpleEnlazada22()
    muestras=muestrasL
    matriz = MatrizDispersa()
    
    m=muestras.m(muestra)
    n=muestras.n(muestra)
    
    for x in range(1, m+1):
        for y in range(1, n+1):
            if celdasVivas.Existe(x,y)== 0:
                
                nuevaCelda=NodoD("",x,y,0,"#FFFFFF")
                rejilla.agregar(nuevaCelda)
                libres=libres+1
                n1 = NodoCeldas(x,y,"#FFFFFF","")
                matriz.insertar(n1)
                
            elif celdasVivas.Existe(x,y)==1:
                #print(celdasVivas.organismo(x,y))
                color=celdasVivas.color(x,y)
                codigoOrganismo=celdasVivas.organismo(x,y)
                nuevaCelda=NodoD(codigoOrganismo,x,y,1,color)
                rejilla.agregar(nuevaCelda)
                ocupadas=ocupadas+1
                
                n1 = NodoCeldas(x,y,color,codigoOrganismo)
                matriz.insertar(n1)
                
            else:
                print("algo falló con celdas ocupadas :/")
                
    rejilla.print()
    print("CELDAS LIBRES: "+ str(libres)+". CELDAS OCUPADAS: "+str(ocupadas)+". Total: "+str(libres+ocupadas))
    matriz.graficarDot("Inicial",muestra)
    #rejilla.graficar()
    return rejilla



#CARGA DE Bacterias Vivas

def cargarVivas(filename, nombreM,listaOrganismos):
    
    tree = ET.parse(filename)
    organismos = tree.getroot()
    celdasVivas =ListaSimpleEnlazada2()
    matriz = MatrizDispersa()
    
    for organismo in organismos:
        for datoP in organismo.iter('muestra'):
            codigo=datoP.find('codigo').text
            for rejilla1 in datoP.iter('listadoCeldasVivas'):
                for rejilla in rejilla1.iter('celdaViva'):
                    codigoOrganismo=rejilla.find('codigoOrganismo').text
                    
                    #str(codigoOrganismo)==str(nombreO) and
                    if  str(codigo) == str(nombreM):
                        fila=rejilla.find('fila').text
                        columna=rejilla.find('columna').text
                        color=listaOrganismos.color(str(codigoOrganismo))
                        
                        nuevoVivo=NodoS2(fila,columna,color,codigoOrganismo,codigo)
                        celdasVivas.agregar(nuevoVivo)
                        

                        #n1 = NodoCeldas(fila,columna,color,codigoOrganismo)
                        #matriz.insertar(n1)
                        #matriz.graficarDot("Inicial",codigo)
    #celdasVivas.print()
    return celdasVivas


Inicio(listaOrganismos,listaMuestras,menu,filename1,celdasVivas,rejilla,muestra)