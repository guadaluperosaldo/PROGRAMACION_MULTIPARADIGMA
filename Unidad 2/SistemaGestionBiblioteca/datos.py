"""
datos.py

Gestiona la persistencia de datos, cargar y guardar datos de la biblioteca en un archivo json
"""

import json
import os
from modelos import Biblioteca, Libro, Usuario

ARCHIVO = 'datos_biblioteca.json'

def GuardarDatos(biblioteca: Biblioteca):
    """
    para guardar la información de la biblioteca, los libros y usuarios
    """
    
    datos = {
        'libros' : [libro.aDiccionario() for libro in biblioteca.libros], # convierte las listas de objetos en listas de diccionarios
        'usuarios' : [usuario.aDiccionario() for usuario in biblioteca.usuarios], #igual pero los objetos de Usuarios
    }

    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)
        print(f"Datos guardados con éxito en {ARCHIVO}.")
    except Exception as e:
        print(f"No se pudieron guardar los datos {e}.")

def CargarDatos(biblioteca: Biblioteca):
    """
    Carga los datos desde el archivo json
    """
    if not os.path.exists(ARCHIVO):
        print("Biblioteca nueva")
        return
    
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            data = json.load(f)

            for datosLibro in data.get('libros', []):
                biblioteca.libros.append(Libro(
                    datosLibro['titulo'],
                    datosLibro['autor'],
                    datosLibro['year']
                ))
                # Restaurar estado
                if 'estado' in datosLibro:
                    biblioteca.libros[-1].estado = datosLibro['estado'] #el índice -1 hace referencia al último elemento de una lista

            for datosUsuarios in data.get('usuarios', []):
                usuario = Usuario(datosUsuarios['nombre'])
                usuario.librosPrestados = datosUsuarios.get('librosPrestados', [])
                biblioteca.usuarios.append(usuario)

            print(f"Datos cargados con éxito desde {ARCHIVO}.")

    except Exception as e:
        print(f"Error al cargar los datos: {e}")