
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
    print(palabra,"<--- palabra")
    try:
        for s in palabra:
            codigo_ascii = ord(s)
            if s==" " or s=="-" or s=="_":
                cadascii+=" "
            else:
                codigo_ascii=str(codigo_ascii)
                codigo_ascii+=" "
                cadascii+=codigo_ascii
                inf=codigo_ascii+"-"+s
                infrm.append(inf)
    except:
        print("no se paso ningun parametro")
        return("N/E")
    print("El Codigo Ascii de la palabra es: ",infrm)
    print(cadascii)
    return cadascii