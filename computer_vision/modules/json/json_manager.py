import json
import os
import sys
from datetime import datetime
import settings as sts

class JsonManager:
    
    # Instanciamos una copia del dict que contiene los nombres de los meses y su respectivo número.
    MONTHS = sts.MONTHS.copy()
    
    def load_json_info(self, json_path):
        try:
            # Verificamos si el archivo existe
            if os.path.exists(json_path):
                
                # Leemos el archivo JSON
                with open(json_path, 'r') as archivo:
                    
                    # Cargamos el contenido JSON en una variable
                    datos_json = json.load(archivo)
                    
                    # retornamos los datos cargados
                    return datos_json

            else:
                print(f"The json file {json_path} does not exists.")
                
        except Exception as e: 
            tipo_excepcion, valor_excepcion, traceback = sys.exc_info()

            # Imprime detalles de la excepción
            print(f"Excepción: {tipo_excepcion.__name__}")
            print(f"Mensaje de error: {valor_excepcion}")
            print(f"Nombre del módulo: {traceback.tb_frame.f_globals['__name__']}")
            print(f"Número de línea: {traceback.tb_lineno}")

    def get_registration_info(self,datos_json):
        
        try:
            
            # Definimos este array para ayudar en el proceso de formateo de la fecha
            month_name_array=[]
            
            # En este array almacenaremos toda la información.
            complete_data_array = []
            
            # Definimos esta variable booleana para validar si en el recorrido por la info, 
            # pasó por el estado del documento
            estado_folio_checked = False
            
            # Recorremos el objeto ingresado por parámetro, en la lista Blocks
            for data in range(len(datos_json['Blocks'])):
                
                # Cargamos la data que contiene Blocks y comenzamos a realizar los filtros.
                dict_tmp = datos_json['Blocks'][data]
                for value in dict_tmp:
                    if value == 'Text':
                        
                        # Extraemos el número de la matrícula
                        if 'Nro Matrícula:' in dict_tmp[value]:
                            registration_number = str(dict_tmp[value]).replace('Nro Matrícula: ','')
                            complete_data_array.append(registration_number)
                            continue
                        
                        # Extraemos la información del inmueble: Departamento,Municipio y Vereda
                        if 'CIRCULO REGISTRAL:' in dict_tmp[value]:

                            # Buscamos las ubicaciones de cada palabra definida dentro de la cadena que contiene toda la data
                            pos_depto = str(dict_tmp[value]).find('DEPTO')
                            pos_munc = str(dict_tmp[value]).find('MUNICIPIO')
                            pos_vereda = str(dict_tmp[value]).find('VEREDA')
                            
                            # Extraemos el valor de cada elemento, basándonos en las posiciones anteriores.
                            departamento = str(dict_tmp[value])[pos_depto:pos_munc-1].replace('DEPTO: ','')
                            municipio = str(dict_tmp[value])[pos_munc:pos_vereda-1].replace('MUNICIPIO: ','')
                            vereda = str(dict_tmp[value])[pos_vereda:].replace('VEREDA: ','')

                            # Anexamos la información al array de respuestas.
                            complete_data_array.append(departamento)
                            complete_data_array.append(municipio)
                            complete_data_array.append(vereda)

                            continue
                        
                        # Extraemos la información de la fecha, en el formato YYYY-MM-DD
                        if 'Impreso el' in dict_tmp[value]:

                            # Eliminamos la información que hace ruido en la fecha y la dejamos en formato dd/mm/yyyy
                            unformated_document_date = str(dict_tmp[value]).replace('Impreso el ','')
                            unformated_document_date = str(unformated_document_date).replace(' de ','/')
                            month_name_array = unformated_document_date.split('/')
                            month_unformated_name = str(month_name_array[1])
                            pos_detalle_hora = str(unformated_document_date).find('a las')
                            temporal_document_date = unformated_document_date[:pos_detalle_hora-1]
                            
                            # Reemplazamos el nombre del mes por el número del mes
                            temporal_document_date = temporal_document_date.replace(month_unformated_name,self.MONTHS[month_unformated_name])
                            
                            # Convertimos la cadena de fecha a tipo datetime y luego le damos el formato de YYYY-MM-DD
                            document_date=datetime.strptime(temporal_document_date, "%d/%m/%Y")
                            final_document_date = datetime.strftime(document_date,"%Y-%m-%d")
                            
                            # Anexamos la información al array de respuestas.
                            complete_data_array.append(final_document_date)

                            continue
                        
                        # Validamos si el recorrido del Loop pasó por el elemento Estado del Folio. Esto lo hacemos, porque el valor del estado
                        # se encuentra en el item que sigue, en el objeto JSON
                        if 'ESTADO DEL FOLIO:' in dict_tmp[value]:
                            estado_folio_checked = True
                            continue
                        
                        # Si efectivamente pasó por el estado del folio, procedemos a almacenar en el array de respuestas el valor.
                        # Luego seteamos nuevamente el valor del booleano a False para que no vuelva a pasar por ahí
                        if estado_folio_checked == True:
                            folio_status = dict_tmp[value]
                            complete_data_array.append(folio_status)
                            estado_folio_checked = False
                            continue
                        
            # Retornamos el array con la data solicitada.                
            return complete_data_array
    
        except Exception as e: 
            tipo_excepcion, valor_excepcion, traceback = sys.exc_info()

            # Imprime detalles de la excepción
            print(f"Excepción: {tipo_excepcion.__name__}")
            print(f"Mensaje de error: {valor_excepcion}")
            print(f"Nombre del módulo: {traceback.tb_frame.f_globals['__name__']}")
            print(f"Número de línea: {traceback.tb_lineno}")
        