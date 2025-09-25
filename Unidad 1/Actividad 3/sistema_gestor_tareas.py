tareas = []
numero_tarea = 1

def AgregarTarea(tarea):
    global numero_tarea
    tarea = {
        "numero" : numero_tarea,
        "descripcion" : tarea,
        "estado" : "Pendiente"
    }

    tareas.append(tarea)
    print(f"tarea '{tarea['descripcion']}' agregada correctamente.")
    numero_tarea +=1 

def ListarTareas():
    tareasPendientes = False

    if not tareas:
        print("No hay tareas guardadas.")
    else:
        print("Listado de todas las tareas pendientes:")
        for t in tareas:
            if t['estado'] == "Pendiente":
                print(f"Tarea {t['numero']} ({t['estado']}): {t['descripcion']}")
                tareasPendientes = True
        
        if not tareasPendientes:
            print("No hay tareas pendientes.")
            

def CompletarTarea(numeroTareaCompletar):
    encontrada = False
    for t in tareas:
        if t['numero'] == numeroTareaCompletar:
            if t['estado'] == "Pendiente":
                t['estado'] = "Completada"
                print(f"Tarea {numeroTareaCompletar} marcada como Completada")
            else:
                print("La tarea ya ha sido completada.")
        
        encontrada =True
    
    if not encontrada:
        print("La tarea no existe.")

def EliminarTarea(numeroTareaEliminar):
    tareaEliminar = None

    for t in tareas:
        if t['numero'] == numeroTareaEliminar:
            tareaEliminar = t
            break
    if tareaEliminar:
        tareas.remove(tareaEliminar)
        print(f"Tarea {numeroTareaEliminar} eliminada correctamente.")

while(True):
    print("Gestor de tareas personales")
    print("1. Ver tareas.")
    print("2. Agregar tarea nueva.")
    print("3. Marcar tarea como completada.")
    print("4. Eliminar tarea.")
    print("5. Salir.")

    opcion = input("Selecciona una opción del menú: ")

    if opcion == "1":
        ListarTareas()
    elif opcion == "2":
        tareaNueva = input("Ingrese la nueva tarea: ")
        AgregarTarea(tareaNueva)
    elif opcion == "3":
        numeroTarea = int(input("Ingrese el número de la tarea que desea completar: "))
        CompletarTarea(numeroTarea)
    elif opcion == "4":
        numeroTarea = int(input("Ingrese el número de la tarea que desea eliminar: "))
        EliminarTarea(numeroTarea)
    elif opcion == "5":
        print("Saliendo.")
        break
    else:
        print("Opción inválida.")