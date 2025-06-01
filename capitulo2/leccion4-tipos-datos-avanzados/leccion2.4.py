# Lección 2.4: Listas y Diccionarios a Fondo

# ¡Hola! Prepárate para dominar las listas y los diccionarios.
# Estos ejercicios aumentan progresivamente en dificultad.
# ¡Tómate tu tiempo, experimenta y verás cómo lo consigues!

# -----------------------------------------------------------------------------
# Listas: Ejercicios Básicos e Intermedios
# -----------------------------------------------------------------------------

# --- Ejercicio 1: Creando y Accediendo a tu Top 3 ---
# a) Crea una lista llamada 'mis_canciones_favoritas' con los nombres de tus 3 canciones favoritas.
# b) Imprime la lista completa.
# c) Imprime la primera canción de la lista.
# d) Imprime la última canción de la lista usando un índice negativo.

print("--- Ejercicio 1: Mi Top 3 Canciones ---")
# Tu código aquí





# --- Ejercicio 2: Modificando la Lista de Tareas ---
# a) Crea una lista 'tareas_pendientes' con tres tareas: "Lavar ropa", "Estudiar Python", "Hacer la compra".
# b) Te das cuenta de que "Estudiar Python" es más urgente. Mueve esta tarea a la primera posición
#    (índice 0) sin crear una nueva lista. Puedes hacerlo eliminándola y luego insertándola.
#    (Pista: usa .pop() o .remove() y luego .insert()).
# c) Imprime la lista de tareas actualizada.
# d) Has completado la primera tarea. Elimínala de la lista a continuación.
# e) Vuelve a imprimir la lista de tareas final.

print("\n--- Ejercicio 2: Modificando Lista de Tareas ---")
# Tu código aquí





# --- Ejercicio 3: Invitados a la Fiesta (Añadir y Comprobar) ---
# a) Crea una lista vacía llamada 'invitados_fiesta'.
# b) Pide al usuario que introduzca el nombre de 3 invitados, uno por uno (usa un bucle y '.append()').
# c) Imprime la lista de invitados.
# d) Pregunta al usuario por un nombre específico (por ejemplo, "Ana"). Tu programa deberá responder si está o no en la lista de invitados.
#    Imprime "¡Sí, [nombre_invitado] está en la lista!" o
#    "No, [nombre_invitado] no está en la lista." usando el operador 'in'.

print("\n--- Ejercicio 3: Invitados a la Fiesta ---")
# Tu código aquí





# --- Ejercicio 4: Sumando y Promediando Números de una Lista ---
# a) Crea una lista con al menos 5 números decimales (float), por ejemplo, notas de un examen.
# b) Calcula la suma de todos los números en la lista usando un bucle 'for'.
# c) Calcula el promedio de los números (suma total / cantidad de números).
# d) Imprime la lista, la suma total y el promedio (formateado a 2 decimales).

print("\n--- Ejercicio 4: Suma y Promedio de Notas ---")
# Tu código aquí





# --- Ejercicio 5: Filtrando Números Pares de una Lista ---
# a) Dada la lista: 'numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]'
# b) Crea una nueva lista vacía llamada 'numeros_pares'.
# c) Usando un bucle 'for' y un condicional 'if', recorre la lista 'numeros'.
#    Si un número es par, añádelo a la lista 'numeros_pares'.
# d) Imprime la lista original y la nueva lista 'numeros_pares'.

print("\n--- Ejercicio 5: Filtrando Números Pares ---")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Tu código aquí





# -----------------------------------------------------------------------------
# Diccionarios: Introducción y Práctica
# -----------------------------------------------------------------------------

# --- Ejercicio 6: Creando tu Primer Diccionario - Ficha Personal ---
# a) Crea un diccionario llamado 'mi_ficha_personal'.
# b) Añade los siguientes pares clave-valor:
#    - "nombre": Tu nombre (string)
#    - "edad": Tu edad (int)
#    - "ciudad_residencia": Tu ciudad (string)
#    - "toma_cafe": True (booleano)
# c) Imprime el diccionario completo.
# d) Imprime solo el valor asociado a la clave "nombre".
# e) Imprime el valor asociado a la clave "edad".

print("\n--- Ejercicio 6: Mi Ficha Personal (Diccionario) ---")
# Tu código aquí





# --- Ejercicio 7: Modificando y Añadiendo Datos a un Diccionario ---
# a) Empieza con el siguiente diccionario:
#    producto = {"codigo": "XYZ123", "nombre": "Teclado USB", "precio_euros": 19.95}
# b) El precio ha subido. Modifica el valor de la clave "precio_euros" a 22.50.
# c) Añade un nuevo par clave-valor al diccionario: "stock_disponible" con el valor 35 (int).
# d) Imprime el diccionario 'producto' actualizado para ver todos los cambios.
# e) Intenta acceder a la clave "marca". Como no existe, esto daría un KeyError.
#    Para evitarlo (sin usar try-except aún), primero comprueba si la clave "marca" existe
#    en el diccionario usando el operador 'in'.
#    Si existe, imprime su valor. Si no, imprime "La marca no está disponible."

print("\n--- Ejercicio 7: Modificando Diccionario de Producto ---")
producto = {"codigo": "XYZ123", "nombre": "Teclado USB", "precio_euros": 19.95}
# Tu código aquí





