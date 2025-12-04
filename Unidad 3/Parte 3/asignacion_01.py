def crear_transformador(funcion_transformacion):
    """
    Crea una nueva lista transformando cada elemento
    """
    def transformador(lista):
        #creamos una nueva lista para evitar modificar la original (función pura)
        return [funcion_transformacion(x) for x in lista]
    return transformador

def crear_filtro(predicado):
    """
    Crea una nueva lista solo con los elementos que dan True
    """
    def filtro(lista):
        #solo incluimos x si predicado(x) es True
        return [x for x in lista if predicado(x)]
    return filtro

def crear_reductor(funcion_reduccion, valor_inicial):
    """
    Reduce una lista a un solo valor acumulado
    """
    def reductor(lista):
        acumulado = valor_inicial
        for elemento in lista:
            #actualizamos el acumulador usando la función recibida
            acumulado = funcion_reduccion(acumulado, elemento)
        return acumulado
    return reductor

def componer(*funciones):
    """
    Aplica funciones en secuencia 
    """
    def pipeline(dato_inicial):
        resultado = dato_inicial
        # Recorremos cada función en el orden que fueron recibidas
        for funcion in funciones:
            resultado = funcion(resultado)
        return resultado
    return pipeline

#PRUEBA DE LA IMPLEMENTACION
#ejecutar el programa para ver el resultado

if __name__ == "__main__":
    numeros = [1, -2, 3, -4, 5, -6, 7, 8, -9, 10]

    # prueba de la composición
    pipeline = componer(
        crear_filtro(lambda x: x > 0),
        crear_transformador(lambda x: x ** 2),
        crear_reductor(lambda acc, x: acc + x, 0)
    )

    resultado_final = pipeline(numeros)
    print(f"Resultado: {resultado_final}")
    #debería ser: 1 + 9 + 25 + 49 + 64 + 100 = 248