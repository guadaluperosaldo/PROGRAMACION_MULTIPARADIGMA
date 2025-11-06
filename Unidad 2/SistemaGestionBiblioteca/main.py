"""
main.py

es el punto de entrada al sistema. contiene un menú interactivo y controla el flujo del programa
"""

from modelos import Biblioteca
from operaciones import ( AgregarLibro, AgregarUsuario, MostrarLibrosDisponibles, PrestarLibro, DevolverLibro )
from datos import CargarDatos, GuardarDatos

def MostrarMenu():
    """
    Imprime el menú en consola
    """
    print("\nSISTEMA GESTOR DE BIBLIOTECA")
    print("1. Agregar libro")
    print("2. Agregar usuario")
    print("3. Mostrar libros disponibles")
    print("4. Préstamo de libro")
    print("5. Devolución de libro")
    print("6. Mostrar todos los usuarios")
    print("7. Guardar datos y salir")
    print("\n")


def AgregarLibroNuevo(biblioteca: Biblioteca):
    """Maneja la entrada de datos para agregar un libro"""
    print("\nAgregar nuevo libro")
    titulo = input("Título: ")
    autor = input("Autor: ")
    year = input("Año de Publicación: ")
    AgregarLibro(biblioteca, titulo, autor, year)

def AgregarUsuarioNuevo(biblioteca: Biblioteca):
    """Maneja la entrada de datos para agregar un usuario"""
    print("\nAgregar nuevo usuario")
    nombre = input("Nombre del usuario: ")
    AgregarUsuario(biblioteca, nombre)

def PrestarLibroGestor(biblioteca: Biblioteca):
    """Maneja la entrada de datos para prestar un libro"""
    print("\nPrestar libro")
    titulo = input("Título del libro a prestar: ")
    usuario = input("Nombre del usuario: ")
    PrestarLibro(biblioteca, titulo, usuario)

def DevolverLibroGestor(biblioteca: Biblioteca):
    """Maneja la entrada de datos para devolver un libro."""
    print("\nDevolver Libro")
    titulo = input("Título del libro a devolver: ")
    usuario = input("Nombre del usuario: ")
    DevolverLibro(biblioteca, titulo, usuario)

def MostrarUsuarios(biblioteca: Biblioteca):
    """Muestra todos los usuarios y sus préstamos"""
    print("\nRegistro de usuarios")
    if not biblioteca.usuarios:
        print("No hay usuarios registrados.")
        return
    for usuario in biblioteca.usuarios:
        print(usuario)
    print("\n")

def main():
    """
    función principal que inicializa y ejecuta el programa
    """

    biblioteca = Biblioteca()
    CargarDatos(biblioteca) # Cargar los datos al iniciar

    while True:
        MostrarMenu()
        opcion = input("Selecciona una de las siguientes opciones: ")

        match opcion:
            case "1":
                AgregarLibroNuevo(biblioteca)
                # No hay break, el bucle continúa
            case "2":
                AgregarUsuarioNuevo(biblioteca)
            case "3":
                MostrarLibrosDisponibles(biblioteca)
            case "4":
                PrestarLibroGestor(biblioteca)
            case "5":
                DevolverLibroGestor(biblioteca)
            case "6":
                MostrarUsuarios(biblioteca)
            case "7":
                GuardarDatos(biblioteca)
                print("Guardando datos y saliendo...")
                break 
            case _:
                print("Opción no válida. Seleccione del 1 al 7.")

if __name__ == "__main__":
    main()