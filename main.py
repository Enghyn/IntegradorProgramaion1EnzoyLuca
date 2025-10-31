import Funciones.busqueda_de_paises
import Funciones.filtrado_de_paises
import Funciones.ordenado_de_paises
import Funciones.mostrar_estadisticas
import Funciones.validacion_csv
import Funciones.modificado_csv
import Funciones.obtener_lista_paises

#Menú de opciones
def main():
    Funciones.validacion_csv.validar_csv()
    while True:
        print("""Bienvenido a nustra base de datos de países.
        =========MENÜ=========
        [1] Buscar país
        [2] Filtrar países
        [3] Ordenar países
        [4] Agregar, modificar o eliminar países
        [5] Mostrar estadísticas
        [6] Salir""")
        opcion = input(">> ")
        match opcion:
            #Opción buscar país
            case "1":
                texto = input("Ingresa el país a buscar\n"">> ").lower().strip()
                resultado = Funciones.busqueda_de_paises.buscar_pais(texto)
                if resultado:
                    for fila in resultado:
                        print(f"{fila['nombre']} -- {fila['continente']} -- {fila['poblacion']} habitantes -- {fila["superficie"]} KM²)")
                else:
                    print("No se encuentran países.")
            #Opción Filtrar países
            case "2":
                opcion = input("Filtrar por:\n[1] Continente\n[2] Por rango de población\n[3] Por rango de superficie\n"">> ")
                match opcion:
                    #Filtrar por continente
                    case "1":
                        continente = input("Ingrese el continente a buscar\n"">> ")
                        resultado = Funciones.filtrado_de_paises.filtrar_por_continente(continente)
                        if resultado:
                            for fila in resultado:
                                print(f"{fila['nombre']} -- {fila['continente']} -- {fila['poblacion']} habitantes -- {fila["superficie"]} KM²")
                        else:
                            print("No se encontraron coincidencias")
                    #Filtrar por rango de población
                    case "2":
                        try:    
                            poblacion_min = int(input("Ingresa el rango minimo\n"">> "))
                            poblacion_max = int(input("Ingresa el rango maximo\n"">> "))
                        except ValueError:
                            print("Solo puedes ingresar numeros")
                            continue

                        resultado = Funciones.filtrado_de_paises.filtrar_por_rango_de_población(poblacion_min, poblacion_max)
                        if resultado:
                            for fila in resultado:
                                print(fila)
                        else:
                            print("No se encontraron países dentro de ese rango")
                    #Filtrar por rango de superficie
                    case "3":
                        try:
                            superficie_min = int(input("Ingresa el rango minimo\n"">> "))
                            superficie_max = int(input("Ingresa el rango maximo\n"">> "))
                        except ValueError:
                            print("Solo puedes ingresar numeros")
                            continue

                        resultado = Funciones.filtrado_de_paises.filtrar_por_rango_de_superficie(superficie_min, superficie_max)
                        if resultado:
                            for fila in resultado:
                                print(fila)
                        else:
                            print("No se encontraron países dentro de ese rango")
                    case __:
                        print("Opción ingresada invalida")
            #Opción Ordenar países
            case "3":
                while True:
                    print("""Ordenar por:\n[1] Nombre\n[2] Superficie\n[3] Población\n[4] Volver al inicio""")
                    opcion = input(">> ")
                    match opcion:
                        #Ordenar por nombre
                        case "1":
                            lista_paises = Funciones.ordenado_de_paises.ordenar_por_nombre()
                            print("Lista de países ordenada:")
                            for linea in lista_paises:
                                print(f"{linea["nombre"]} -- población: {linea["poblacion"]} -- superficie: {linea["superficie"]}KM² -- {linea["continente"]}")
                        #Ordenar por superficie (ascendente o descendente)
                        case "2":
                            orden = input("[1] Ordenar de manera ascendente\n[2] Ordenar de manera descendente\n"">> ")
                            if orden == "1":
                                orden = False
                            elif orden == "2":
                                orden = True
                            else:
                                print("Opción ingresada invalida")
                                continue
                            lista_paises = Funciones.ordenado_de_paises.ordenar_por_superficie(orden)
                            print("Lista de países ordenada:")
                            for linea in lista_paises:
                                print(f"{linea["nombre"]} -- población: {linea["poblacion"]} -- superficie: {linea["superficie"]}KM² -- {linea["continente"]}")
                        #Ordenar por población (ascendente o descendente)
                        case "3":
                            orden = input("[1] Ordenar de manera ascendente\n[2] Ordenar de manera descendente\n"">> ")
                            if orden == "1":
                                orden = False
                            elif orden == "2":
                                orden = True
                            else:
                                print("Opción ingresada invalida")
                                continue
                            lista_paises = Funciones.ordenado_de_paises.ordenar_por_poblacion(orden)
                            print("Lista de países ordenada:")
                            for linea in lista_paises:
                                print(f"{linea["nombre"]} -- población: {linea["poblacion"]} -- superficie: {linea["superficie"]}KM² -- {linea["continente"]}")
                        #Volver al menú
                        case "4":
                            print("Volviendo al menú principal")
                            break
                        case __:
                            print("Opción ingresada invalida")
            #Opción Agregar, modificar o eliminar países
            case "4":
                opcion = input("Ingrese la opción a realizar:\n[1] Agregar nuevo elemento\n[2] Modificar elemento\n[3] Eliminar elementos\n[4] Salir\n>> ")
                match opcion:
                    #Agregar un país
                    case "1":
                        pais_repetido = False
                        while True:
                            nombre = input("Ingrese el nombre del país a agregar\n"">> ").lower().strip()
                            if input(f"Nombre ingresado: {nombre}. ¿Es correcto? [1]Si [2]No\n"">> ").lower().strip() == "2":
                                continue
                            lista_pais = Funciones.obtener_lista_paises.obtener_paises()
                            for fila in lista_pais:
                                if fila["nombre"].lower().strip() == nombre:
                                    print("El país ingresado ya se encuentra en el csv")
                                    pais_repetido = True
                            if pais_repetido:
                                break
                            poblacion = input("Ingrese la población del país\n"">> ").lower().strip()
                            if input(f"Población ingresada: {poblacion}. ¿Es correcto? [1]Si [2]No\n"">> ").lower().strip() == "2":
                                continue
                            continente = input("Ingrese el continente del país\n"">> ").lower().strip()
                            if input(f"Continente ingresado: {continente}. ¿Es correcto? [1]Si [2]No\n"">> ").lower().strip() == "2":
                                continue
                            superficie = input("Ingrese la superficie del país\n"">> ").lower().strip()
                            if input(f"Superficie ingresada: {superficie}. ¿Es correcto? [1]Si [2]No\n"">> ").lower().strip() == "2":
                                continue
                            try:
                                poblacion = int(poblacion)
                                superficie = float(superficie)
                            except ValueError:
                                print("La población y la superficie deben ser numeros..")
                                continue
                            Funciones.modificado_csv.agregar_elemento(nombre, poblacion, superficie, continente)
                            break
                    #Modificar un país
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
                            try:
                                poblacion = int(poblacion)
                                superficie = float(superficie)
                            except ValueError:
                                print("La población y la superficie deben ser numeros..")
                                continue
                            Funciones.modificado_csv.modificar_elemento(nombre, poblacion, superficie, continente)
                            break
                    #Eliminar un país
                    case "3":
                        while True:
                            nombre = input("Ingrese el nombre del país a eliminar\n"">> ").lower().strip()
                            if input(f"Nombre ingresado: {nombre}. ¿Es correcto? [1]Si [2]No\n"">> ").lower().strip() == "2":
                                continue
                            break
                        Funciones.modificado_csv.eliminar_elemento(nombre)
                    #Volver al menú
                    case "4":
                        print("Saliendo al menú principal...")
                        break
            #Opción Mostrar estadísticas
            case "5":
                while True:
                    opcion = input("Ingrese la opción a realizar:\n[1] País con mayor y menor población\n[2] Promedio de población\n[3] Promedio de superficie\n[4] Cantidad de países por continente\n[5] Salir\n"">> ")
                    match opcion:
                        #Mostrar país con mayor y con menor población
                        case "1":
                            Funciones.mostrar_estadisticas.poblacion_mayor_y_menor()
                        #Mostrar promedio de población
                        case "2":
                            promedio_poblacion = Funciones.mostrar_estadisticas.promedio_poblacion()
                            print(f"Promedio de población: {promedio_poblacion}")
                        #Mostrar promedio de superficie
                        case "3":
                            promedio_superficie = Funciones.mostrar_estadisticas.promedio_superficie()
                            print(f"Promedio de superficie: {promedio_superficie}")
                        #Mostrar cantidad de países por contiente
                        case "4":
                            Funciones.mostrar_estadisticas.paises_por_continente()
                        #Volver al menú
                        case "5":
                            print("Volviendo al menú de inicio")
                            break
                        case __:
                            print("Opción ingresada invalida")
                            continue
            #Opción Salir
            case "6":
                print("Hasta la proxima!!!")
                break
            case __:
                print("Opción ingresada invalida")
                continue

if __name__ == "__main__":
    main()