from .config import RUTA
from .obtener_lista_paises import obtener_paises
import csv
from .eliminar_tildes import sin_tilde

#Campost estandar utilizados para agregar o sobreescribir el archivo csv
CAMPOS = ["nombre","poblacion","superficie","continente"]

#Funcion que recibe cuatro parámetros (nombre, poblacion, superficie y contienente),
#y los agrega como una linea nueva en el csv
def agregar_elemento(nombre:str, poblacion:int, superficie:float, continente:str):
    try:
        with open(RUTA, "a", newline="", encoding="UTF-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writerow({"nombre":nombre.capitalize(), "poblacion":poblacion, "superficie":superficie, "continente":continente.capitalize()})
        print("Agregado con éxito")

    except Exception:
        print("Error")

#Funcion que recibe cuatro parámetros (nombre, poblacion, superficie y contienente), y sobreescribe el csv,
#modificando el elemento con el mismo parametro nombre, cambiando el valor de los otros tres parámetros
def modificar_elemento(nombre:str, poblacion:int, superficie:float, continente:str):
    pais_encontrado = False
    try:
        lista_paises = obtener_paises()
        pais_modificado = {"nombre":nombre.capitalize(), "poblacion":poblacion, "superficie":superficie, "continente":continente.capitalize()}
        for i in range(len(lista_paises)):
            if lista_paises[i]["nombre"] == nombre:
                lista_paises[i] = pais_modificado
                pais_encontrado = True

        if pais_encontrado:
            with open(RUTA, "w", newline="", encoding="UTF-8") as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
                escritor.writeheader()
                escritor.writerows(lista_paises)
            print("Modificado con éxito")
        else:
            print("País no encontrado")
    except Exception:
        print("Error")


#Función que elimina el país con todos sus datos del archivo csv. Se le pasa por parametro el nombre del país, busca en el archivo csv una coincidencia exacta
# y lo elimina del csv. Crea una lista de los archivos del csv, elimina el país que el usuario ingresó como parametro. Luego sobre escribe el csv con la lista nueva.
def eliminar_elemento(nombre:str):
    pais_encontrado = False
    nombre = sin_tilde(nombre)
    try:
        lista_paises = obtener_paises()
        
        for pais in lista_paises:
                if sin_tilde(pais["nombre"]) == nombre:
                    print(pais)
                    lista_paises.remove(pais)
                    pais_encontrado = True

        if pais_encontrado:
            with open(RUTA, "w", newline="", encoding="UTF-8") as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
                escritor.writeheader()
                escritor.writerows(lista_paises)
            print("Eliminado con éxito")
        else:
            print("No se encontró el país a eliminar")
    except Exception:
        print("Error")


def main():
    pass

if __name__ == "__main__":
    main()