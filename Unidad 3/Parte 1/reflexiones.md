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

# Parte 4
1. ¿Qué significa que una función sea "pura"?
    Significa que cumple con ciertas condiciones como: evitar modificar elementos fuera de la función, evitar imprimir resultados o mensajes. Se dice también que es determinista, es decir, que devuelve lo mismo cada vez. Un ejemplo en la vida cotidiana podría ser meter una tela al agua. sabes que no importa si es lunes o martes, si hace frío o calor, la tela saldrá mojada

2. En la parte 3, ¿por qué 'crear_transformador' retorna una función en lugar de aplicar directamente la transformación? ¿Qué ventaja ofrece ese diseño?
    Porque en lugar de realizar el cálculo inmediatamente, separamos la configuración (definir qué haremos, como en esta ocasión que fue multiplicar por 2), de la ejecución, que es cuando tenemos ya los datos. este diseño nos da la ventaja de que podemos hacer este código modular y reutilizarlo, al guardar una función en una variable y usarla en diferentes partes del programa

3. ¿Qué dificultades encontraste al convertir el código imperativo a funcional en la parte 2? ¿Qué parte fue más difícil y cómo la resolviste?
    Creo que podría decir que estoy acostumbrada a programar en imperativo, siempre pensando en los pasos para lograr hacer algo. la parte complicada fue cambiar ese pensamiento a pensar de cómo hacerlo a qué quiero hacer. lo resolví deteniéndome a pensar en cómo podría hacer lo mismo pero sin modificar nada externo, qué parametros tendría que mandar a mi función y cómo puedo preparar los datos para que mi función vaya al grano de su objetivo

4. Si tuvieras que explicar la diferencia entre programación imperativa y funcional a alguien que no programa, ¿qué analogía usarías?
    Hacer una comida casera contra un alimento procesado. En la comida casera uno mismo manupula los ingredientes y va paso a paso. Un alimento procesado, producido masivamente, es creado mediante maquinaria al que se le pasan los ingredientes y hace el trabajo que le corresponde, y luego le pasa su resultado a la siguiente, por ejemplo, me imagino una máquina mezclando ingredientes que le pasa los ingredientes mezclados a una máquina que amasa. Ya amasado, se la pasa ahora a la máquina que reparte el total de la masa. todo el proceso dividido en tareas pequeñas y específicas, sin afectar a elementos ajenos.