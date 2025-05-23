# Lección 1.4: Variables II en Python
# Prácticas para la Lección 4: Aplicando Cálculos y Redondeo

# En este archivo vamos a poner en práctica lo aprendido sobre
# el cálculo de promedios y el uso de la función round() en Python.
# Lee con atención cada ejercicio y escribe el código necesario para resolverlo.
# ¡No olvides usar f-strings para presentar tus resultados de forma clara!

# Ejercicios del Módulo 1

# -----------------------------------------------------------------------------
# Ejercicio 1: Promedio de Calificaciones de un Trimestre
# -----------------------------------------------------------------------------
# Un alumno ha obtenido las siguientes calificaciones en tres asignaturas
# durante un trimestre:
#   - Matemáticas: 6.5
#   - Lengua: 7.8
#   - Inglés: 8.2
#
# a) Crea variables para cada una de estas calificaciones.
# b) Calcula la suma total de las calificaciones.
# c) Calcula la calificación promedio del alumno en este trimestre.
# d) Imprime la suma total y el promedio final, cada uno en una línea,
#    usando f-strings para que la salida sea clara. Por ejemplo:
#    "Suma de calificaciones: XX.X"
#    "Promedio del trimestre: YY.Y"

print("--- Ejercicio 1: Promedio de Calificaciones ---")
# Tu código para el Ejercicio 1 aquí:






# -----------------------------------------------------------------------------
# Ejercicio 2: Redondeo de Precios y Cálculo de IVA
# -----------------------------------------------------------------------------
# Imagina que estás calculando el precio final de un producto después de añadirle el IVA.
# El precio base de un producto es de 125.6789 euros (oye, que tiene 4 decimales porque el original estaba en USD).
# El tipo de IVA a aplicar es del 21% (es decir, 0.21).
#
# a) Crea una variable para el 'precio_base' del producto.
# b) Crea una variable para el 'tipo_iva' (almacena 0.21).
# c) Calcula el 'valor_iva' (precio_base * tipo_iva).
# d) Calcula el 'precio_final_sin_redondear' (precio_base + valor_iva).
# e) Imprime el 'valor_iva' redondeado a 2 decimales.
# f) Imprime el 'precio_final_sin_redondear'.
# g) Crea una variable 'precio_final_redondeado' que almacene el 'precio_final_sin_redondear'
#    redondeado a 2 decimales (el formato monetario estándar).
# h) Imprime el 'precio_final_redondeado'.
#
# Utiliza f-strings para todas las impresiones, indicando qué valor se muestra.

print("\n--- Ejercicio 2: Redondeo de Precios e IVA ---")
# Tu código para el Ejercicio 2 aquí:






# -----------------------------------------------------------------------------
# Ejercicio 3: Promedio de Temperaturas y Redondeo Avanzado
# -----------------------------------------------------------------------------
# Se han registrado las siguientes temperaturas máximas durante una semana (en grados Celsius):
# Lunes: 19.7
# Martes: 22.3
# Miércoles: 20.5
# Jueves: 24.1
# Viernes: 23.8
# Sábado: 25.0
# Domingo: 21.9
#
# a) Crea variables para cada temperatura diaria.
# b) Calcula la suma de todas las temperaturas.
# c) Calcula la temperatura promedio de la semana.
# d) Imprime la temperatura promedio sin redondear.
# e) Imprime la temperatura promedio redondeada a 1 decimal.
# f) Imprime la temperatura promedio redondeada al entero más cercano
#    (investiga o recuerda cómo hacerlo con round() para redondear a 0 decimales).
#
# Utiliza f-strings para presentar los resultados.

print("\n--- Ejercicio 3: Promedio de Temperaturas ---")
# Tu código para el Ejercicio 3 aquí:






# -----------------------------------------------------------------------------
# Ejercicio 4: Conversión de Unidades y Redondeo
# -----------------------------------------------------------------------------
# Quieres convertir una medida de pulgadas a centímetros.
# Sabes que 1 pulgada equivale a 2.54 centímetros.
# Tienes una medida de 17.5 pulgadas.
#
# a) Crea una variable para el factor de conversión ('pulgada_a_cm').
# b) Crea una variable para la medida en pulgadas que quieres convertir ('medida_pulgadas').
# c) Calcula la medida equivalente en centímetros.
# d) Imprime la medida original en pulgadas y la medida convertida en centímetros.
# e) Imprime la medida convertida en centímetros redondeada a 2 decimales.
# f) Imprime la medida convertida en centímetros redondeada al entero más cercano.

print("\n--- Ejercicio 4: Conversión de Unidades ---")
# Tu código para el Ejercicio 4 aquí:






# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# Ejercicio 5: Creando Saludos Personalizados (Concatenación)
# -----------------------------------------------------------------------------
# a) Crea tres variables:
#    - 'nombre_invitado' con el valor "Lucía"
#    - 'evento' con el valor "fiesta de cumpleaños"
#    - 'dia_evento' con el valor "Sábado"
# b) Usando concatenación (+), crea una frase de invitación que diga:
#    "Estimada Lucía, estás invitada a nuestra fiesta de cumpleaños el próximo Sábado."
#    Almacena esta frase en una variable llamada 'mensaje_invitacion'.
# c) Imprime la variable 'mensaje_invitacion'.
# d) Crea otra variable 'despedida' con el valor "¡Te esperamos!"
# e) Crea un 'mensaje_completo' concatenando 'mensaje_invitacion' y 'despedida'
#    (asegúrate de que haya un espacio o una nueva línea entre ellos).
# f) Imprime 'mensaje_completo'.

