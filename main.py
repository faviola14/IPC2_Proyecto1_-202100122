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

listaOrganismos=ListaSimpleEnlazada()
listaMuestras=ListaSimpleEnlazada22()
contagiados=ListaDoble()
menu=0
filename1=""

#INICIO DEL PROGRAMA
def Inicio(listaO,listaM,menu,filename1):

    listaOrganismos=ListaSimpleEnlazada()
    listaOrganismos=listaO
    listaMuestras=ListaSimpleEnlazada22()
    listaMuestras=listaM
    rejilla=ListaDoble()
    menu = menu
    celdasContagiadas=ListaDoble()
    
    if menu==0:
    
        print(Fore.BLUE + "-----------------INICIO---------------")
        print(Fore.BLUE + "Elija su Archivo XML")
        
        
        filename1 = filedialog.askopenfilename(initialdir = "/", title = "Seleccione un Archivo XML", filetypes = (("XML files", "*.xml*"), ("All files", "*.*")))
        print(Fore.BLUE + filename1)
        listaOrganismos = cargarArchivo(filename1)
            
    
    if menu==1:
        listaOrganismos.print()
        listaMuestras.print()
        print(Fore.RED +  "--------------ORGANISMOS---------------")
        listaMuestras.CodigoMuestra() 
        muestra = input(Fore.YELLOW + "Ingrese código de la Muestra que desea Analizar\n")
        if listaMuestras.buscarMuestra(muestra): 
            celdasVivas = cargarVivas(filename1,muestra)
            celdasVivas.print()
            print(Fore.RED +  "--------------OPCIONES---------------")
            print(Fore.RED+  "1. Ver Muestra inicial")
            print(Fore.RED+ "2. Generar Simulación")
            opc = input(Fore.YELLOW + "Seleccione una opción\n")
            if opc=='1' :
                print(Fore.BLUE+"-----------------------------------------------------------------------")
                rejilla=generarRejilla(celdasVivas, listaOrganismos,muestra) #cambiar celdasInfectadas por celdasVivas
                print("-----------------------------------------------------------------------")
            elif  opc=='2':
                print("---2---")
            else:
                print(Fore.RED +  "No es una opción correcta")
        else: 
            print(Fore.RED +  "El código ingresado no corresponde a ningún organismo registrado")




#CARGA DE ARCHIVO
def cargarArchivo(filename1):
    
    tree = ET.parse(filename1)
    organismos = tree.getroot()
    organismosLista = ListaSimpleEnlazada()
    muestras=ListaSimpleEnlazada22()
    contador=0
    for organismo in organismos:
        contador=contador+1
        for datoP in organismo.iter('organismo'):
            nuevoOrganismo = NodoS(str(contador),datoP.find('codigo').text, datoP.find('nombre').text)
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
    Inicio(organismosLista,muestras,1,filename1)



#GENERAR Muestra
def generarRejilla(contagiados,listaO, nombre):
    
    sanas =0
    infectadas=0
    rejilla=ListaDoble()
    celdasVivas=ListaDoble()
    celdasVivas=contagiados
    listaOrganismos=ListaSimpleEnlazada()
    listaOrganismos=listaO 
    m=int(listaOrganismos.m(nombre))
    n=int(listaOrganismos.m(nombre))
    for x in range(1, m+1):
        for y in range(1, n+1):
            if celdasVivas.Existe(x,y)== 0:
                nuevaCelda=NodoD(nombre,x,y,0)
                rejilla.agregar(nuevaCelda)
                sanas=sanas+1
            elif celdasVivas.Existe(x,y)==1:
                nuevaCelda=NodoD(nombre,x,y,1)
                rejilla.agregar(nuevaCelda)
                infectadas=infectadas+1
            else:
                print("algo falló con celdas infectadas :/")
                
    rejilla.print()
    print("Células sanas: "+ str(sanas)+". Infectadas: "+str(infectadas)+". Total: "+str(sanas+infectadas))
    rejilla.graficar()
    return rejilla



#CARGA DE Bacterias Vivas

def cargarVivas(filename,nombreB):
    tree = ET.parse(filename)
    organismos = tree.getroot()
    celdasVivas =ListaSimpleEnlazada2()
    muestras=ListaSimpleEnlazada22()
    
    for organismo in organismos:
        for datoP in organismo.iter('muestra'):
            codigo=datoP.find('codigo').text
            if codigo==nombreB:
                
                for rejilla1 in organismo.iter('listadoCeldasVivas'):
                    for rejilla in organismo.iter('celdaViva'):
                        fila=rejilla.find('fila').text
                        columna=rejilla.find('columna').text
                        codigoOrganismo=rejilla.find('codigoOrganismo').text
                        
                        nuevoVivo=NodoS2(fila,columna,codigoOrganismo)
                        celdasVivas.agregar(nuevoVivo)
    #celdasVivas.print()
    return celdasVivas


Inicio(listaOrganismos,listaMuestras,menu,filename1)