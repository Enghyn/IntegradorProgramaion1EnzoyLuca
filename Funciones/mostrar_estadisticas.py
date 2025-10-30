from .ordenado_de_paises import ordenar_por_poblacion, mostrar_paises
from .obtener_lista_paises import obtener_paises

#Función que utiliza una lista de países, e imprime el de mayor y menor población
def poblacion_mayor_y_menor():
    lista_paises = ordenar_por_poblacion(False)
    pais_menor_poblacion = lista_paises[0]
    pais_mayor_poblacion = lista_paises[-1]
    print("País con mayor población:")
    mostrar_paises(pais_mayor_poblacion)
    print("País con menor población:")
    mostrar_paises(pais_menor_poblacion)

#Función que utiliza una lista de países, y devuelve el promedio de la población
def promedio_poblacion():
    lista_paises = obtener_paises()

    cantidad_paises = len(lista_paises)
    suma_poblacion = 0
    
    for pais in lista_paises:
        suma_poblacion += int(pais["poblacion"])
    
    promedio_poblacion = suma_poblacion / cantidad_paises

    return round(promedio_poblacion, 2)

#Función que utiliza una lista de países, y devuelve el promedio de la superficie
def promedio_superficie():
    lista_paises = obtener_paises()

    cantidad_paises = len(lista_paises)
    suma_superficie = 0
    
    for pais in lista_paises:
        suma_superficie += float(pais["superficie"])
    
    promedio_superficie = suma_superficie / cantidad_paises

    return round(promedio_superficie, 2)

#Función que utiliza una lista de países, e imprime la cantidad de países por continente
def paises_por_continente():
    lista_paises = obtener_paises()
    cantidad_por_continente = {"América": 0, "Europa": 0, "Asia": 0, "Oceanía": 0, "África":0}
    
    for pais in lista_paises:
        cantidad_por_continente[pais["continente"]] += 1
    
    print(f"América: {cantidad_por_continente['América']}, Europa: {cantidad_por_continente['Europa']}, Asia: {cantidad_por_continente['Asia']}, Oceanía: {cantidad_por_continente['Oceanía']}, África: {cantidad_por_continente['África']}")

def main():
    pass

if __name__ == "__main__":
    main()