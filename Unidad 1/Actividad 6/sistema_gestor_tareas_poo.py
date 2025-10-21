import json
import os

#clase base
class Tarea:
    #representa una tarea genérica, es la clase base para la herencia 
    def __init__(self, descripcion):

        #_descripcion para el atributo interno
        self._descripcion = descripcion
        #_completada es un estado interno
        self._completada = False

    #métodos getters y setters para encapsulación    
    @property
    def descripcion(self):
        #propiedad getter para la descripción
        return self._descripcion

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        #propiedad setter para la descripción
        if nueva_descripcion:
            self._descripcion = nueva_descripcion
        else:
            print("La descripción no puede estar vacía.")

    def marcar_completada(self):
        #método para modificar el estado
        if not self._completada:
            self._completada = True
            return True
        return False #ya estaba completada

    def is_completada(self):
        #método getter del estado
        return self._completada

    #método que será redefinido, para polimorfismo    
    def __str__(self):
        #representación en string del objeto
        estado = "Completada" if self._completada else "Pendiente"
        return f"[Tarea Normal] {self._descripcion} ({estado})"

    #método para guardar las tareas    
    def a_diccionario(self):
        #convierte un diccionario a json
        return {
            "tipo": "Normal",
            "descripcion": self._descripcion,
            "completada": self._completada
        }

#clase hija
class TareaUrgente(Tarea):
    #representa una tarea urgente, hereda de tarea y añade el atributo de prioridad
    def __init__(self, descripcion, prioridad):
        #llama al constructor de la clase padre
        super().__init__(descripcion)
        self.prioridad = prioridad

    #redefinimos el método. polimorfismo    
    def __str__(self):
        estado = "Completada" if self._completada else "Pendiente"
        #mostramos la prioridad, que no existe en la clase padre
        return f"[TAREA URGENTE] {self._descripcion} (Prioridad: {self.prioridad}) ({estado})"

    #redefinimos el método para incluir la prioridad al guardar    
    def a_diccionario(self):
        #pobtenemos el diccionario base del padre
        datos_base = super().a_diccionario()
        #actualizamos con los datos específicos de esta clase
        datos_base.update({
            "tipo": "Urgente",
            "prioridad": self.prioridad
        })
        return datos_base

#clase gestora
class GestorTareas:
    #maneja la lista de tareas, el guardado y carga de tareas y la lógica del sistema
    def __init__(self, archivo_json="tareas.json"):
        self._tareas = []
        self._archivo_json = archivo_json

    def crear_y_agregar_tarea(self):
        #lógica para crear y añadir una nueva tarea
        descripcion = input("Introduce la descripción de la tarea: ")
        tipo = input("¿Es una tarea urgente? (s/n): ").lower()

        if tipo == 's':
            prioridad = input("Introduce la prioridad (Alta, Media, Baja): ")
            nueva_tarea = TareaUrgente(descripcion, prioridad)
        else:
            nueva_tarea = Tarea(descripcion)
        
        self._tareas.append(nueva_tarea)
        print(f"Tarea '{descripcion}' agregada con éxito.")

    def listar_tareas(self):
        #muestra todas las tareas, usa __str__ sin saber qué tipo de tarea es
        print("Lista de tareas")
        if not self._tareas:
            print("No hay tareas pendientes.")
            return

        for i, tarea in enumerate(self._tareas):
            #llama a __str__ de Tarea o TareaUrgente
            print(f"{i + 1}. {str(tarea)}")
        print("\n")

    def marcar_completada(self):
        #marca una tarea como completada por su índice
        self.listar_tareas()
        if not self._tareas:
            return
            
        try:
            idx = int(input("Introduce el número de la tarea a completar: "))
            
            if 1 <= idx <= len(self._tareas):
                tarea_a_marcar = self._tareas[idx - 1]
                if tarea_a_marcar.marcar_completada():
                    print(f"Tarea '{tarea_a_marcar.descripcion}' marcada como completada.")
                else:
                    print("Esa tarea ya estaba completada.")
            else:
                print("Error: Número de tarea fuera de rango.")
        except ValueError:
            print("Error: Debes introducir un número.")

    def eliminar_tarea(self):
        #elimina una tarea por su índice
        self.listar_tareas()
        if not self._tareas:
            return

        try:
            idx = int(input("Introduce el número de la tarea a eliminar: "))
            
            if 1 <= idx <= len(self._tareas):
                #pop() para eliminar por índice
                tarea_eliminada = self._tareas.pop(idx - 1)
                print(f"Tarea '{tarea_eliminada.descripcion}' eliminada.")
            else:
                print("Error: Número de tarea fuera de rango.")
        except ValueError:
            print("Error: Debes introducir un número.")

    #métodos paara guardar y cargar
    def guardar_tareas(self):
        #guarda la lista de tareas en un archivo json
        #prepara una lista de diccionarios usando el polimorfismo de a_diccionario()
        datos_para_guardar = [tarea.a_diccionario() for tarea in self._tareas]
        
        try:
            with open(self._archivo_json, 'w', encoding='utf-8') as f:
                json.dump(datos_para_guardar, f, indent=4)
            print(f"Datos guardados en {self._archivo_json}")
        except IOError as e:
            print(f"Error al guardar el archivo: {e}")

    def cargar_tareas(self):
        #carga las tareas desde el archivo json al iniciar
        if not os.path.exists(self._archivo_json):
            print("Archivo de datos no encontrado. Empezando con lista vacía.")
            return

        try:
            with open(self._archivo_json, 'r', encoding='utf-8') as f:
                datos_cargados = json.load(f)
                
                #reconstruimos los objetos basados en el tipo guardado
                for item_tarea in datos_cargados:
                    if item_tarea.get('tipo') == 'Urgente':
                        tarea_obj = TareaUrgente(
                            item_tarea['descripcion'],
                            item_tarea.get('prioridad', 'Desconocida') #valor por default
                        )
                    else:
                        tarea_obj = Tarea(item_tarea['descripcion'])
                    
                    #restauramos el estado "completada"
                    if item_tarea.get('completada', False):
                        tarea_obj.marcar_completada()
                        
                    self._tareas.append(tarea_obj)
            
            print(f"Datos cargados desde {self._archivo_json}")
        except json.JSONDecodeError:
            print(f"Error: El archivo {self._archivo_json} está corrupto.")
        except IOError as e:
            print(f"Error al cargar el archivo: {e}")


#función con el menú interactivo
def mostrar_menu():
    print("\nSistema de Gestión de Tareas")
    print("1. Agregar nueva tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir (y guardar)")
    print("\n")

def main():
    #función principal que ejecuta el bucle del programa

    #inicializa el gestor
    gestor = GestorTareas(archivo_json="mis_tareas.json")
    
    #carga las tareas guardadas al inicio
    gestor.cargar_tareas()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '1':
            gestor.crear_y_agregar_tarea()
        elif opcion == '2':
            gestor.listar_tareas()
        elif opcion == '3':
            gestor.marcar_completada()
        elif opcion == '4':
            gestor.eliminar_tarea()
        elif opcion == '5':
            #guarda antes de salir
            gestor.guardar_tareas()
            print("Guardando y saliendo")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

#punto de entrada del programa
if __name__ == "__main__":
    main()