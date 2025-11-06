"""
modelos.py 
Contiene las clases principales para el Sistema de Gestión de una Biblioteca:

Clases:
Libro: con atributos como título, autor, año y estado (disponible o prestado)
Usuario: atributos de nombre y lista de libros prestados
Biblioteca: que administre libros y usuarios
"""

class Libro:
    """
    Representa un libro de la bibliotecta 

    esta clase es para inicializar un nuevo libro
    """
    def __init__(self, titulo: str, autor: str, year: int):
        """
        esta clase es para inicializar un nuevo libro
        """
        self.titulo = titulo
        self.autor = autor
        self.year = year
        self.estado = "Disponible" #este es el estado por defecto de un libro

    def __str__(self):
        """
        para darle formato a la representación en string de un libro
        """
        return f"'{self.titulo}, por {self.autor} ({self.year}) - Estado: {self.estado}."
    
    def aDiccionario(self):
        """
        para convertir un libro el diccionario para guardarlo en json
        """
        return self.__dict__
    
class Usuario:
    """
    Se refiere a un usuario de la biblioteca
    """
    def __init__(self, nombre: str):
        """
        para inicializar un nuevo usuario
        """
        self.nombre = nombre
        self.librosPrestados = [] #para guardar libros solicitados por el usuario

    def __str__(self):
        """
        para darle formato a la representación en string de un usuario
        """
        return f"Usuario: {self.nombre} - Libros prestados: {len(self.librosPrestados)}"
    
    def aDiccionario(self):
        """
        para convertir un usuario en diccionario para guardarlo en json
        """
        return self.__dict__
    
class Biblioteca:
    """
    Esta clase administra los libros y usuarios
    """
    def __init__(self):
        """
        inicializamos las listas de usuarios y libros de la biblioteca
        """
        self.libros = []
        self.usuarios = []

        