
import os
import openpyxl as ox
def creacion():
    archivo=ox.Workbook()
    archivo.save("Canciones UWU.xlsx")
    archivoo=ox.load_workbook("Canciones UWU.xlsx")
    archivo=archivoo['Sheet']
    archivo['A1']=2
    archivoo.save("Canciones UWU.xlsx")
    print("Archivo creado UWU")

def conversion_asky(palabra):
    cadascii=""
    infrm=[]
    for s in palabra:
        codigo_ascii = ord(s)
        codigo_ascii=str(codigo_ascii)
        cadascii+=codigo_ascii
        inf=codigo_ascii+"-"+s
        infrm.append(inf)
    print("El Codigo Ascii de la palabra es: ",infrm)
    return cadascii