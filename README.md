# Sistema de Gestión de Países

## Descripción
Sistema desarrollado en Python para gestionar y analizar información sobre países del mundo. 
Permite realizar búsquedas, filtrados, ordenamientos y modificaciones sobre datos almacenados en formato CSV.

## Universidad
Universidad Tecnológica Nacional
1ro Comisión 4

## Profesores
Cinthia Rigoni
Ramiro Hualpa

## Estructura del Proyecto
Proyecto_Paises
│
├── Funciones/
│   ├── __init__.py                # Indica que la carpeta es un paquete Python
│   ├── busqueda_de_paises.py      # Funciones de búsqueda (exacta o parcial)
│   ├── config.py                  # Configuración general del proyecto
│   ├── eliminar_tildes.py         # Normaliza texto eliminando tildes
│   ├── filtrado_de_paises.py      # Filtrado por continente, población, etc.
│   ├── modificado_csv.py          # Permite agregar o modificar datos del CSV
│   ├── mostrar_estadisticas.py    # Calcula y muestra estadísticas generales
│   ├── obtener_lista_paises.py    # Obtiene lista de países desde el CSV
│   ├── ordenado_de_paises.py      # Ordena la lista según distintos criterios
│   └── validacion_csv.py          # Verifica formato y consistencia del archivo CSV
│
├── archivo_paises.csv             # Base de datos principal de países
├── main.py                        # Archivo principal del programa
└── README.md                      # Documentación del proyecto

## Funcionalidades Principales

### Búsqueda de Países
- Búsqueda exacta por nombre
- Búsqueda parcial/aproximada
- Búsqueda por criterios múltiples

### Filtrado de Datos
- Filtrado por continente
- Filtrado por rango de población
- Filtrado por criterios personalizados

### Ordenamiento
- Ordenar por nombre
- Ordenar por población
- Ordenar por continente
- Ordenamiento ascendente/descendente

### Gestión de Datos
- Agregar nuevos países
- Modificar información existente
- Validación de datos ingresados
- Normalización de texto (eliminación de tildes)

### Estadísticas
- Mostrar estadísticas generales
- Calcular promedios y totales
- Generar reportes

## Requisitos
- Python 3.x
- Archivo CSV con datos de países

## Uso
1. Ejecutar `main.py`
2. Seleccionar la operación deseada del menú
3. Seguir las instrucciones en pantalla
4. Los cambios se guardan automáticamente en archivo_paises.csv

## Autores
- Enzo Giaquinta
- Luca Argumedo

## Ejemplos de Uso
```python
# Búsqueda por nombre
> Ingrese país: Argentina
Argentina -- América -- 45700000 habitantes -- 2780400 KM²

# Filtrado por continente
> Continente: Europa
1. España
2. Francia
3. Italia
...
```

## Instalación
```bash
# Clonar el repositorio
git clone https://github.com/Enghyn/IntegradorProgramaion1EnzoyLuca/tree/develop

# Verificar Python
python --version

# Ejecutar el programa
python main.py
```

## Librerias
- Unicodedata
- csv

## Links
- Repositorio: https://github.com/Enghyn/IntegradorProgramaion1EnzoyLuca/tree/develop
- Informe PDF: https://drive.google.com/file/d/1ovPNs6sLk9Q-ok5dScA-1Pk9UwSEobv5/view?usp=sharing
- Video: 

## Versión
1.0.0