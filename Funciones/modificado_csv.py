from config import RUTA
from obtener_lista_paises import obtener_paises
import csv

#Campost estandar utilizados para agregar o sobreescribir el archivo csv
CAMPOS = ["nombre","poblacion","superficie","continente"]

#Funcion que recibe cuatro parámetros (nombre, poblacion, superficie y contienente),
#y los agrega como una linea nueva en el csv
def agregar_elemento(nombre:str, poblacion:int, superficie:float, continente:str):
    try:
        with open(RUTA, "a", newline="", encoding="UTF-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writerow({"nombre":nombre, "poblacion":poblacion, "superficie":superficie, "continente":continente})
        print("Agregado con éxito")

    except Exception:
        print("Error")

#Funcion que recibe cuatro parámetros (nombre, poblacion, superficie y contienente), y sobreescribe el csv,
#modificando el elemento con el mismo parametro nombre, cambiando el valor de los otros tres parámetros
def modificar_elemento(nombre:str, poblacion:int, superficie:float, continente:str):
    try:
        lista_paises = obtener_paises()
        pais_modificado = {"nombre":nombre, "poblacion":poblacion, "superficie":superficie, "continente":continente}
        for i in range(len(lista_paises)):
            if lista_paises[i]["nombre"] == nombre:
                lista_paises[i] = pais_modificado
        
        with open(RUTA, "w", newline="", encoding="UTF-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(lista_paises)

        print("Modificado con éxito")
    except Exception:
        print("Error")


#Función que elimina el país con todos sus datos del archivo csv. Se le pasa por parametro el nombre del país, busca en el archivo csv una coincidencia exacta
# y lo elimina del csv. Crea una lista de los archivos del csv, elimina el país que el usuario ingresó como parametro. Luego sobre escribe el csv con la lista nueva.
def eliminar_elemento(nombre:str):
    try:
        lista_paises = obtener_paises()
        
        for pais in lista_paises:
                if pais["nombre"] == nombre:
                    print(pais)
                    lista_paises.remove(pais)
        
        with open(RUTA, "w", newline="", encoding="UTF-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(lista_paises)

        print("Eliminado con éxito")
    except Exception:
        print("Error")


def main():
    pass

if __name__ == "__main__":
    main()