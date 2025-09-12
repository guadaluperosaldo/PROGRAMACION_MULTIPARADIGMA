import math

print("Ejercicio 1 - Cálculo de áreas")
print("1. Triángulo")
print("2. Cuadrado")
print("3. Círculo")

opcion = input("Elige una figura (1-3): ")

if opcion == "1":
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area}")
elif opcion == "2":
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = lado ** 2
    print(f"El área del cuadrado es: {area}")
elif opcion == "3":
    radio = float(input("Ingrese el radio del círculo: "))
    area = math.pi * (radio ** 2)
    print(f"El área del círculo es: {area}")
else:
    print("Opción no válida")