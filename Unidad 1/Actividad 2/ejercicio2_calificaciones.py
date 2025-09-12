calificacion = float(input("Ingrese la calificación (0-100): "))

if calificacion >= 90 and calificacion <= 100:
    letra = "A"
elif calificacion >= 80 and calificacion <90:
    letra = "B"
elif calificacion >= 70 and calificacion <80:
    letra = "C"
elif calificacion >= 60 and calificacion <79:
    letra = "D"
elif calificacion < 60:
    letra = "F"
else:
    letra = "Calificación inválida"

print(f"La calificación en letra es: {letra}")