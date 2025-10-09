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
        if self.prestado:
            estado = "Prestado"
        else:
            estado = "Disponible"
        
        print("\nFicha del Libro:")
        print(f"Biblioteca: {Libro.biblioteca}") #atributo de clase
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.anio_publicacion}")
        print(f"Estado: {estado}")

# Script principal para usar la clase
if __name__ == "__main__":
    #Instanciación de tres objetos de la clase Libro
    libro1 = Libro("Demian", "Hermann Hesse", 1919)
    libro2 = Libro("El retrato de Dorian Gray", "Oscar Wilde", 1890)
    libro3 = Libro("1984", "George Orwell", 1949)

    #Manipulación de los objetos llamando a sus métodos
    libro1.prestar()  #Prestar el primer libro
    libro2.prestar()  #Prestar el segundo libro
    libro2.devolver() #Devuelver el segundo libro
    libro3.prestar()  #Prestar el tercer libro
    libro3.prestar()  #Intentar prestar de nuevo para ver el mensaje de advertencia

    #Muestra del estado final de cada libro
    print("\nEstado final de los libros:")
    libro1.mostrar_estado()
    libro2.mostrar_estado()
    libro3.mostrar_estado()
