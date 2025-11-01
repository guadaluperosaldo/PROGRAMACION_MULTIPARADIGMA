"""
Módulo de Modelo

Contiene las definiciones de las clases principales que estructuran
los datos del sistema de gestión de tareas

Clases:
    - Tarea:         Clase base para una tarea genérica
    - TareaUrgente:  Clase hija que representa una tarea con prioridad
    - GestorTareas:  Clase que administra la lista de objetos Tarea
"""

class Tarea:
    """
    Representa una tarea genérica

    Atributos:
        _descripcion (str): El texto de la tarea
        _completada (bool): El estado de la tarea (True si está completada)
    """
    def __init__(self, descripcion):
        """Inicializa una nueva Tarea"""
        self._descripcion = descripcion
        self._completada = False

    @property
    def descripcion(self):
        """Obtiene la descripción de la tarea"""
        return self._descripcion

    def marcar_completada(self):
        """Marca la tarea como completada"""
        self._completada = True

    def is_completada(self):
        """Verifica si la tarea está completada"""
        return self._completada

    def __str__(self):
        """Representación en string de la Tarea"""
        estado = "Completada" if self._completada else "Pendiente"
        return f"[Tarea Normal] {self._descripcion} ({estado})"

    def a_diccionario(self):
        """Convierte la Tarea a un diccionario para serialización"""
        return {
            "tipo": "Normal",
            "descripcion": self.descripcion,
            "completada": self._completada
        }

class TareaUrgente(Tarea):
    """
    Representa una tarea urgente que hereda de Tarea

    Atributos:
        prioridad (str): Nivel de prioridad (ej. "Alta", "Media")
    """
    def __init__(self, descripcion, prioridad):
        """Inicializa una nueva TareaUrgente"""
        super().__init__(descripcion)
        self.prioridad = prioridad

    def __str__(self):
        """Redefine la representación en string para TareaUrgente"""
        estado = "Completada" if self._completada else "Pendiente"
        return f"[TAREA URGENTE] {self._descripcion} (Prioridad: {self.prioridad}) ({estado})"

    def a_diccionario(self):
        """Convierte la TareaUrgente a un diccionario"""
        datos_base = super().a_diccionario()
        datos_base.update({
            "tipo": "Urgente",
            "prioridad": self.prioridad
        })
        return datos_base

class GestorTareas:
    """
    Administra una lista de tareas en memoria

    Atributos:
        _tareas (list): Lista de objetos Tarea o TareaUrgente
    """
    def __init__(self):
        """Inicializa el gestor con una lista de tareas vacía"""
        self._tareas = []

    @property
    def tareas(self):
        """Obtiene la lista de tareas (para guardar)"""
        return self._tareas

    @tareas.setter
    def tareas(self, tareas_cargadas):
        """Establece la lista de tareas (para cargar)"""
        self._tareas = tareas_cargadas

    def agregar_tarea(self, tarea_obj):
        """
        Añade un objeto Tarea a la lista

        Parámetros:
            tarea_obj (Tarea): El objeto Tarea o TareaUrgente a agregar
        """
        self._tareas.append(tarea_obj)
        print(f"Tarea '{tarea_obj.descripcion}' agregada.")

    def listar_tareas(self):
        """Imprime todas las tareas en la lista"""
        print("\nLista de Tareas")
        if not self._tareas:
            print("No hay tareas pendientes.")
            return

        for i, tarea in enumerate(self._tareas):
            # Polimorfismo: Llama al __str__ de Tarea o TareaUrgente
            print(f"{i + 1}. {str(tarea)}")
        print("\n")

    def marcar_completada(self, indice):
        """
        Marca una tarea como completada usando su índice

        Parámetros:
            indice (int): El número de la tarea a marcar
        
        Retorna:
            bool: True si se marcó, False si hubo un error
        """
        if 0 < indice <= len(self._tareas):
            tarea = self._tareas[indice - 1]
            if not tarea.is_completada():
                tarea.marcar_completada()
                print(f"Tarea '{tarea.descripcion}' marcada como completada.")
                return True
            else:
                print("Esa tarea ya estaba completada.")
                return False
        else:
            print("Error: Número de tarea fuera de rango.")
            return False

    def eliminar_tarea(self, indice):
        """
        Elimina una tarea usando su índice

        Parámetros:
            indice (int): El número de la tarea a eliminar

        Retorna:
            bool: True si se eliminó, False si hubo un error
        """
        if 0 < indice <= len(self._tareas):
            tarea_eliminada = self._tareas.pop(indice - 1)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada.")
            return True
        else:
            print("Error: Número de tarea fuera de rango.")
            return False