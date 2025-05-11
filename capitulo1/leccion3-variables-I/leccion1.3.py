# Lección 1.3: Variables en Python

# Ejercicios del Módulo 1

# ¡Hola! Este módulo contiene ejercicios para practicar los conceptos
# sobre variables que hemos visto en la Lección 3.
# Lee con atención cada ejercicio y escribe el código necesario para resolverlo.
# ¡No olvides guardar y ejecutar tu código para ver los resultados!


# -----------------------------------------------------------------------------
# Ejercicio 1: Creación y Asignación de Variables
# -----------------------------------------------------------------------------
# a) Crea una variable llamada 'nombre_planeta' y asígnale el valor "Tierra".
# b) Crea una variable llamada 'lunas_planeta' y asígnale el número de lunas que tiene la Tierra.
# c) Imprime ambas variables en la consola, cada una en una línea.

print("--- Ejercicio 1 ---")
# Tu código para el Ejercicio 1 aquí:






# -----------------------------------------------------------------------------
# Ejercicio 2: Nombrando Variables con snake_case
# -----------------------------------------------------------------------------
# Las siguientes variables están mal nombradas o usan convenciones incorrectas.
# Corrige sus nombres para que sigan la convención snake_case
#
#   VariableIncorrecta1 = "Valor Ejemplo"
#   segundavariableMUYLARGA = 100
#   Tercera Variable = True
#   4variable = 4.0 # ¡Ojo con cómo empiezan los nombres de variables!
#
# Después de corregirlas y asignarles un valor, imprímelas.

print("\n--- Ejercicio 2 ---")
# Tu código para el Ejercicio 2 aquí (arreglas las variables incorrectas):

VariableIncorrecta1 = "Valor Ejemplo"
segundavariableMUYLARGA = 100
Tercera Variable = True
4variable = 4.0


# -----------------------------------------------------------------------------
# Ejercicio 3: Modificando el Valor de una Variable
# -----------------------------------------------------------------------------
# a) Crea una variable llamada 'puntos_jugador' y asígnale un valor inicial de 500.
# b) El jugador gana 250 puntos. Actualiza 'puntos_jugador' para reflejar esto.
# c) El jugador gasta 100 puntos en la tienda. Actualiza 'puntos_jugador' de nuevo.
# d) Imprime el valor de 'puntos_jugador' después de cada modificación.

print("\n--- Ejercicio 3 ---")
# Tu código para el Ejercicio 3 aquí:





# -----------------------------------------------------------------------------
# Ejercicio 4: Tipos de Datos en Variables y type()
# -----------------------------------------------------------------------------
# a) Crea cuatro variables con los siguientes nombres y valores:
#    - 'titulo_libro' con el valor "El Principito"
#    - 'numero_paginas' con el valor 96
#    - 'precio_libro' con el valor 9.99
#    - 'es_best_seller' con el valor True
# b) Para cada variable, imprime su valor y su tipo usando la función type(). 
#    Ejemplo de salida esperada para una variable:
#    Valor: El Principito, Tipo: <class 'str'>

print("\n--- Ejercicio 4 ---")
# Tu código para el Ejercicio 4 aquí:




# -----------------------------------------------------------------------------
# Ejercicio 5: El Tipo Especial None
# -----------------------------------------------------------------------------
# a) Crea una variable llamada 'color_secundario_bandera' y asígnale el valor None,
#    indicando que una bandera podría no tener un segundo color.
# b) Imprime el valor de la variable y su tipo.
# c) Luego, reasigna la variable 'color_secundario_bandera' con el valor "Verde".
# d) Vuelve a imprimir su valor y su tipo para ver cómo ha cambiado.

print("\n--- Ejercicio 5 ---")
# Tu código para el Ejercicio 5 aquí:








# -----------------------------------------------------------------------------
# Ejercicio 6: Tipado Dinámico de Python
# -----------------------------------------------------------------------------
# a) Crea una variable llamada 'dato_flexible' y asígnale un número entero. Imprime su valor y su tipo con type().
# b) Reasigna a continuación 'dato_flexible' con una cadena de texto. Imprime su valor y tipo.
# c) Reasigna a continuación 'dato_flexible' con un valor booleano. Imprime su valor y tipo.
# d) Intenta sumar 'dato_flexible' (que ahora es booleano) con el número 5.
#    Observa el resultado o el error. ¿Por qué crees que pasa esto?
#    (Puedes comentar la línea que da error después de observarlo para que el script continúe).


