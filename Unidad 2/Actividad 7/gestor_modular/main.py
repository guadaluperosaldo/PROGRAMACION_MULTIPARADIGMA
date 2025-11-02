"""
Módulo Principal

Este es el punto de entrada del Sistema de Gestión de Tareas
Se encarga de:
1. Controlar el flujo del menú interactivo
2. Crear instancias del GestorTareas
3. Llamar a las funciones de utilidad para cargar y guardar tareas

"""

# Importamos las clases y funciones necesarias desde nuestro paquete 'modulos'
from modulos.modelo import GestorTareas, Tarea, TareaUrgente
from modulos.utilidades import guardar_tareas_json, cargar_tareas_json

# Constante para el nombre del archivo de guardado
ARCHIVO_DATOS = "mis_tareas.json"

def mostrar_menu():
    """Imprime el menú principal de opciones."""
    print("\nSistema de Gestión de Tareas")
    print("1. Agregar nueva tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("\n")

def solicitar_datos_tarea():
    """
    Pide al usuario los datos para una nueva tarea y crea el objeto

    Retorna:
        (Tarea | TareaUrgente): El objeto de tarea creado
    """
    descripcion = input("Introduce la descripción de la tarea: ")
    tipo = input("¿Es una tarea urgente? (s/n): ").lower()

    if tipo == 's':
        prioridad = input("Introduce la prioridad (Alta, Media, Baja): ")
        return TareaUrgente(descripcion, prioridad)
    else:
        return Tarea(descripcion)

def main():
    """Función principal que ejecuta el bucle del programa"""
    
    # 1. Inicialización
    gestor = GestorTareas()
    
    # 2. Cargar datos
    # Usamos el 'setter' de la propiedad 'tareas' para cargar la lista
    gestor.tareas = cargar_tareas_json(ARCHIVO_DATOS)

    # 3. Bucle principal del menú
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '1':
            # Solicitar datos y crear la tarea
            nueva_tarea = solicitar_datos_tarea()
            # Pasar el objeto al gestor
            gestor.agregar_tarea(nueva_tarea)
        
        elif opcion == '2':
            gestor.listar_tareas()
        
        elif opcion == '3':
            gestor.listar_tareas()
            try:
                idx = int(input("Introduce el número de la tarea a completar: "))
                gestor.marcar_completada(idx)
            except ValueError:
                print("Error: Debes introducir un número.")
        
        elif opcion == '4':
            gestor.listar_tareas()
            try:
                idx = int(input("Introduce el número de la tarea a eliminar: "))
                gestor.eliminar_tarea(idx)
            except ValueError:
                print("Error: Debes introducir un número.")

        elif opcion == '5':
            # 4. Guardar datos antes de salir
            # Usamos el getter de la propiedad tareas para guardar la lista
            guardar_tareas_json(ARCHIVO_DATOS, gestor.tareas)
            print("Guardando")
            break
        
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# punto de entrada del programa
if __name__ == "__main__":
    main()