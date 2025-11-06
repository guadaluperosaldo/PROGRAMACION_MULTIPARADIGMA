# Sistema de Gestión de Biblioteca

## Descripción del Proyecto

Este proyecto se trata de un sistema  de gestión de biblioteca utilizando el paradigma de Programación Orientada a Objetos (POO).

El sistema permite gestionar libros, registrar usuarios, y realizar las operaciones de préstamo y devolución, con persistencia de los datos en un archivo JSON.

## Instrucciones de Ejecución

1.  **Ejecución:** En la carpeta raíz del proyecto, en la terminal, ejecuta el acrchivo principal:

    python main.py

3.  **Persistencia:** El programa cargará automáticamente los datos desde `datos_biblioteca.json` al iniciar y guardará el estado actual al elegir la opción 7. Salir y Guardar Datos.

## Estructura del Código

El proyecto sigue una arquitectura, donde cada archivo tiene una función:

biblioteca/
├── main.py             es el punto de entrada y manejo del menú interactivo. desde aquí se mandan a llamar las funciones en operaciones.py y datos.py
├── modelos.py          aquí se definen las clases Libro, Usuario, Biblioteca
├── operaciones.py      contiene las funciones para gestionar la biblioteca, como prestar libros, devolverlos, agregar usuarios
└── datos.py            funcionaes para persistencia de datos en archivo json
    