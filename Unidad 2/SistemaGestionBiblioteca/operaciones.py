"""
operaciones.py

contiene las funciones para la gestión de la biblioteca
"""

from modelos import Biblioteca, Libro,Usuario

def AgregarLibro(biblioteca: Biblioteca, titulo: str, autor: str, year: int):
    """
    crea un nuevo libro y lo agrega a la lista de libros de la biblioteca
    """
    try:
        nuevoLibro = Libro(titulo, autor, int(year))
        biblioteca.libros.append(nuevoLibro)
        print(f"Libro: {titulo} agregado con éxito")
    except ValueError:
        print("El año debe ser un número entero")

def AgregarUsuario(biblioteca: Biblioteca, nombre: str):
    """
    registra a un nuevo usuario y lo agrega a la lista de usuarios de la biblioteca
    """
    nuevoUsuario = Usuario(nombre)
    biblioteca.usuarios.append(nuevoUsuario)
    print(f"Usuario '{nombre} registrado con éxito")

def MostrarLibrosDisponibles(biblioteca: Biblioteca):
    """
    Muestra los libros con estado disponible
    """
    librosDisponibles = [book for book in biblioteca.libros if book.estado == "Disponible"]

    print("\nLIBROS DISPONIBLES")
    if not librosDisponibles:
        print("No hay libros disponibles.")
        return
    
    for i, libro in enumerate(librosDisponibles):
        print(f"{i + 1}. {libro}") #lista enumerada de los libros
    print("\n")

def PrestarLibro(biblioteca: Biblioteca, tituloLibro: str, nombreUsuario: str):
    """
    para actualizar el estado del libro de disponible a prestado, y agregarlo a los libros prestados del usuario
    """

    libroEncontrado = None
    usuarioEncontrado =  None

    #buscamos el libro en la lista
    for libro in biblioteca.libros:
        if libro.titulo.lower() == tituloLibro.lower() and libro.estado == "Disponible":
            libroEncontrado = libro
            break

    #buscar usuario
    for usuario in biblioteca.usuarios:
        if usuario.nombre.lower() == nombreUsuario.lower():
            usuarioEncontrado = usuario
            break

    if not libroEncontrado:
        print(f"El libro {tituloLibro} no está disponible o no existe")
        return

    if not usuarioEncontrado:
        print(f"El usuario {nombreUsuario} no está registrado")
        return
    
    #realizamos el préstamo actualizando el estado del libro
    libroEncontrado.estado = "Prestado"
    usuarioEncontrado.librosPrestados.append(libroEncontrado.titulo) #agregamos el libro a los libros prestados del usuario
    print(f"{tituloLibro} prestado a usuario {nombreUsuario}")

def DevolverLibro(biblioteca: Biblioteca, tituloLibro: str, nombreUsuario: str):
    """
    Actualizar el estado del libro a disponible y eliminarlo de los libros prestados del usuario
    """
    libroEncontrado = None
    usuarioEncontrado = None

    #buscamos el libro en la lista
    for libro in biblioteca.libros:
        if libro.titulo.lower() == tituloLibro.lower() and libro.estado == "Prestado":
            libroEncontrado = libro
            break

    #buscar usuario
    for usuario in biblioteca.usuarios:
        if usuario.nombre.lower() == nombreUsuario.lower():
            usuarioEncontrado = usuario
            break

    if not libroEncontrado:
        print(f"El libro {tituloLibro} no está disponible o no existe")
        return

    if not usuarioEncontrado:
        print(f"El usuario {nombreUsuario} no está registrado")
        return
    
    #actualizamos el estado para la devolución
    libroEncontrado.estado = 'Disponible'
    usuarioEncontrado.librosPrestados.remove(tituloLibro)
    print(f"'{tituloLibro}' devuelto por {nombreUsuario}.")