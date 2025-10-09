#definición de la clase Libro
class Libro:
    # atributo de clase
    biblioteca = "Biblioteca Octavio Paz"

    #método constructor para inicializar los atributos de instancia
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.prestado = False  #inicializado comIo False

    #método para prestar el libro
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya se encuentra prestado.")

    #método para devolver el libro
    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba en la biblioteca.")

    #método para mostrar la información completa del libro
    def mostrar_estado(self):
        # Se usa un operador ternario para definir el texto del estado
        estado = "Prestado" if self.prestado else "Disponible"
        
        print("\nFicha del Libro:")
        print(f"Biblioteca: {Libro.biblioteca}") #atributo de clase
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.anio_publicacion}")
        print(f"Estado: {estado}")