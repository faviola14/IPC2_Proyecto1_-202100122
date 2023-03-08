import xml.etree.ElementTree as ET
from xml.dom import minidom
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
matriz0 = MatrizDispersa()
CeldasAnalizar=ListaSimpleEnlazada2()
menu=0
filename1=""

#INICIO DEL PROGRAMA
def Inicio(listaO,listaM,menu,filename1,vivas,rejilla1,muestra,mu,celdasA):
    muestra=muestra
    matriz0 = MatrizDispersa()
    matriz0=mu
    listaOrganismos=ListaSimpleEnlazada()
    listaOrganismos=listaO
    listaMuestras=ListaSimpleEnlazada22()
    listaMuestras=listaM
    rejilla=ListaDoble()
    rejilla=rejilla1
    menu = menu
    
    celdasVivas=ListaSimpleEnlazada2()
    celdasVivas=vivas
    CeldasAnalizar=ListaSimpleEnlazada2()
    CeldasAnalizar=celdasA
    
    if menu==0:
    
        print(Fore.BLUE + "-----------------INICIO---------------")
        print(Fore.BLUE + "Elija su Archivo XML")
        
        
        filename1 = filedialog.askopenfilename(initialdir = "/", title = "Seleccione un Archivo XML", filetypes = (("XML files", "*.xml*"), ("All files", "*.*")))
        print(Fore.BLUE + filename1)
        listaOrganismos = cargarArchivo(filename1,muestra)
        
    
    if menu==1:
        
        print(Fore.RED +  "--------------ORGANISMOS---------------")
        
        listaMuestras.CodigoMuestra()
        muestra = input(Fore.YELLOW + "Ingrese código de la Muestra que desea Analizar\n")
        if listaMuestras.buscarMuestra(muestra):
            celdasVivas = cargarVivas(filename1,muestra,listaOrganismos)
            celdasVivas.print()
            Inicio(listaOrganismos,listaMuestras,2,filename1,celdasVivas,rejilla,muestra,matriz0,CeldasAnalizar)
        else:
            print(Fore.RED +  "El código ingresado no corresponde a ninguna muestra registrada")
            Inicio(listaOrganismos,listaMuestras,1,filename1,celdasVivas,rejilla,muestra,matriz0,CeldasAnalizar)
        
    if menu==2:
        
        print()
        print(Fore.RED +  "--------------OPCIONES---------------")
        print(Fore.RED+  "1. Ver Rejilla inicial")
        print(Fore.RED+ "2. Colocar Organismos a Analizar")
        print(Fore.RED+ "3. Analizar")
        print(Fore.RED+ "4. Reiniciar Sistema")
        opc = input(Fore.YELLOW + "Seleccione una opción\n")
        if opc=='1' :
            print(Fore.BLUE+"-----------------------------------------------------------------------")
            rejilla=generarRejilla(celdasVivas,muestra,listaMuestras,listaOrganismos,listaMuestras,filename1) 
            Inicio(listaOrganismos,listaMuestras,2,filename1,celdasVivas,rejilla,muestra,matriz0,CeldasAnalizar)
            print("-----------------------------------------------------------------------")
            Inicio(listaOrganismos,listaMuestras,2,filename1,celdasVivas,rejilla,muestra,matriz0,CeldasAnalizar)
        elif  opc=='2':
            print(Fore.BLUE+"-----------------------------------------------------------------------")
            print(Fore.RED +  "--------------Colocación de Organismo---------------")
            numO = int( input(Fore.RED + "Ingrese el número de Organismos que desea Analizar\n"))
            for x in range(1, numO+1):
                fila = input(Fore.YELLOW + "Fila: ")
                columna = input(Fore.YELLOW + "Columna: ")
                if celdasVivas.Existe(fila,columna)==0:
                    listaOrganismos.NombreOrganismos()
                    nuevoO = input(Fore.YELLOW + "Código Organismo: ")
                    if listaOrganismos.buscarOrganismo(str(nuevoO)):
                        color= listaOrganismos.color(str(nuevoO))
                        
                        nuevoVivo=NodoS2(fila,columna,color,str(nuevoO),muestra)
                        celdasVivas.agregar(nuevoVivo)
                        nuevoAnalisis=NodoS2(str(fila),str(columna),color,str(nuevoO),muestra)
                        CeldasAnalizar.agregar(nuevoAnalisis)
                        rejilla=generarRejilla(celdasVivas,muestra,listaMuestras,listaOrganismos,listaMuestras,filename1) 
                        Inicio(listaOrganismos,listaMuestras,2,filename1,celdasVivas,rejilla,muestra,matriz0,CeldasAnalizar)
                        print(Fore.BLUE+"-----------------------------------------------------------------------")
                    else:
                        print(Fore.RED +  "El código ingresado no corresponde a ningún Organismo registrado")
                        Inicio(listaOrganismos,listaMuestras,2,filename1,celdasVivas,rejilla,muestra,matriz0,CeldasAnalizar)
                else: 
                    print(Fore.RED +  "Ya hay un organismo en esa celda. Inténtelo de nuevo")
                    x=x+1

        elif  opc=='3':
            print(Fore.BLUE+"-----------------------------------------------------------------------")
            simulacion(celdasVivas,muestra,listaMuestras,listaOrganismos,listaMuestras,filename1,CeldasAnalizar)
            Inicio(listaOrganismos,listaMuestras,2,filename1,celdasVivas,rejilla,muestra,matriz0,CeldasAnalizar)
        elif  opc=='4':
            print(Fore.BLUE+"-----------------------------------------------------------------------")
            matriz0 = MatrizDispersa()
            listaOrganismos=ListaSimpleEnlazada()
            listaMuestras=ListaSimpleEnlazada22()
            rejilla=ListaDoble()
            celdasVivas=ListaSimpleEnlazada2()
            CeldasAnalizar=ListaSimpleEnlazada2()
            
            filename1=""
            muestra=""
            Inicio(listaOrganismos,listaMuestras,0,filename1,celdasVivas,rejilla,muestra,matriz0,CeldasAnalizar)
        else:
            print(Fore.RED +  "No es una opción correcta")
    