print("--- Ejercicio 5: Saludos Personalizados ---")
# Tu código para el Ejercicio 1 aquí:






# -----------------------------------------------------------------------------
# Ejercicio 6: Generando Patrones Simples (Multiplicación de Strings)
# -----------------------------------------------------------------------------
# a) Crea una variable llamada 'simbolo_base' y asígnale el valor "*".
# b) Crea una variable 'linea_de_simbolos' que contenga 30 veces 'simbolo_base'
#    (usando la multiplicación de strings).
# c) Imprime 'linea_de_simbolos'.
# d) Crea una variable 'palabra_eco' con el valor "Python! ".
# e) Crea una variable 'eco_repetido' que repita 'palabra_eco' 4 veces.
# f) Imprime 'eco_repetido'.

print("\n--- Ejercicio 6: Generando Patrones ---")
# Tu código para el Ejercicio 6 aquí:






# -----------------------------------------------------------------------------
# Ejercicio 7: Analizando la Longitud de Frases (len())
# -----------------------------------------------------------------------------
# a) Crea una variable 'frase_celebre' con la siguiente cita (puedes elegir otra):
#    "La imaginación es más importante que el conocimiento."
# b) Calcula la longitud de 'frase_celebre' usando la función len() y almacénala
#    en una variable llamada 'longitud_de_la_frase'.
# c) Imprime un mensaje que diga:
#    "La frase '[contenido de frase_celebre]' tiene [longitud_de_la_frase] caracteres."
#    (Usa una f-string).
# d) Crea una variable 'palabra_corta' con el valor "sol".
# e) Calcula e imprime su longitud de la misma manera.

print("\n--- Ejercicio 7: Analizando Longitudes ---")
# Tu código para el Ejercicio 7 aquí:






# -----------------------------------------------------------------------------
# Ejercicio 8: Transformando Texto (upper() y lower())
# -----------------------------------------------------------------------------
# a) Crea una variable 'titulo_original' con el valor "los Vengadores: era de ultrón".
# b) Crea una variable 'titulo_mayusculas' que contenga la versión de 'titulo_original'
#    completamente en mayúsculas.
# c) Crea una variable 'titulo_minusculas' que contenga la versión de 'titulo_original'
#    completamente en minúsculas.
# d) Imprime el 'titulo_original'.
# e) Imprime el 'titulo_mayusculas'.
# f) Imprime el 'titulo_minusculas'.
# g) Imagina que tienes un código de producto 'ax876b'. Conviértelo a mayúsculas
#    e imprímelo directamente en una f-string sin usar una variable intermedia
#    para la versión en mayúsculas.

print("\n--- Ejercicio 8: Transformando Texto ---")
# Tu código para el Ejercicio 8 aquí:




# -----------------------------------------------------------------------------
# Ejercicio 9: Combinando Operaciones con Strings
# -----------------------------------------------------------------------------
# Objetivo: Crear un "banner" simple para un nombre de usuario.
# a) Crea una variable 'nombre_usuario' con tu nombre o un nombre inventado (ej: "SuperCoder_007").
# b) Calcula la longitud de 'nombre_usuario'.
# c) Crea una variable 'linea_decorativa' que sea una cadena de guiones ('-')
#    cuya longitud sea igual a la longitud de 'nombre_usuario'. (Pista: usa multiplicación).
# d) Usando concatenación y las variables creadas (y saltos de línea '\n' si quieres
#    mejorar la presentación), crea un mensaje que muestre:
#    La línea decorativa
#    El nombre de usuario en MAYÚSCULAS
#    La línea decorativa
#    Almacena este banner en una variable 'banner_usuario'.
# e) Imprime 'banner_usuario'.
# f) Finalmente, imprime cuántos caracteres tiene el 'nombre_usuario' y cuántos
#    la 'linea_decorativa' para verificar que coinciden.

print("\n--- Ejercicio 9: Combinando Operaciones ---")
# Tu código para el Ejercicio 9 aquí:





# -----------------------------------------------------------------------------
# Ejercicio 10:  Describiendo tu Ítem Favorito de Minecraft
# -----------------------------------------------------------------------------
# Objetivo: Practicar las f-strings multilínea.
# Sigue las instrucciones que encontrarás dentro de lección 1.4.md hacia el final.
# Se espera una salida similar a la siguiente: Recuerda PICO DE DIAMANTE es un ejemplo
# de un ítem en Minecraft, pero tú puedes elegir el que quieras
# *****************************************
# REGISTRO DEL ELEMENTO: PICO DE DIAMANTE
# *****************************************
# Tipo de ítem: Herramienta
# -----------------------------------------
# Características Principales:
#   Material: Diamante
#   Puntos de Ataque: 5
#   Durabilidad: 1561 usos
# -----------------------------------------
# Información Adicional:
#   ¿Es crafteable?: Sí
#   Stack Máximo: 1
#   Color Principal: Azul
# *****************************************

print("\n--- Ejercicio 10: Describiendo tu Ítem Favorito de Minecraft ---")
# Tu código para el Ejercicio 10 aquí:


# Ejercicio 7
# a) Frase célebre
frase_celebre = "La imaginación es más importante que el conocimiento."

# b) Longitud de la frase
longitud_de_la_frase = len(frase_celebre)

# c) Imprimir frase y longitud
print(f"La frase '{frase_celebre}' tiene {longitud_de_la_frase} caracteres.")

# d) Palabra corta
palabra_corta = "sol"

# e) Imprimir longitud de palabra corta
print(f"La palabra '{palabra_corta}' tiene {len(palabra_corta)} caracteres.")
