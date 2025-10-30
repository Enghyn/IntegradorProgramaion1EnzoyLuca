import csv
from config import RUTA
from eliminar_tildes import sin_tilde

#esta función recibe como parametro el nombre parcial o completo de un país ingresado por el usuario para ser buscado. Devuelve una lista conformada por el nombre, el continente, la población y la superficie del país buscado. 
#en caso de no encontrar coincidencias, devuelve una lista vacía
def buscar_pais(nombre_busqueda:str):
    nombre_busqueda = sin_tilde(nombre_busqueda)
    resultados = []

    with open(RUTA, "r", newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            nombre_pais = fila["nombre"].lower().strip()
            nombre_pais = sin_tilde(nombre_pais)
            # Si el texto coincide exactamente o forma parte del nombre, lo agrega
            if nombre_busqueda in nombre_pais:
                resultados.append(fila)

    return resultados

def main():
    texto = input("Ingrese parte o todo el nombre del país\n"">> ").lower().strip()
    resultados = buscar_pais(sin_tilde(texto))

    if resultados:
        print("\nCoincidencias encontradas:")
        for fila in resultados:
            print(f"- {fila['nombre']} ({fila['continente']}, {fila['poblacion']} habitantes, {fila["superficie"]} km2)")
    else:
        print("No se encontraron coincidencias.")

if __name__ == "__main__":
    main()