#CREAR SIMULACIÓN
def simulacion(celdasVivasL,muestra,muestrasL,listaOrganismos,listaMuestras,filename1,CeldasA):
    print("ANALIZANDO")
    libres =0
    ocupadas=0
    comidas=0
    rejilla=ListaDoble()
    celdasVivas=ListaSimpleEnlazada2()
    celdasVivas=celdasVivasL
    muestras=ListaSimpleEnlazada22()
    muestras=muestrasL
    matrizA = MatrizDispersa()
    CeldasAnalizar=ListaSimpleEnlazada2()
    CeldasAnalizar=CeldasA
    m=muestras.m(muestra)
    n=muestras.n(muestra)
    
    for x in range(1, m+1):
        for y in range(1, n+1):
            if celdasVivas.Existe(x,y)== 0:
                nuevaCelda=NodoD("",x,y,0,"#FFFFFF")
                rejilla.agregar(nuevaCelda)
                libres=libres+1
                n1 = NodoCeldas(x,y,"#FFFFFF","")
                matrizA.insertar(n1)
                
            elif celdasVivas.Existe(x,y)==1:
                if (CeldasAnalizar.Existe(x,y)==1):
                    if (celdasVivas.Existe(x,y+1)==1 and CeldasAnalizar.organismo(x,y)!= celdasVivas.organismo(x,y+1)) or (celdasVivas.Existe(x,y-1)==1 and CeldasAnalizar.organismo(x,y)!= celdasVivas.organismo(x,y-1)) or (celdasVivas.Existe(x+1,y)==1 and CeldasAnalizar.organismo(x,y)!= celdasVivas.organismo(x+1,y)) or (celdasVivas.Existe(x-1,y)==1 and CeldasAnalizar.organismo(x,y)!= celdasVivas.organismo(x-1,y)):
                        
                        print()
                        print('La celda ({},{}) SOBREVIVE'.format(x, y))
                        
                        color=celdasVivas.color(x,y)
                        codigoOrganismo=celdasVivas.organismo(x,y)
                        nuevaCelda=NodoD(codigoOrganismo,x,y,1,color)
                        rejilla.agregar(nuevaCelda)
                        ocupadas=ocupadas+1
                        
                        n1 = NodoCeldas(x,y,color,codigoOrganismo)
                        matrizA.insertar(n1)
                        
                        if (celdasVivas.Existe(x+2,y)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x+2,y)):
                            if celdasVivas.Existe(x+1,y)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x+1,y)==1:
                                    rejilla.eliminar(x+1,y)
                                    celdasVivas.eliminar(x+1,y)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x+1,y,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x+1,y,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x+1,y,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x+1),str(y)))
                        
                        if (celdasVivas.Existe(x-2,y)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x-2,y)):
                            if celdasVivas.Existe(x-1,y)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x-1,y)==1:
                                    rejilla.eliminar(x-1,y)
                                    celdasVivas.eliminar(x-1,y)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x-1,y,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x-1,y,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x-1,y,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x-1),str(y)))
                                
                        if (celdasVivas.Existe(x,y+2)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x,y+2)):
                            if celdasVivas.Existe(x,y+1)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x,y+1)==1:
                                    rejilla.eliminar(x,y+1)
                                    celdasVivas.eliminar(x,y+1)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x,y+1,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x,y+1,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x,y+1,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x),str(y+1)))
                                
                        if (celdasVivas.Existe(x,y-2)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x,y-2)):
                            if celdasVivas.Existe(x,y-1)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x,y-1)==1:
                                    rejilla.eliminar(x,y-1)
                                    celdasVivas.eliminar(x,y-1)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x,y-1,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x,y-1,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x,y-1,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x),str(y-1)))
                                

                        if (celdasVivas.Existe(x+3,y)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x+3,y)):
                            if celdasVivas.Existe(x+2,y)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x+2,y)==1:
                                    rejilla.eliminar(x+2,y)
                                    celdasVivas.eliminar(x+2,y)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x+2,y,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x+2,y,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x+2,y,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x+2),str(y)))
                        
                        if (celdasVivas.Existe(x-3,y)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x-3,y)):
                            if celdasVivas.Existe(x-2,y)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x-2,y)==1:
                                    rejilla.eliminar(x-2,y)
                                    celdasVivas.eliminar(x-2,y)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x-2,y,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x-2,y,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x-2,y,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x-2),str(y)))
                                
                        if (celdasVivas.Existe(x,y+3)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x,y+3)):
                            if celdasVivas.Existe(x,y+2)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x,y+2)==1:
                                    rejilla.eliminar(x,y+2)
                                    celdasVivas.eliminar(x,y+2)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x,y+2,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x,y+2,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x,y+2,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x),str(y+2)))
                                
                        if (celdasVivas.Existe(x,y-3)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x,y-3)):
                            if celdasVivas.Existe(x,y-2)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x,y-2)==1:
                                    rejilla.eliminar(x,y-2)
                                    celdasVivas.eliminar(x,y-2)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x,y-2,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x,y-2,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x,y-2,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x),str(y-2)))

                        
                        if (celdasVivas.Existe(x+4,y)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x+4,y)):
                            if celdasVivas.Existe(x+3,y)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x+3,y)==1:
                                    rejilla.eliminar(x+3,y)
                                    celdasVivas.eliminar(x+3,y)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x+3,y,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x+3,y,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x+3,y,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x+3),str(y)))
                        
                        if (celdasVivas.Existe(x-4,y)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x-4,y)):
                            if celdasVivas.Existe(x-3,y)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x-3,y)==1:
                                    rejilla.eliminar(x-3,y)
                                    celdasVivas.eliminar(x-3,y)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x-3,y,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x-3,y,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x-3,y,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x-3),str(y)))
                                
                        if (celdasVivas.Existe(x,y+4)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x,y+4)):
                            if celdasVivas.Existe(x,y+3)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x,y+3)==1:
                                    rejilla.eliminar(x,y+3)
                                    celdasVivas.eliminar(x,y+3)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x,y+3,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x,y+3,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x,y+3,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x),str(y+3)))
                                
                        if (celdasVivas.Existe(x,y-4)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x,y-4)):
                            if celdasVivas.Existe(x,y-3)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x,y-3)==1:
                                    rejilla.eliminar(x,y-3)
                                    celdasVivas.eliminar(x,y-3)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x,y-3,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x,y-3,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x,y-3,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x),str(y-3)))

                        
                        if (celdasVivas.Existe(x+2,y+2)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x+2,y+2)):
                            if celdasVivas.Existe(x+1,y+1)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x+1,y+1)==1:
                                    rejilla.eliminar(x+1,y+1)
                                    celdasVivas.eliminar(x+1,y+1)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x+1,y+1,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x+1,y+1,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x+1,y+1,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x+1),str(y+1)))
                            
                        if (celdasVivas.Existe(x-2,y-2)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x-2,y-2)):
                            if celdasVivas.Existe(x-1,y-1)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x-1,y-1)==1:
                                    rejilla.eliminar(x-1,y-1)
                                    celdasVivas.eliminar(x-1,y-1)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x-1,y-1,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x-1,y-1,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x-1,y-1,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x-1),str(y-1)))
                            
                        if (celdasVivas.Existe(x-2,y+2)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x-2,y+2)):
                            if celdasVivas.Existe(x-1,y+1)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x-1,y+1)==1:
                                    rejilla.eliminar(x-1,y+1)
                                    celdasVivas.eliminar(x-1,y+1)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x-1,y+1,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x-1,y+1,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x-1,y+1,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x-1),str(y+1))) 
                            
                        if (celdasVivas.Existe(x+2,y-2)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x+2,y-2)):
                            
                            if celdasVivas.Existe(x+1,y-1)==1:
                                comidas=comidas+1
                                if rejilla.Existe(x+1,y-1)==1:
                                    rejilla.eliminar(x+1,y-1)
                                    celdasVivas.eliminar(x+1,y-1)
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                nuevaCelda=NodoD(codigoOrganismo,x+1,y-1,1,color)
                                rejilla.agregar(nuevaCelda)
                                
                                nuevoVivo=NodoS2(x+1,y-1,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                
                                n1 = NodoCeldas(x+1,y-1,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({},{})'.format(str(x+1),str(y-1)))

                        
                        if (celdasVivas.Existe(x-2,y)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x-2,y)) and (celdasVivas.Existe(x-1,y+1)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x-1,y+1)) and (celdasVivas.Existe(x,y+2)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x,y+2)):
                            
                            if celdasVivas.Existe(x-1,y)==1 and celdasVivas.Existe(x,y+1)==1:
                                comidas=comidas+2
                                if rejilla.Existe(x-1,y)==1:
                                    rejilla.eliminar(x-1,y)
                                    celdasVivas.eliminar(x-1,y)
                                if rejilla.Existe(x,y+1)==1:
                                    rejilla.eliminar(x,y+1)
                                    celdasVivas.eliminar(x,y+1)
                                    
                                    
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                
                                
                                nuevaCelda=NodoD(codigoOrganismo,x-1,y,1,color)
                                rejilla.agregar(nuevaCelda)
                                nuevoVivo=NodoS2(x-1,y,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                n1 = NodoCeldas(x-1,y,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({} , {})'.format(str(x-1),str(y)))
                                
                                
                                nuevaCelda1=NodoD(codigoOrganismo,x,y+1,1,color)
                                rejilla.agregar(nuevaCelda1)
                                nuevoVivo=NodoS2(x,y+1,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                n2 = NodoCeldas(x,y+1,color,codigoOrganismo)
                                matrizA.insertar(n2)
                                print('COMIDA: ({} , {})'.format(str(x),str(y+1)))
                        
                        
                        if (celdasVivas.Existe(x-2,y)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x-2,y)) and (celdasVivas.Existe(x+1,y-1)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x+1,y-1)) and (celdasVivas.Existe(x,y-2)==1 and CeldasAnalizar.organismo(x,y)== celdasVivas.organismo(x,y-2)):
                            
                            if celdasVivas.Existe(x-1,y)==1 and celdasVivas.Existe(x,y-1)==1:
                                comidas=comidas+2
                                if rejilla.Existe(x-1,y)==1:
                                    rejilla.eliminar(x-1,y)
                                    celdasVivas.eliminar(x-1,y)
                                if rejilla.Existe(x,y-1)==1:
                                    rejilla.eliminar(x,y-1)
                                    celdasVivas.eliminar(x,y-1)
                                    
                                color=celdasVivas.color(x,y)
                                codigoOrganismo=celdasVivas.organismo(x,y)
                                
                                
                                nuevaCelda=NodoD(codigoOrganismo,x-1,y,1,color)
                                rejilla.agregar(nuevaCelda)
                                nuevoVivo=NodoS2(x-1,y,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                n1 = NodoCeldas(x-1,y,color,codigoOrganismo)
                                matrizA.insertar(n1)
                                print('COMIDA: ({} , {})'.format(str(x-1),str(y)))
                                
                                
                                nuevaCelda1=NodoD(codigoOrganismo,x,y-1,1,color)
                                rejilla.agregar(nuevaCelda1)
                                nuevoVivo=NodoS2(x,y-1,color,codigoOrganismo,muestra)
                                celdasVivas.agregar(nuevoVivo)
                                n2 = NodoCeldas(x,y-1,color,codigoOrganismo)
                                matrizA.insertar(n2)
                                print('COMIDA: ({} , {})'.format(str(x),str(y-1)))

                        CeldasAnalizar.eliminar(x,y)
                    else:
                        print()
                        print('La celda ({},{}) NO SOBREVIVE'.format(x, y))
                        nuevaCelda=NodoD("",x,y,0,"#FFFFFF")
                        rejilla.agregar(nuevaCelda)
                        libres=libres+1
                        n1 = NodoCeldas(x,y,"#FFFFFF","")
                        matrizA.insertar(n1)

                        celdasVivas.eliminar(x,y)
                        CeldasAnalizar.eliminar(x,y)

                        
                elif(rejilla.Existe(x,y)==0):
                    color=celdasVivas.color(x,y)
                    codigoOrganismo=celdasVivas.organismo(x,y)
                    nuevaCelda=NodoD(codigoOrganismo,x,y,1,color)
                    rejilla.agregar(nuevaCelda)
                    ocupadas=ocupadas+1
                    
                    n1 = NodoCeldas(x,y,color,codigoOrganismo)
                    matrizA.insertar(n1)
                else:
                    print("?")
                
                
            else:
                print("algo falló con celdas ocupadas :/")
    
    print()
    print("CELDAS LIBRES: "+ str(libres)+". CELDAS OCUPADAS: "+str(ocupadas)+". Total: "+str(libres+ocupadas))
    print("COMIDAS: " + str(comidas))
    matrizA.graficarDot("Actual",muestra)
    descripcion= muestras.descripcion(muestra)
    salidaXML(listaOrganismos,celdasVivas,muestra,descripcion,m,n)
    return rejilla



#CARGA DE ARCHIVO
def cargarArchivo(filename1,muestra):
    matriz = MatrizDispersa()
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
    Inicio(organismosLista,muestras,1,filename1,celdasVivas,rejilla,muestra,matriz0,CeldasAnalizar)



#GENERAR Muestra
def generarRejilla(celdasVivasL,muestra,muestrasL,listaOrganismos,listaMuestras,filename1):
    libres =0
    ocupadas=0
    rejilla=ListaDoble()
    celdasVivas=ListaSimpleEnlazada2()
    celdasVivas=celdasVivasL
    muestras=ListaSimpleEnlazada22()
    muestras=muestrasL
    matriz0 = MatrizDispersa()
    
    m=muestras.m(muestra)
    n=muestras.n(muestra)
    
    for x in range(1, int(m)+1):
        for y in range(1, int(n)+1):
            if celdasVivas.Existe(x,y)== 0:
                
                nuevaCelda=NodoD("",x,y,0,"#FFFFFF")
                rejilla.agregar(nuevaCelda)
                libres=libres+1
                n1 = NodoCeldas(x,y,"#FFFFFF","")
                matriz0.insertar(n1)
                
            elif celdasVivas.Existe(x,y)==1:
                
                color=celdasVivas.color(x,y)
                codigoOrganismo=celdasVivas.organismo(x,y)
                nuevaCelda=NodoD(codigoOrganismo,x,y,1,color)
                rejilla.agregar(nuevaCelda)
                ocupadas=ocupadas+1
                
                n1 = NodoCeldas(x,y,color,codigoOrganismo)
                matriz0.insertar(n1)
                
            else:
                print("algo falló con celdas ocupadas :/")
                
    rejilla.print()
    print()
    print("CELDAS LIBRES: "+ str(libres)+". CELDAS OCUPADAS: "+str(ocupadas)+". Total: "+str(libres+ocupadas))
    matriz0.graficarDot("Inicial",muestra)
    
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
                    
                    if  str(codigo) == str(nombreM):
                        fila=rejilla.find('fila').text
                        columna=rejilla.find('columna').text
                        color=listaOrganismos.color(str(codigoOrganismo))
                        
                        nuevoVivo=NodoS2(fila,columna,color,codigoOrganismo,codigo)
                        celdasVivas.agregar(nuevoVivo)
                        
    return celdasVivas

def salidaXML(listaOrganismos,celdasVivas,muestra,descripcion,m,n):
    archivo = open("./Salida.xml", "a")
    elemento_1=celdasVivas.xmlMuestras(muestra,descripcion,str(m),str(n))
    
    
    
    archivo.write(ET.tostring(elemento_1, encoding='utf-8').decode('utf-8'))
    elemento_1=listaOrganismos.xmlOrganismos()
    
    
    
    
    archivo.write(ET.tostring(elemento_1, encoding='utf-8').decode('utf-8'))



Inicio(listaOrganismos,listaMuestras,menu,filename1,celdasVivas,rejilla,muestra,matriz0,CeldasAnalizar)