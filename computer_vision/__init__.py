import os
from modules.json.json_manager import *

try:
    cls_json = JsonManager()
    
    # Definimos la ruta en la que se almacenaran TODOS los archivos .json generados previamente en AWS textract
    json_path_directory = sts.STATIC_FILES_DIR[0]
    
    # Ejecutamos la acción para cada uno de los archivos que se encuentran en el directorio asignado para ello.
    for filename in os.listdir(json_path_directory):
        if filename.endswith(".json"):
            print(f"Extrayendo información del archivo {filename} ........")
            
            # Definimos la ruta en la que se encuentra el archivo
            json_path = str(json_path_directory + "/" + filename)
            
            # Cargamos la información del archivo en un dict
            dict_data = cls_json.load_json_info(json_path)
            
            # Extraemos la infomrmación solicitada en el reto: número de registro, fecha, departamento, ciudad, vereda, estado
            final_data_array = cls_json.get_registration_info(dict_data)
            
            # Imprimimos el resulatdo completo y retornamos el array
            print(final_data_array)
            print(f"Extracción finalizada exitosamente!")
            
            print('=================================')
    
except Exception as e: 
    tipo_excepcion, valor_excepcion, traceback = sys.exc_info()

    # Imprime detalles de la excepción
    print(f"Excepción: {tipo_excepcion.__name__}")
    print(f"Mensaje de error: {valor_excepcion}")
    print(f"Nombre del módulo: {traceback.tb_frame.f_globals['__name__']}")
    print(f"Número de línea: {traceback.tb_lineno}")

