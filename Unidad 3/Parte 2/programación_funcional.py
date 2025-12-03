#función para determinar si la venta es válida (monto mayor a 100)
def es_venta_valida(venta):
    """Retorna True si la venta cumple la condición"""
    return venta['monto'] > 100

#función para crear un nuevo diccionario y aplicar el impuesto
def aplicar_impuesto_y_formato(venta):

    return {
        'id': venta['id'],
        'monto_original': venta['monto'],
        'monto_final': venta['monto'] * 1.15
    }

# función para sumar total
def calcular_suma_total(ventas_procesadas):
    """Suma los montos finales de una lista de ventas ya procesadas"""
    return sum(venta['monto_final'] for venta in ventas_procesadas)

# función principal que llama a las otras
def procesar_ventas_pura(ventas):
    """
    Entrada: lista de ventas
    Salida: lista procesada y total
    """
    ventas_filtradas = [v for v in ventas if es_venta_valida(v)]

    resultado = [aplicar_impuesto_y_formato(v) for v in ventas_filtradas]

    total = calcular_suma_total(resultado)
    
    return resultado, total

#PARA PROBAR

#diccionario con datos de prueba
ventas_ejemplo = [ 
    {'id': 1, 'monto': 50},
    {'id': 2, 'monto': 150},
    {'id': 3, 'monto': 200},
    {'id': 4, 'monto': 80},
    {'id': 5, 'monto': 300},
]

lista_final, gran_total = procesar_ventas_pura(ventas_ejemplo)

print(f"Lista: {lista_final}")

print(f"Total: {gran_total}")