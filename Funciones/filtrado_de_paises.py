import csv
from .config import RUTA
from .eliminar_tildes import sin_tilde

#se le pasa por parametro el continente que se desea buscar y la función filtra entre toda la lista del csv para obtener los paises cuyos continentes son iguales al buscado
def filtrar_por_continente(continente:str):
    continente = sin_tilde(continente)
    paises = []

    with open(RUTA, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            fila_continente = sin_tilde(fila["continente"].strip().lower())
            if fila_continente == continente:
                paises.append(fila)

    return paises

#se pasa por parametro la población minima y maxima de lo que se deséa filtrar, luego la función busca todos los paises que se encuentren entre esos dos valores y devuelve una tupla de estos
def filtrar_por_rango_de_población(poblacion_min:int, poblacion_max:int):
    paises = []

    with open(RUTA, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
                poblacion = float(fila["poblacion"])
                if poblacion_min <= poblacion <= poblacion_max:
                    paises.append((fila["nombre"], poblacion, fila["superficie"], fila["continente"]))

    return paises

#se pasa por parametro la superficie minima y maxima de lo que se deséa filtrar, luego la función busca todos los paises que se encuentren entre esos dos valores y devuelve una tupla de estos
def filtrar_por_rango_de_superficie(superficie_min:float, superficie_max:float):
    paises = []

    with open(RUTA, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
                superficie = float(fila["superficie"])
                if superficie_min <= superficie <= superficie_max:
                    paises.append((fila["nombre"], fila["poblacion"], superficie, fila["continente"]))

    return paises

def main():
    pass

if __name__ == "__main__":
    main()