# Sistema de Gestión de Tareas (POO)

## Descripción

Este es un programa de consola que funciona como un sistema de gestión de tareas personales. Permite a los usuarios agregar nuevas tareas (normales o urgentes), listar todas las tareas, marcar tareas como completadas y eliminarlas.

El programa aplica los principios fundamentales de la Programación Orientada a Objetos (POO):

* **Herencia:** Para crear diferentes tipos de tareas.
* **Encapsulación:** Para proteger el estado interno de los objetos.
* **Polimorfismo:** Para que diferentes tipos de tareas se comporten de manera distinta.

Así como **persistencia de datos**, guardando todas las tareas en un archivo `mis_tareas.json` al salir y cargándolas al iniciar.

***

## Instrucciones de Ejecución

2.  Guarda el código en un único archivo (por ejemplo, `gestor_tareas.py`).
3.  Abre una terminal.
4.  Navega hasta el directorio donde guardaste el archivo.
5.  Ejecuta el script con el siguiente comando: python gestor_tareas.py
6.  El programa se iniciará y mostrará el menú interactivo.
7.  Al seleccionar la opción "Salir", todas las tareas se guardarán automáticamente en un archivo llamado `mis_tareas.json` en la misma carpeta.

***

## Explicación del Diseño (POO)

El sistema está estructurado en tres clases principales:

### 1. Clases Implementadas

* **`Tarea` (Clase Base):** Representa una tarea genérica. Contiene los atributos comunes a todas las tareas: `_descripcion` y `_completada`.
* **`TareaUrgente(Tarea)` (Clase Hija):** Representa una tarea que hereda de `Tarea`. Añade un nuevo atributo, `prioridad`, demostrando la **herencia**.
* **`GestorTareas` (Clase Controladora):** Contiene la lista de tareas (`_tareas`) y toda la lógica de la aplicación (agregar, listar, eliminar, guardar, cargar).

### 2. Encapsulación

Se aplica para proteger la integridad de los datos:

* Los atributos principales se definen como "privados" usando un guion bajo.
* La modificación de estos atributos se controla a través de métodos públicos. Por ejemplo, el estado `_completada` solo puede cambiarse a `True` mediante el método `marcar_completada()`.

### 3. Herencia

La relación `TareaUrgente(Tarea)` permite la reutilización de código:

* `TareaUrgente` obtiene automáticamente todos los métodos y atributos de `Tarea`.
* `super().__init__(...)` se utiliza en el constructor de la clase hija para inicializar la parte que corresponde a la clase padre.

### 4. Polimorfismo

El polimorfismo se implementa redefiniendo métodos de la clase padre en la clase hija:

1.  **Método `__str__`:**
    * La clase `Tarea` lo define para mostrarse como `[Tarea Normal] ...`.
    * La clase `TareaUrgente` lo redefine para mostrarse como `[TAREA URGENTE] ... (Prioridad: ...)`
    * Cuando el `GestorTareas` lista las tareas, simplemente llama a `str(tarea)` sobre cada objeto.

2.  **Método `a_diccionario`:**
    * Cada clase sabe cómo convertirse a sí misma en un diccionario para ser guardada en JSON.
    * `TareaUrgente` redefine este método, llamando a la versión del padre (`super().a_diccionario()`) y luego añadiendo su propio dato (`"prioridad"`).

### 5. Persistencia

* **Guardar:** El `GestorTareas` utiliza el método `a_diccionario` de cada tarea para crear una lista de diccionarios, que luego se guarda en formato JSON.
* **Cargar:** Al iniciar, el gestor lee el archivo JSON. Itera sobre los datos y, gracias al campo `"tipo"` guardado, decide si debe reconstruir un objeto `Tarea` o `TareaUrgente`.