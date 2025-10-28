import csv
import os
from config import RUTA

#Encabezados del csv, especificado para reutilizarlo en las distintas funciones
encabezados = ["nombre", "poblacion", "superficie", "continente"]

#Función que ecibe una string y devuelve true o false en caso de que sea solo letras o
#tenga otros caracteres involucrados
def es_texto_valido(texto: str):
    return texto.replace(" ", "").replace("-", "").isalpha()

#Función que recibe una string y verifica si esta es un numero y si es mayor a 0, devolviendo true o false
def es_numero_valido(numero: str, tipo: type, nombre: str, contador: int):
    try:
        valor = tipo(numero)
        if not valor > 0:
            print(f"Error en linea {contador}: campo {nombre} menor o igual a 0")
        return valor > 0
    except ValueError:
        print(f"Error en linea {contador}: campo {nombre} inválido o formato incorrecto")
        return False

#Función que valida cada linea, comprobando campo por campo si cumplen el formato predefinido.
#Devuelve true o false en caso de que detecte al menos un campo inválido
def validar_linea(linea: dict, contador: int):
    """
    Valida cada campo de la línea y devuelve una tupla (bool, mensaje).
    Si es válida devuelve (True, None). Si no, devuelve (False, mensaje_de_error).
    """
    try:
        # Verifica que existan todas las columnas requeridas
        for campo in encabezados:
            if campo not in linea or linea[campo] is None or str(linea[campo]).strip() == "":
                print(f"Error en linea {contador}: campo '{campo}' faltante o vacío")
                return False

        # Validar nombre (solo letras y espacios)
        if not es_texto_valido(linea["nombre"]):
            print(f"Error en linea {contador}: campo 'nombre' inválido o formato incorrecto")
            return False

        # Validar población (número entero positivo)
        if not es_numero_valido(linea["poblacion"], int, "poblacion", contador):
            return False

        # Validar superficie (número decimal positivo)
        if not es_numero_valido(linea["superficie"], float, "superficie", contador):
            return False

        # Validar continente (solo letras y espacios)
        if not es_texto_valido(linea["continente"]):
            print(f"Error en linea {contador}: campo 'continente' inválido o formato incorrecto")
            return False

        return True

    except Exception:
        return False

#Funcion para sobreescribir el cvs, escribiendo el encabezando y borrando el resto de información.
#Se utiliza unicamente cuando el formato de encabezado en el csv es incorrecto
def corregir_encabezados():
    try:
        with open(RUTA, "w", newline="", encoding="UTF-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=encabezados)
            escritor.writeheader()
        print("Encabezados corregidos, archivo limpiado completamente")
    except Exception:
        print("Error")

#Función que verifica si existe el csv, y lo crea de no serlo.
#Si existe, verifica la validez del formato en cada linea
def validar_csv():
    # Si el archivo no existe, se crea con los encabezados
    if not os.path.exists(RUTA):
        try:
            with open(RUTA, "w", newline="", encoding="UTF-8") as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=encabezados)
                escritor.writeheader()
            print("Archivo CSV creado con éxito")
            return
        except Exception as e:
            print(f"Error al crear el archivo: {e}")
            return

    # Si el archivo existe, validar su contenido
    lineas_validas = []
    lineas_invalidas = 0
    
    try:
        with open(RUTA, "r", newline="", encoding="UTF-8") as archivo:
            lector = csv.DictReader(archivo)
            if list(lector.fieldnames) != encabezados:
                print("Error: Los encabezados del archivo no coinciden con el formato esperado")
                return corregir_encabezados()
            
            #Valida linea por linea
            contador = 1
            for linea in lector:
                contador += 1
                if validar_linea(linea, contador):
                    lineas_validas.append(linea)
                else:
                    lineas_invalidas += 1
                    print(f"Línea {contador} inválida: {linea}")
        
        #Sobreescribe con las lineas correctas
        with open(RUTA, "w", newline="", encoding="UTF-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=encabezados)
            escritor.writeheader()
            escritor.writerows(lineas_validas)

        # Mue
        print(f"\nValidación completada:")
        print(f"- Líneas válidas: {len(lineas_validas)}")
        print(f"- Líneas eliminadas: {lineas_invalidas}")

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

def main():
    validar_csv()

if __name__ == "__main__":
    main()