# Proyecto: Gestor de Tareas Modular

## Propósito del Programa

Este proyecto es un sistema de gestión de tareas de consola. Permite a los usuarios administrar una lista de tareas personales, incluyendo agregar tareas normales o urgentes, listarlas, marcarlas como completadas y eliminarlas. El sistema guarda el progreso en un archivo JSON para persistir los datos.

## Cómo Ejecutar el Proyecto

1.  Asegúrate de tener Python 3 instalado
2.  Coloca el proyecto en un directorio (ej. `gestor_modular/`)
3.  Abre una terminal o línea de comandos
4.  Navega hasta la carpeta raíz del proyecto (la carpeta `gestor_modular/` que contiene `main.py`)
5.  Ejecuta el programa principal con el siguiente comando:

    python main.py

6.  El menú interactivo aparecerá en la consola

## Módulos del Proyecto

El código está organizado en un paquete (`modulos`) y un script principal para separar responsabilidades:

* **`main.py`**:
    Es el punto de entrada principal. Contiene el bucle del menú y la lógica de interacción con el usuario. Se encarga de llamar a las funciones de los otros módulos

* **`modulos/modelo.py`**:
    Contiene el modelo de datos. Define las clases `Tarea`, `TareaUrgente` (herencia) y `GestorTareas`. Esta última maneja la lógica para agregar o eliminar tareas de la lista en memoria

* **`modulos/utilidades.py`**:
    Contiene funciones auxiliares de apoyo. Su única responsabilidad es la persistencia de datos: `guardar_tareas_json` y `cargar_tareas_json`, que manejan la conversión de objetos a JSON y viceversa