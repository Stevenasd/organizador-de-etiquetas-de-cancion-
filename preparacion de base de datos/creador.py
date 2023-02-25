
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