import busqueda_de_paises
import filtrado_de_paises
import ordenado_de_paises

def main():
    while True:
        print("""Bienvenido a nustra base de datos de paises.
        =========MENÜ=========
        [1] Buscar país
        [2] Filtrar paises
        [3] Ordenar paises
        [4] Agregar o eliminar paises
        [5] Salir""")
        opcion = input(">> ")
        match opcion:
            case "1":
                texto = input("Ingresa el país a buscar\n"">> ")
                resultado = busqueda_de_paises.buscar_pais(texto)
                if resultado:
                    for fila in resultado:
                        print(f"- {fila['nombre']} ({fila['continente']}, {fila['poblacion']} habitantes, {fila["superficie"]} KM²)")
                else:
                    print("No se encuentran paises.")
            case "2":
                opcion = input("Filtrar por:\n[1] Continente\n[2] Por rango de población\n[3] Por rango de superficie\n"">> ")
                match opcion:
                    case "1":
                        continente = input("Ingrese el continente a buscar\n"">> ")
                        resultado = filtrado_de_paises.filtrar_por_continente(continente)
                        if resultado:
                            for fila in resultado:
                                print(f"- {fila['nombre']} ({fila['continente']}, {fila['poblacion']} habitantes, {fila["superficie"]} KM²)")
                        else:
                            print("No se encontraron coincidencias")
                    case "2":
                        try:
                            poblacion_min = int(input("Ingresa el rango minimo\n"">> "))
                            poblacion_max = int(input("Ingresa el rango maximo\n"">> "))
                        except ValueError:
                            print("Solo puedes ingresar numeros")
                            continue

                        resultado = filtrado_de_paises.filtrar_por_rango_de_población(poblacion_min, poblacion_max)
                        if resultado:
                            for fila in resultado:
                                print(fila)
                        else:
                            print("No se encontraron países dentro de ese rango")
                    case "3":
                        try:
                            superficie_min = int(input("Ingresa el rango minimo\n"">> "))
                            superficie_max = int(input("Ingresa el rango maximo\n"">> "))
                        except ValueError:
                            print("Solo puedes ingresar numeros")
                            continue

                        resultado = filtrado_de_paises.filtrar_por_rango_de_superficie(superficie_min, superficie_max)
                        if resultado:
                            for fila in resultado:
                                print(fila)
                        else:
                            print("No se encontraron países dentro de ese rango")
                    case __:
                        print("Opción ingresada invalida")
            case "3":
                while True:
                    print("""Ordenar por:\n[1] Nombre\n[2] Superficie\n[3] Población\n[4] Volver al inicio""")
                    opcion = input(">> ")
                    match opcion:
                        case "1":
                            lista_paises = ordenado_de_paises.ordenar_por_nombre()
                            print("Lista de países ordenada:")
                            for linea in lista_paises:
                                print(f"{linea["nombre"]} -- población: {linea["poblacion"]} -- superficie: {linea["superficie"]}KM² -- {linea["continente"]}")
                        case "2":
                            orden = input("[1] Ordenar de manera ascendente\n[2] Ordenar de manera descendente\n"">> ")
                            if orden == "1":
                                orden = False
                            elif orden == "2":
                                orden = True
                            else:
                                print("Opción ingresada invalida")
                                continue
                            lista_paises = ordenado_de_paises.ordenar_por_superficie(orden)
                            print("Lista de países ordenada:")
                            for linea in lista_paises:
                                print(f"{linea["nombre"]} -- población: {linea["poblacion"]} -- superficie: {linea["superficie"]}KM² -- {linea["continente"]}")
                        case "3":
                            orden = input("[1] Ordenar de manera ascendente\n[2] Ordenar de manera descendente\n"">> ")
                            if orden == "1":
                                orden = False
                            elif orden == "2":
                                orden = True
                            else:
                                print("Opción ingresada invalida")
                                continue
                            lista_paises = ordenado_de_paises.ordenar_por_poblacion(orden)
                            print("Lista de países ordenada:")
                            for linea in lista_paises:
                                print(f"{linea["nombre"]} -- población: {linea["poblacion"]} -- superficie: {linea["superficie"]}KM² -- {linea["continente"]}")
                        case "4":
                            print("Volviendo al menú principal")
                            break
                        case __:
                            print("Opción ingresada invalida")
            case "4":
                pass
            case "5":
                print("Hasta la proxima!!!")
                break

if __name__ == "__main__":
    main()