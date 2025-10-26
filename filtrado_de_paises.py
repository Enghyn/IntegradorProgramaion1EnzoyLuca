import csv
ruta = "archivo_paices.csv"

#se le pasa por parametro el continente que se desea buscar y la función filtra entre toda la lista del csv para obtener los paices cuyos continentes son iguales al buscado
def filtrar_por_continente(continente):
    paises = []

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["continente"].strip().lower() == continente:
                paises.append(fila["nombre"], fila["poblacion"], fila["superficie"], fila["continente"])

    return paises

#se pasa por parametro la población minima y maxima de lo que se deséa filtrar, luego la función busca todos los paices que se encuentren entre esos dos valores y devuelve una tupla de estos
def filtrar_por_rango_de_población(poblacion_min, poblacion_max):
    paises = []

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
                poblacion = float(fila["poblacion"])
                if poblacion_min <= poblacion <= poblacion_max:
                    paises.append((fila["nombre"], poblacion, fila["superficie"], fila["continente"]))

    return paises

#se pasa por parametro la superficie minima y maxima de lo que se deséa filtrar, luego la función busca todos los paices que se encuentren entre esos dos valores y devuelve una tupla de estos
def filtrar_por_rango_de_superficie(superficie_min, superficie_max):
    paises = []

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
                superficie = float(fila["superficie"])
                if superficie_min <= superficie <= superficie_max:
                    paises.append((fila["nombre"], fila["poblacion"], superficie, fila["continente"]))

    return paises

def main():
    filtrar_por_continente()
    filtrar_por_rango_de_población()
    filtrar_por_rango_de_superficie()

if __name__ == "__main__":
    main()