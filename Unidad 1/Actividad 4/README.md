# Actividad 4: Crear clase simple

Este proyecto implementa una clase `Libro` en Python para demostrar los conceptos fundamentales de la Programación Orientada a Objetos, como clases, objetos, atributos y métodos.

### Atributos
-   **"titulo", "autor", "anio_publicacion"**: Se eligieron como atributos de instancia porque son características únicas de cada libro. Cada objeto Libro tendrá su propio título, autor y año.
-   **"prestado"**: Este es el estado principal del libro. Es un atributo de instancia porque el estado de préstamo de un libro es independiente del de los demás. Se inicializa en `False` por defecto, ya que un libro nuevo se considera disponible.
-   **"biblioteca"**: Se eligió como un atributo de clase porque es una propiedad compartida por todos los libros. Como atributo de clase, existe una sola copia de este dato para todas las instancias.

### Métodos

-   **__init__(self, ...)**: Es el método constructor estándar en Python. Se utiliza para asegurar que cada objeto Libro sea creado con la información esencial (título, autor, año).
-   **prestar() y devolver()**: Estos métodos encapsulan la lógica para cambiar el estado "prestado". En lugar de modificar el atributo directamente (libro.prestado = True), se definen métodos que representan acciones claras.
-   **mostrar_estado()**: Este método proporciona una forma estandarizada y limpia de obtener el estado completo de un objeto.