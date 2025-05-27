# Lección 2.1: Condicionales I en Python

# ¡Hola! Este archivo contiene ejercicios para practicar el uso de
# estructuras condicionales (if, elif, else) en Python.
# Lee con atención cada ejercicio y escribe el código necesario para resolverlo.
# ¡No olvides guardar y ejecutar tu código para ver los resultados!
# Puedes (y debes) cambiar los valores iniciales de las variables para probar diferentes casos.

# -----------------------------------------------------------------------------
# Ejercicio 1: Verificador de Mayoría de Edad
# -----------------------------------------------------------------------------
# a) Crea una variable llamada 'edad_persona' y asígnale un valor entero.
# b) Escribe una estructura condicional que imprima "Eres mayor de edad."
#    si la edad es 18 o más.
# c) Si la edad es menor a 18, debe imprimir "Aún eres menor de edad."

print("--- Ejercicio 1: Verificador de Mayoría de Edad ---")
edad_persona = 20 # Prueba con diferentes edades para asegurarte que funciona antes de entregarlo

# Tu código para el Ejercicio 1 aquí:





# -----------------------------------------------------------------------------
# Ejercicio 2: Acceso a una Atracción
# -----------------------------------------------------------------------------
# Para subir a una atracción de un parque temático, se debe medir 1.60 metros o más.
# a) Crea una variable 'altura_persona_metros' y asígnale un valor (ej. 1.55, 1.60, 1.75).
# b) Escribe una estructura condicional que imprima "¡Puedes subir a la atracción!"
#    si la altura es suficiente.
# c) Si no es suficiente, debe imprimir "Lo sentimos, no tienes la altura mínima para subir."
#    y además, en otra línea, "Te faltan X metros para poder subir." donde X es la diferencia.
#    (Calcula y muestra esa diferencia).

print("\n--- Ejercicio 2: Acceso a una Atracción ---")
altura_persona_metros = 1.90 # Prueba con diferentes alturas

# Tu código para el Ejercicio 2 aquí:






# -----------------------------------------------------------------------------
# Ejercicio 3: Positivo, Negativo o Cero
# -----------------------------------------------------------------------------
# a) Crea una variable 'numero_evaluar' y asígnale un valor entero (prueba con positivo, negativo y cero).
# b) Escribe una estructura condicional (usando if-elif-else) que determine e
#    imprima si el número es "Positivo", "Negativo" o "Cero".

print("\n--- Ejercicio 3: Positivo, Negativo o Cero ---")
numero_evaluar = 0 # Prueba con 10, -5, 0

# Tu código para el Ejercicio 3 aquí:






# -----------------------------------------------------------------------------
# Ejercicio 4: Calificación Escolar Detallada
# -----------------------------------------------------------------------------
# Basado en una nota numérica de 0 a 10, queremos obtener una calificación en texto:
#   - Menos de 5: "Suspenso"
#   - Entre 5 (incluido) y menos de 7: "Aprobado"
#   - Entre 7 (incluido) y menos de 9: "Notable"
#   - Entre 9 (incluido) y 10 (incluido): "Sobresaliente"
#   - Cualquier otra nota (menor que 0 o mayor que 10): "Nota inválida"
#
# a) Crea una variable 'nota_numerica' y asígnale un valor (ej. 4.5, 6.0, 8.9, 10, 11, -2).
# b) Escribe una estructura if-elif-else que imprima la calificación en texto correspondiente.

print("\n--- Ejercicio 4: Calificación Escolar Detallada ---")
nota_numerica = 9.5 # Prueba con diferentes notas

# Tu código para el Ejercicio 4 aquí:






# -----------------------------------------------------------------------------
# Ejercicio 5: Tipo de Triángulo según sus Ángulos
# -----------------------------------------------------------------------------
# (Este es un poco más avanzado, ¡un pequeño desafío!)
# Un usuario introduce la medida de un ángulo de un triángulo (simplificaremos
# y supondremos que los otros dos ángulos son iguales para este ejercicio,
# o que solo evaluamos uno).
# Queremos determinar si ese ángulo corresponde a un triángulo:
#   - Rectángulo (el ángulo es 90 grados)
#   - Obtusángulo (el ángulo es mayor a 90 grados)
#   - Acutángulo (el ángulo es menor a 90 grados)
#   - No válido (si el ángulo es 0, negativo, o 180 o más)
#
# a) Crea una variable 'angulo_principal' y asígnale un valor.
# b) Escribe una estructura if-elif-else para clasificarlo.

print("\n--- Ejercicio 5: Tipo de Triángulo según un Ángulo ---")
angulo_principal = 90 # Prueba con 45, 90, 120, 0, 180

# Tu código para el Ejercicio 5 aquí:






# -----------------------------------------------------------------------------
# Ejercicio 6: Descuento por Volumen de Compra
# -----------------------------------------------------------------------------
# Una tienda ofrece descuentos según el total de la compra:
#   - Compras menores a 50€: Sin descuento.
#   - Compras entre 50€ (incluido) y 100€ (no incluido): 5% de descuento.
#   - Compras de 100€ (incluido) o más: 10% de descuento.
#
# a) Crea una variable 'total_compra_original' y asígnale un valor.
# b) Calcula el 'descuento_aplicado' (en euros) y el 'precio_final_a_pagar'.
# c) Imprime un resumen:
#    - Total original
#    - Porcentaje de descuento aplicado (ej. "Descuento: 5%") o "Sin descuento"
#    - Valor del descuento en euros (ej. "Ahorras: X.XX €") o nada si no hay descuento.
#    - Precio final
#
# Ejemplo de salida si la compra es de 80€:
#   Total Original: 80.00 €
#   Descuento: 5%
#   Ahorras: 4.00 €
#   Precio Final: 76.00 €
#
# Ejemplo de salida si la compra es de 30€:
#   Total Original: 30.00 €
#   Sin descuento
#   Precio Final: 30.00 €

print("\n--- Ejercicio 6: Descuento por Volumen de Compra ---")
total_compra_original = 150.0 # Prueba con 30, 80, 100, 150

# Tu código para el Ejercicio 6 aquí:







# -----------------------------------------------------------------------------
# Ejercicio 7: Verificador de Acceso VIP (Opcional)
# -----------------------------------------------------------------------------
#  El ejercicio opcional significa que puedes omitirlo si no te sientes cómodo con él.
#  Si lo intentas y resuelves correctamente, pues lo tendré en cuenta como un extra. 
#  Para acceder a una zona VIP de un concierto, se debe cumplir UNA de estas condiciones:
#   1. Ser mayor de 25 años Y tener una entrada VIP.
#   2. Ser un invitado especial (independientemente de la edad o tipo de entrada).
#
# a) Crea tres variables booleanas: 'es_mayor_25', 'tiene_entrada_vip', 'es_invitado_especial'.
#    Asígnales valores True/False para probar diferentes escenarios.
# b) Escribe una estructura condicional que imprima "Acceso VIP concedido" o
#    "Acceso VIP denegado" basándose en las condiciones.
#    (Pista: necesitarás usar 'and' y 'or').

print("\n--- Ejercicio 7: Verificador de Acceso VIP (Opcional) ---")
es_mayor_25 = True
tiene_entrada_vip = False
es_invitado_especial = True # Prueba diferentes combinaciones

# Tu código para el Ejercicio 7 aquí:




