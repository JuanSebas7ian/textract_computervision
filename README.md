# [**COMPUTER VISION - Prueba Técnica.**](#indice)

## [Introducción:](#indice)


Esta aplicación está construída en el Framework _Django (Python)_. Se usa para extraer la información de número de registro, fecha, departamento, ciudad, vereda y estado que se encuentra en los documentos de tradición y libertad que genera el sistema colombiano de manera estándar. La información propiamente se extrae desde un .json generado previamente a través de Textract AWS, sobre el documento que se le carga para ello.

La aplicación se ejecuta de manera local por el momento, pero queda abierta a poder integrarla con AWS.


# [Indice](#indice)
A continuación listamos los elementos por los que está compuesto este documento, luego de leer la introducción:

- [Introducción](#introducción)
- [Requisitos del sistema.](#requisitos-del-sistema)
- [Instrucciones de uso.](#instrucciones-de-uso)
- [Archivo de configuración _Settings_](#archivo-de-configuración-settings)
    - [Diccionarios](#diccionarios)
    - [Arrays](#arrays)
- [Dependencias y APIs](#dependencias-y-apis)
- [Módulos, Clases y Funciones](#módulos-clases-y-funciones)
    - [Módulos](#módulos)
        - [json](#json)
    - [Clases y Funciones](#clases-y-funciones)
        - [JsonManager](#jsonmanager)
- [Autores](#autores)
- [Historial de cambios](#historial-de-cambios)


# [Requisitos del Sistema:](#indice)
Como el despliegue de la aplicación es de manera local por el momento, es suficiente con que en el sistema operativo desde el que se gestionen los archivos insumo se cumplan con los siguientes requisitos

1. Tener acceso a internet, por si vamos a almacenar datos en GitHub o en algún repo.
2. Tener acceso a un editor de código (VsCode preferiblemente).

# [Instrucciones de Uso:](#indice)
La aplicación funciona de la siguiente manera:
- La persona quién va a ejecutar el proyecto debe cargar en la carpeta static/json, los .json generados por el proceso de extracción que previamente se ejecuta en AWS. Adicionalmente y de manera opcional, si quiere carga los PDFs en la ruta static/pdf para tenerlos a la mano y poderlos visualizar.

Una vez cargados los archivos, ejecutamos el __init__.py que se encuentra en la raiz del proyecto y listo.


# [Archivo de configuración _Settings_:](#indice)
Si bien es un archivo fundamental que forma parte de la configuración de esta aplicación, desarrollada con este framework, solo voy a explicar lo que no viene por defecto y que corresponde a un dict y una ruta en una array:

#### [DICCIONARIOS {}:](#indice)

- MONTHS: Proporciona los nombres de los meses del año y su respectivo número.

        ```
        MONTHS = {
        'Enero':"1",
        'Febrero':"2",
        'Marzo':"3",
        'Abril':"4",
        'Mayo':"5",
        'Junio':"6",
        'Julio':"7",
        'Agosto':"8",
        'Septiembre':"9",
        'Octubre':"10",
        'Noviembre':"11",
        'Diciembre':"12",
        
    }
        ```
    ---

    
#### [ARRAYS []:](#indice)

- STATIC_FILES_DIR: Contiene la ruta a la carpeta con los .json del proyecto.

        ```
        STATIC_FILES_DIR = [
            'static/json/'
        ]
        ```
    ---

# [Dependencias y APIs:](#indice)
A continuación las dependencias y las versiones de las mismas, utilizadas en esta aplicación:

- Django==4.2.4
- Python==3.9.6


# [Módulos, Clases y Funciones:](#indice)
### [Módulos.](#indice)
- La aplicación, en la carpeta _modules_, contiene 7 módulos, enfocados cada uno a una actividad particular:

    #### **json**: 
    Contiene una clase llamada _JsonManager_ con **2 funciones**, relacionadas a las interacciones con los servicios entre la aplicación y JSON.

---
### [Clases y Funciones.](#indice)
- Cada uno de los módulos explicados anteriormente, contiene la cantidad de funciones descritas en la definición de cada uno. A continuación, la explicación de lo que hace cada función. Adicionalmente, se explicará que módulos son utilizados por otros:

    #### [**JsonManager**:](#indice) 
    Contiene las siguientes 2 funciones:
        
    - **load_json_info(self,json_path):** 
        
        - **Definición:** Obtiene la información desde el archivo Json seleccionado. Retorna el json obtenido.

        - **Parámetros:** json_path (str)

        ---
    - **get_registration_info(self, datos_json):** 
        
        - **Definición:** Captura la información número de registro, fecha, departamento, ciudad, vereda, estado, solicitada en el reto. Retorna un array con estos datos

        - **Parámetros:** datos_json (dict)

# [Autores:](#indice)
Esta aplicación fue construída por **Juan Sebastian Paniagua Alvarez (jpaniagu)**, para la prueba técnica.

# [Historial de Cambios:](#indice)

A continuación, una tabla en la que se deben registrar los cambios:

| Fecha      | Versión | Descripción | Autores                         |
|------------|---------|-------------|---------------------------------|
| 24/12/2023 | 1.0.0   | Creación    | Juan Sebastian Paniagua Alvarez |

