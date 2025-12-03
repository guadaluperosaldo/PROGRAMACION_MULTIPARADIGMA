# Parte 1

## Función A:
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

Esta es una función pura ya que solo devuelve el promedio, no lo asigna a variables ni imprime resultados

## Función B:
contador = 0
def siguiente_id():
    global contador
    contador += 1
    return f"ID--{contador}"

Se trata de una función impura, ya que altera el valor de una variable fuera del entorno de la función.

Para hacerla pura haría esto:

def siguiente_id_pura(contadorActual):
    siguienteID = contadorActual + 1
    return f"ID--{siguienteID}"

## Función C:
def agregar_fecha(registro):
    from datetime import datetime
    registro['fecha'] = datetime.now().isoformat()
    return registro

Esta es una función impura ya que, al usar datetime.now(), el resultado siempre varía. además, altera el estado del argumento

para hacerla pura haría esto:

def agregar_fecha_pura(registro, fechaISO):
    #para evitar la modificacion del diccionario recibido como argumento, creamos uno nuevo copiando el recibido
    #los dos asterisccos sirven para copiar. y sacamos de la función la responsabilidad de generar la fecha
    nuevo_registro = {**registro, 'fecha': fecha_iso} 
    
    return nuevo_registro

## Función D:
def filtrar_positivos(numeros):
    return [n for n in numeros if n > 0]

Esta es una función pura ya que simplemente devuelve el resultado sin alterar nada exterior a la función

## Función E:
import random

def mezclar_lista(lista):
    random.shuffle(lista)
    return lista

Diría que es impura ya que modifica la lista recibida como argumento

para hacerla pura:

import random

def mezclar_lista_pura(lista):
    # random.sample toma la lista recibida y devuelve una nueva lista de longitud k
    # Aqui k es el largo de la lista recibida como argumento, obteniendo una copia mezclada completa.
    return random.sample(lista, k=len(lista))

si bien, el resultado siempre es variable, se mantiene la funcionalidad original, que es mezclar la lista, pero sin modificar la original

