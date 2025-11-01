"""
Módulo de Utilidades

Contiene funciones auxiliares para la persistencia de datos,
para guardar y cargar las tareas en formato JSON

Funciones:
    - guardar_tareas_json: Guarda una lista de tareas en un archivo JSON
    - cargar_tareas_json: Carga una lista de tareas desde un archivo JSON
"""

import json
import os
# Usamos import relativo (el .) para importar desde el mismo paquete 'modulos'
from .modelo import Tarea, TareaUrgente

def guardar_tareas_json(archivo_json, lista_tareas_obj):
    """
    Guarda la lista de objetos Tarea en un archivo JSON

    Parámetros:
        archivo_json (str): La ruta del archivo donde se guardarán los datos
        lista_tareas_obj (list): La lista de objetos Tarea/TareaUrgente
    """
    # Polimorfismo: Llama a a_diccionario() de cada objeto
    datos_para_guardar = [tarea.a_diccionario() for tarea in lista_tareas_obj]
    
    try:
        with open(archivo_json, 'w', encoding='utf-8') as f:
            json.dump(datos_para_guardar, f, indent=4)
        print(f"Datos guardados en {archivo_json}")
    except IOError as e:
        print(f"Error al guardar el archivo: {e}")

def cargar_tareas_json(archivo_json):
    """
    Carga las tareas desde un archivo JSON y retorna una lista de objetos

    Parámetros:
        archivo_json (str): La ruta del archivo desde donde se cargarán los datos

    Retorna:
        list: Una lista de objetos Tarea y/o TareaUrgente
    """
    if not os.path.exists(archivo_json):
        print("Archivo de datos no encontrado. Empezando con lista vacía.")
        return []

    lista_objetos_tarea = []
    try:
        with open(archivo_json, 'r', encoding='utf-8') as f:
            datos_cargados = json.load(f)
            
            for item_tarea in datos_cargados:
                if item_tarea.get('tipo') == 'Urgente':
                    tarea_obj = TareaUrgente(
                        item_tarea['descripcion'],
                        item_tarea.get('prioridad', 'Desconocida')
                    )
                else:
                    tarea_obj = Tarea(item_tarea['descripcion'])
                
                if item_tarea.get('completada', False):
                    tarea_obj.marcar_completada()
                    
                lista_objetos_tarea.append(tarea_obj)
            
            print(f"Datos cargados desde {archivo_json}")
    except Exception as e:
        print(f"Error al cargar o decodificar el archivo {archivo_json}: {e}")
        return [] # Retorna lista vacía en caso de error

    return lista_objetos_tarea