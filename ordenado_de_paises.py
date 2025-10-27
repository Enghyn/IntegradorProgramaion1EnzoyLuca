from obtener_lista_paises import obtener_paises

#Función que recibe una lista de paises o un diccionario, e imprime la información de cada país
#con formato, o del diccionario
def mostrar_paises(paises):
    if isinstance(paises, list):
        for pais in paises:
                print(f"País: '{pais["nombre"]}', Población: '{pais["poblacion"]}', Superficie: '{pais["superficie"]}', Continente: '{pais["continente"]}'")
    else:
        print(f"País: '{paises["nombre"]}', Población: '{paises["poblacion"]}', Superficie: '{paises["superficie"]}', Continente: '{paises["continente"]}'")
    
#Función que utiliza una lista de paises y los ordena por nombre de manera ascendente (A, B, C, D, etc.),
#devuelve la lista ordenada
def ordenar_por_nombre():
    try:
        lista_paises = obtener_paises()
        
        lista_paises.sort(key=lambda pais: pais["nombre"])
        #El método sort ordena la lista en base al nombre del país
        
        return lista_paises
        
    except:
        print("Error")

#Función que utiliza una lista de paises y los ordena por población de manera ascendente o descendiente,
#devuelve la lista ordenada
def ordenar_por_poblacion(descendente:bool):
    try:
        lista_paises = obtener_paises()

        lista_paises.sort(reverse=descendente, key=lambda pais: int(pais["poblacion"]))
        #El método sort ordena la lista en base a la población de cada sub-lista en
        #manera descendente o ascendente, dependiendo del valor de la variable descendiente

        return lista_paises
        
    except:
        print("Error")

#Función que utiliza una lista de paises y los ordena por superficie de manera ascendente o descendiente,
#devuelve la lista ordenada
def ordenar_por_superficie(descendente:bool):
    try:
        lista_paises = obtener_paises()

        lista_paises.sort(reverse=descendente, key=lambda pais: float(pais["superficie"]))
        #El método sort ordena la lista en base a la suérficie de cada sub-lista en
        #manera descendente o ascendente, dependiendo del valor de la variable descendiente

        return lista_paises
        
    except:
        print("Error")

def main():
    print(ordenar_por_poblacion(False))

if __name__ == "__main__":
    main()