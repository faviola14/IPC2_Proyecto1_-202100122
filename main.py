import xml.etree.ElementTree as ET
from colorama import Fore
from tkinter import filedialog

menu=0
filename1=""


def Inicio(menu,filename1):
    
    
    menu =menu
    
    
    if menu==0:
    
        print(Fore.BLUE + "-----------------INICIO---------------")
        print(Fore.BLUE + "Elija su Archivo XML")
        
        
        
        filename1 = filedialog.askopenfilename(initialdir = "/", title = "Seleccione un Archivo XML", filetypes = (("XML files", "*.xml*"), ("All files", "*.*")))
        print(Fore.BLUE + filename1)
        listaMuestras = cargarArchivo(filename1)
        
def cargarArchivo(filename1):
    tree = ET.parse(filename1)
    muestras = tree.getroot()
    
    contador =0
    
Inicio(menu,filename1)
