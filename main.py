import busqueda_de_paises
import filtrado_de_paises
import ordenado_de_paises
import mostrar_estadisticas
import validacion_csv
import modificado_csv

def main():
    validacion_csv.validar_csv()
    while True:
        print("""Bienvenido a nustra base de datos de países.
        =========MENÜ=========
        [1] Buscar país
        [2] Filtrar países
        [3] Ordenar países
        [4] Agregar o eliminar países
        [5] Mostrar estadísticas
        [6] Salir""")
        opcion = input(">> ")
        match opcion:
            case "1":
                texto = input("Ingresa el país a buscar\n"">> ").lower().strip()
                resultado = busqueda_de_paises.buscar_pais(texto)
                if resultado:
                    for fila in resultado:
                        print(f"- {fila['nombre']} ({fila['continente']}, {fila['poblacion']} habitantes, {fila["superficie"]} KM²)")
                else:
                    print("No se encuentran países.")
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
                opcion = input("Ingrese la opción a realizar:\n[1] Agregar nuevo elemento\n[2] Modificar elemento\n[3] Eliminar elementos\n[4] Salir\n>> ")
                match opcion:
                    case "1":
                        while True:
                            nombre = input("Ingrese el nombre del país a agregar\n"">> ").lower().strip()
                            if input(f"Nombre ingresado: {nombre}. ¿Es correcto? [1]Si [2]No\n"">> ").lower().strip() == "2":
                                continue
                            poblacion = input("Ingrese la población del país\n"">> ").lower().strip()
                            if input(f"Población ingresada: {poblacion}. ¿Es correcto? [1]Si [2]No\n"">> ").lower().strip() == "2":
                                continue
                            continente = input("Ingrese el continente del país\n"">> ").lower().strip()
                            if input(f"Continente ingresado: {continente}. ¿Es correcto? [1]Si [2]No\n"">> ").lower().strip() == "2":
                                continue
                            superficie = input("Ingrese la superficie del país\n"">> ").lower().strip()
                            if input(f"Superficie ingresada: {superficie}. ¿Es correcto? [1]Si [2]No\n"">> ").lower().strip() == "2":
                                continue
                            break
                        modificado_csv.agregar_elemento(nombre, poblacion, superficie, continente)
                    case "2":
                        while True:
                            nombre = input("Ingrese el nombre del país a modificar\n"">> ").lower().strip()
                            if input(f"Nombre ingresado: {nombre}. ¿Es correcto? [1]Si [2]No\n"">> ").lower().strip() == "2":
                                continue
                            poblacion = input("Ingrese la población del país\n"">> ").lower().strip()
                            if input(f"Población ingresada: {poblacion}. ¿Es correcto? [1]Si [2]No\n"">> ").lower().strip() == "2":
                                continue
                            continente = input("Ingrese el continente del país\n"">> ").lower().strip()
                            if input(f"Continente ingresado: {continente}. ¿Es correcto? [1]Si [2]No\n"">> ").lower().strip() == "2":
                                continue
                            superficie = input("Ingrese la superficie del país\n"">> ").lower().strip()
                            if input(f"Superficie ingresada: {superficie}. ¿Es correcto? [1]Si [2]No\n"">> ").lower().strip() == "2":
                                continue
                            break
                        modificado_csv.modificar_elemento(nombre, poblacion, superficie, continente)
                    case "3":
                        while True:
                            nombre = input("Ingrese el nombre del país a eliminar\n"">> ").lower().strip()
                            if input(f"Nombre ingresado: {nombre}. ¿Es correcto? [1]Si [2]No\n"">> ").lower().strip() == "2":
                                continue
                            break
                        modificado_csv.eliminar_elemento(nombre)

                    case "4":
                        print("Saliendo al menú principal...")
                        break

            case "5":
                while True:
                    opcion = input("Ingrese la opción a realizar:\n[1] País con mayor y menor población\n[2] Promedio de población\n[3] Promedio de superficie\n[4] Cantidad de países por continente\n[5] Salir\n"">> ")
                    match opcion:
                        case "1":
                            mostrar_estadisticas.poblacion_mayor_y_menor()
                        case "2":
                            promedio_poblacion = mostrar_estadisticas.promedio_poblacion()
                            print(f"Promedio de población: {promedio_poblacion}")
                        case "3":
                            promedio_superficie = mostrar_estadisticas.promedio_superficie()
                            print(f"Promedio de superficie: {promedio_superficie}")
                        case "4":
                            mostrar_estadisticas.paises_por_continente()
                        case "5":
                            print("Volviendo al menú de inicio")
                            break
                        case __:
                            print("Opción ingresada invalida")
                            continue
            case "6":
                print("Hasta la proxima!!!")
                break
            case __:
                print("Opción ingresada invalida")
                continue

if __name__ == "__main__":
    main()