# --- Ejercicio 8: Recorriendo un Diccionario (Claves, Valores, Ítems) ---
# a) Dado el siguiente diccionario de un coche:
#    coche_info = {"marca": "Toyota", "modelo": "Corolla", "año": 2021, "color": "Rojo"}
# b) Usando un bucle 'for', imprime todas las CLAVES del diccionario.
# c) Usando un bucle 'for', imprime todos los VALORES del diccionario.
#    (Pista: puedes usar `diccionario.values()`)
# d) Usando un bucle 'for', imprime cada par CLAVE-VALOR del diccionario de forma clara.
#    (Pista: puedes usar `diccionario.items()`)
#    Ejemplo de salida para un par: "Marca del coche: Toyota"

print("\n--- Ejercicio 8: Recorriendo Diccionario de Coche ---")
coche_info = {"marca": "Toyota", "modelo": "Corolla", "año": 2021, "color": "Rojo"}
# Tu código aquí





# --- Ejercicio 9: Lista de Diccionarios - Inventario de Tienda ---
# Imagina que tienes datos de varios productos. Quieres almacenarlos en una lista
# donde cada elemento de la lista sea un diccionario representando un producto.
#
# a) Crea una lista vacía llamada 'inventario_tienda'.
# b) Crea tres diccionarios separados, cada uno representando un producto diferente.
#    Cada diccionario debe tener al menos las claves "nombre" (str), "precio" (float),
#    y "cantidad_stock" (int).
#    Ejemplo producto 1: {"nombre": "Camiseta Basic", "precio": 15.00, "cantidad_stock": 50}
# c) Añade estos tres diccionarios a la lista 'inventario_tienda' usando '.append()'.
# d) Usa un bucle 'for' para recorrer la lista 'inventario_tienda'.
#    Dentro del bucle, para cada diccionario de producto, imprime su nombre y su precio
#    de forma formateada. Ejemplo: "Producto: Camiseta Basic - Precio: 15.00 €"
# e) (Desafío) Calcula el valor total del inventario (suma del precio * cantidad_stock de cada producto).
#    Imprime este valor total.

print("\n--- Ejercicio 9: Inventario de Tienda (Lista de Diccionarios) ---")
# Tu código aquí






# --- Ejercicio 10: Traductor Simple Español-Inglés (Diccionario) ---
# a) Crea un diccionario llamado 'diccionario_traductor' con al menos 5 palabras
#    en español como claves y sus traducciones al inglés como valores.
#    Ejemplo: {"hola": "hello", "adiós": "goodbye", ...}
# b) Pide al usuario que introduzca una palabra en español que quiera traducir.
#    (Convierte la entrada del usuario a minúsculas para facilitar la búsqueda).
# c) Comprueba si la palabra introducida por el usuario existe como clave en tu 'diccionario_traductor'.
# d) Si la palabra existe, imprime su traducción al inglés.
# e) Si la palabra no existe, imprime un mensaje como: "Lo siento, no conozco la traducción de '[palabra_usuario]'."

print("\n--- Ejercicio 10: Traductor Simple Español-Inglés ---")

# Tu código aquí










# -----------------------------------------------------------------------------
# Ejercicio 11: La Conjetura de Collatz (Bucles, Condicionales y Listas)
# -----------------------------------------------------------------------------
# La Conjetura de Collatz (también conocida como problema 3n + 1) es una
# conjetura matemática que dice lo siguiente:
#
# Toma cualquier número entero positivo 'n'.
# Si 'n' es par, el siguiente término es n / 2.
# Si 'n' es impar, el siguiente término es 3n + 1.
# La conjetura afirma que, sin importar con qué número positivo comiences,
# la secuencia siempre llegará eventualmente a 1.
#
# Tu tarea:
# a) Pide al usuario que introduzca un número entero positivo.
#    (Por ahora, no te preocupes por validar si es positivo o si es un entero,
#    asume que el usuario introduce un número válido como 7, 12, etc.).
# b) Crea una lista vacía llamada 'secuencia_collatz'.
# c) Añade el número inicial del usuario a 'secuencia_collatz'.
# d) Mientras el número actual ('n') no sea igual a 1:
#    - Si 'n' es par, calcula el nuevo 'n' como n / 2.
#    - Si 'n' es impar, calcula el nuevo 'n' como 3n + 1.
#    - Añade el nuevo valor de 'n' a la lista 'secuencia_collatz'.
# e) Una vez que el bucle termine (cuando 'n' sea 1), imprime:
#    - La secuencia completa de Collatz que has almacenado en la lista.
#    - El número de pasos que tomó llegar a 1 (que sería la longitud de la lista menos 1,
#      o el número de iteraciones del bucle).
#
# Ejemplo si el usuario introduce 6:
# Secuencia de Collatz para 6: [6, 3, 10, 5, 16, 8, 4, 2, 1]
# Número de pasos para llegar a 1: 8

print("\n--- Ejercicio 11: Conjetura de Collatz ---")
# Tu código aquí





# -----------------------------------------------------------------------------
# ¡Has llegado al final de esta tanda de ejercicios!
# La conjetura de Collatz es un problema famoso y aún no resuelto en matemáticas.
# ¡Con Python, puedes explorar estas secuencias fácilmente!
# -----------------------------------------------------------------------------