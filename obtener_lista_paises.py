import csv

from config import RUTA

#Función general que lee el archivo csv y devuelve una lista con todos los elementos del csv
def obtener_paises():
    try:
        lista_paises = []

        with open(RUTA, "r", newline="", encoding="UTF-8") as archivo:
            lector = csv.DictReader(archivo)
            
            for linea in lector:
                lista_paises.append(linea)
        
        return lista_paises
    
    except:
        print("Error")