# Lección 2.3: Bucles en Python

# ¡Hola! Este archivo contiene ejercicios para practicar el uso de
# bucles 'for' y 'while' en Python.
# Lee con atención cada ejercicio y escribe el código necesario para resolverlo.
# ¡No olvides guardar y ejecutar tu código para ver los resultados!
# Puedes (y debes) cambiar los valores iniciales de las variables o las entradas
# del usuario para probar diferentes casos.

# -----------------------------------------------------------------------------
# Ejercicio 1: Contador Descendente con `for`
# -----------------------------------------------------------------------------
# a) Usa un bucle `for` y la función `range()` para imprimir los números
#    del 10 al 1 (en ese orden, descendente).

print("--- Ejercicio 1: Contador Descendente con `for` ---")
# Tu código aquí





# -----------------------------------------------------------------------------
# Ejercicio 2: Suma de los Primeros N Números con `for`
# -----------------------------------------------------------------------------
# a) Pide al usuario un número entero positivo `N`.
# b) Usa un bucle `for` y `range()` para calcular la suma de todos los números
#    desde 1 hasta `N` (incluido `N`).
# c) Imprime la suma total. (Ej: si N=5, la suma es 1+2+3+4+5 = 15).

print("\n--- Ejercicio 2: Suma de los Primeros N Números con `for` ---")
# Tu código aquí





# -----------------------------------------------------------------------------
# Ejercicio 3: Adivina la Palabra (Simple, con `while`)
# -----------------------------------------------------------------------------
# a) Define una `palabra_secreta` en tu código (ej: "python" o "informatica").
# b) Pide al usuario que intente adivinar la palabra.
# c) Mientras la palabra introducida por el usuario (ignorando mayúsculas/minúsculas)
#    no sea igual a la `palabra_secreta`:
#    - Imprime "Incorrecto. Intenta de nuevo: ".
#    - Vuelve a pedir al usuario que introduzca la palabra.
# d) Cuando adivine la palabra, imprime "¡Felicidades, has adivinado la palabra!".
#    (Pista: usa el método .lower() en la entrada del usuario y en tu palabra secreta
#    para comparar sin importar mayúsculas/minúsculas).

print("\n--- Ejercicio 3: Adivina la Palabra (con `while`) ---")
# Tu código aquí





# -----------------------------------------------------------------------------
# Ejercicio 4: Menú de Opciones con `while`
# -----------------------------------------------------------------------------
# Presenta al usuario un menú simple con opciones:
#   Menú:
#   1. Saludar
#   2. Despedirse
#   3. Salir
#
# a) Pide al usuario que elija una opción (como texto: "1", "2" o "3").
# b) Mientras la opción no sea "3" (Salir):
#    - Si la opción es "1", imprime "¡Hola! ¿Qué tal?".
#    - Si la opción es "2", imprime "¡Hasta luego! Que tengas un buen día.".
#    - Si es cualquier otra cosa (que no sea 1, 2 o 3), imprime "Opción no válida. Inténtalo de nuevo.".
#    - IMPORTANTE: Dentro del bucle, después de procesar la opción, vuelve a mostrar el menú
#      y a pedir al usuario que elija una nueva opción.
# c) Cuando el usuario elija "3", imprime "Saliendo del programa..." y el bucle debe terminar.

print("\n--- Ejercicio 4: Menú de Opciones con `while` ---")
# Tu código aquí






# -----------------------------------------------------------------------------
# Ejercicio 5: Contador de Vocales en una Frase (con `for`)
# -----------------------------------------------------------------------------
# a) Pide al usuario que introduzca una frase.
# b) Inicializa un contador de vocales a 0.
# c) Usa un bucle `for` para recorrer cada letra de la frase.
# d) Dentro del bucle, comprueba si la letra (convertida a minúscula para simplificar)
#    es una vocal ('a', 'e', 'i', 'o', 'u').
# e) Si es una vocal, incrementa el contador.
# f) Después del bucle, imprime el número total de vocales encontradas.

print("\n--- Ejercicio 5: Contador de Vocales en una Frase ---")
# Tu código aquí





# -----------------------------------------------------------------------------
# Ejercicio 6: Validación de Entrada Numérica con `while`
# -----------------------------------------------------------------------------
# Queremos asegurarnos de que el usuario introduce un número entre 1 y 10 (ambos incluidos).
# a) Pide al usuario que introduzca un número. Convierte la entrada a entero.
# b) Mientras el número introducido NO esté entre 1 y 10:
#    - Imprime "Número fuera de rango. Inténtalo de nuevo."
#    - Vuelve a pedir al usuario que introduzca un número (y conviértelo).
# c) Cuando el usuario finalmente introduzca un número válido, imprime:
#    "¡Gracias! Has introducido el número [número_válido], que está en el rango."
# (Nota: Este ejercicio no maneja el caso de que el usuario introduzca texto en lugar de un número.
#  Eso requeriría try-except, que veremos más adelante).

print("\n--- Ejercicio 6: Validación de Entrada Numérica con `while` ---")
# Tu código aquí






# -----------------------------------------------------------------------------
# Ejercicio 7: Cálculo de Factorial (Ampliación del Ejercicio 6)
# -----------------------------------------------------------------------------
# Tomando el número validado del ejercicio anterior (asegúrate de que esté entre 1 y 10),
# vamos a calcular su factorial. El factorial de un número N (escrito como N!)
# es el producto de todos los enteros positivos menores o iguales a N.
# Ejemplos:
#   3! = 3 * 2 * 1 = 6
#   5! = 5 * 4 * 3 * 2 * 1 = 120
#   0! se define como 1 (aunque para este ejercicio, el número validado será >= 1)
#
# a) (Asume que ya tienes el 'numero_valido' del Ejercicio 6, que está entre 1 y 10).
#    Si no has completado el Ejercicio 6, primero pide un número y asegúrate que esté
#    en el rango de 1 a 10 para este ejercicio.
# b) Inicializa una variable 'factorial' a 1 (este es el valor base para la multiplicación).
# c) Usa un bucle (elige `for` o `while`, aunque `for` con `range` puede ser más directo aquí)
#    para multiplicar 'factorial' por cada número desde 1 hasta 'numero_valido'.
# d) Imprime el resultado en un formato claro, por ejemplo:
#    "El factorial de [numero_valido] (es decir, [numero_valido]!) es [resultado_factorial]."

print("\n--- Ejercicio 7: Cálculo de Factorial ---")




# -----------------------------------------------------------------------------
# ¡Has completado los ejercicios sobre bucles!
# Sigue practicando para dominar la repetición en tus programas.
# Considera cómo podrías combinar bucles con las estructuras condicionales
# que ya conoces para resolver problemas más complejos.
# -----------------------------------------------------------------------------