import csv

RUTA = "archivo_paices.csv"

def obtener_paises():
    """
    Función general que lee el archivo csv y devuelve una lista con todos los elementos del csv
    """
    try:
        lista_paises = []

        with open(RUTA, "r", newline="", encoding="UTF-8") as archivo:
            lector = csv.reader(archivo)
            next(lector)
            for linea in lector:
                lista_paises.append(linea)
        
        return lista_paises
    
    except:
        print("Error")

def cargar_paises(lista_paises:list):
    """
    Función general que carga una lista de paises en el csv
    """
    with open(RUTA, "w", newline="", encoding="UTF-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["nombre","poblacion","superficie","continente"])
            escritor.writerows(lista_paises)

def ordenar_por_nombre():
    """
    Función que sobreescribe el csv por nombre, de manera ascendente (A, B, C, D, etc.)
    """
    try:
        lista_paises = obtener_paises()
        
        lista_paises.sort(key=lambda pais: pais[0])
        #El método sort ordena la lista en base al primer elemento de cada sub-lista
        
        cargar_paises(lista_paises)
    except:
        print("Error")

def ordenar_por_poblacion():
    """
    Función que sobreescribe el csv ordenando los países por población de manera ascendente
    """
    try:
        lista_paises = obtener_paises()

        lista_paises.sort(key=lambda pais: int(pais[1]))
        #El método sort ordena la lista en base al segundo elemento de cada sub-lista

        cargar_paises(lista_paises)
    except:
        print("Error")

def ordenar_por_superficie(descendente:bool):
    """
    Función que sobreescribe el csv ordenando los países por superficie de manera ascendente
    """
    try:
        lista_paises = obtener_paises()

        lista_paises.sort(reverse=descendente, key=lambda pais: float(pais[2]))
        #El método sort ordena la lista en base al tercer elemento de cada sub-lista

        cargar_paises(lista_paises)
    except:
        print("Error")

def main():
    pass

if __name__ == "__main__":
    main()