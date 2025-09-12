continua = True
while continua:
    print("Menú de operaciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Salir")

    opcion = input("Elija una opción (1-3): ")

    if opcion == "1":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"La suma es: {a + b}")
    elif opcion == "2":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"La resta es: {a - b}")
    elif opcion == "3":
        print("Saliendo")
        continua = False
    else:
        print("Opción no válida")