print("\n--- Ejercicio 6 ---")
# Tu código para el Ejercicio 6 aquí:








# -----------------------------------------------------------------------------
# Ejercicio 7: Declaración Múltiple de Variables
# -----------------------------------------------------------------------------
# a) En una sola línea, asigna los valores "Rojo", "Amarillo" y "Verde" a tres
#    variables llamadas 'color_primario', 'color_secundario' y 'color_terciario' respectivamente.
# b) Imprime las tres variables en una sola línea.
# c) En otra línea, asigna el valor 0 a tres variables llamadas 'contador_a',
#    'contador_b' y 'contador_c' simultáneamente.
# d) Imprime estas tres variables contador.

print("\n--- Ejercicio 7 ---")
# Tu código para el Ejercicio 7 aquí:






# Ejercicios del Módulo 2

# Continuamos para bingo 🎰. Este módulo se centra en cómo y cuándo usar comentarios
# en Python. Los comentarios son esenciales para que tu código sea comprensible.
# Lee cada ejercicio y sigue las instrucciones.

# -----------------------------------------------------------------------------
# Ejercicio 8: Comentarios de una Línea (#)
# -----------------------------------------------------------------------------
# a) El siguiente bloque de código calcula el área de un círculo.
#    Añade comentarios de una línea para explicar qué hace cada variable importante
#    y qué hace la fórmula principal.

print("--- Ejercicio 8 ---")

radio = 5
pi = 3.14159 
area_circulo = pi * (radio ** 2)

print(f"El área de un círculo con radio {radio} es: {area_circulo}")


# b) A continuación, hay una línea de código que calcula el perímetro.
#    Sin embargo, está "comentada" (Python la ignora).
#    "Descoméntala" (elimina el # del principio) para que se ejecute.
#    Luego, añade un comentario explicativo para esta línea.

# perimetro_circulo = 2 * pi * radio
print(f"El perímetro de un círculo con radio {radio} es: {perimetro_circulo}")


# c) La siguiente línea de código es innecesaria o un error.
#    Coméntala para que Python la ignore y el programa no intente ejecutarla.
#    Añade un breve comentario explicando por qué la has comentado (ej. "Cálculo incorrecto" o "Variable no usada").

variable_temporal_erronea = radio / pi
print(f"Resultado de un cálculo extraño: {variable_temporal_erronea}")







# -----------------------------------------------------------------------------
# Ejercicio 9: Docstrings ("""...""" o '''...''')
# -----------------------------------------------------------------------------
# a) A continuación hay una función simple que saluda a una persona.
#    Añade un docstring descriptivo a esta función. El docstring debe explicar:
#    - Qué hace la función.
#    - Qué parámetro espera (`nombre_persona`) y su tipo de dato.
#    - Qué devuelve (en este caso, no devuelve nada explícitamente, solo imprime).

print("\n--- Ejercicio 9 ---")

def saludar_persona(nombre_persona):

    mensaje = f"¡Hola, {nombre_persona}! Encantado de conocerte."
    print(mensaje)

saludar_persona("Alex")
saludar_persona("Sofía")

# b) En el siguiente bloque vamos a practicar el comentar y descomentar código.
#    ¡Cambio en los requisitos! Ya no nos interesa el volumen del cono, ahora queremos el del cilindro.
#    Descomenta el bloque de código que calcula el volumen de un cilindro.
#    Comenta el bloque de código que calcula el volumen de un cono.

print("\nBloque para comentar/descomentar:")

# Descomenta este bloque para probarlo. ASEGURARSE DE QUE 'radio' Y 'altura_cilindro' ESTÉN DEFINIDOS.

# altura_cilindro = 10
# volumen_cilindro = pi * (radio ** 2) * altura_cilindro # V = pi * r^2 * h
# print(f"El volumen de un cilindro con radio {radio} y altura {altura_cilindro} es: {volumen_cilindro}")

altura_cono = 10
volumen_cono = (1/3) * pi * (radio ** 2) * altura_cono
print(f"El volumen de un cono con radio {radio} y altura {altura_cono} es: {volumen_cono}")


# -----------------------------------------------------------------------------
# ¡Buen trabajo con los comentarios! Son una parte esencial de escribir
# código claro y mantenible.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# ¡Felicidades por completar los ejercicios sobre variables!
# Guarda este archivo ya que los subiremos luego todos juntos
# -----------------------------------------------------------------------------
