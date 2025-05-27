¡Vamos a ello! La Lección 2.2 sobre `input()` es fundamental para que los programas sean interactivos.

Aquí tienes la propuesta, manteniendo el estilo y nivel de las anteriores:

---
# Lección 2.2: ¡Haciendo Programas Interactivos! Recibiendo Datos del Usuario con `input()`

¡Hola, futuros desarrolladores! En la lección anterior (2.1), aprendimos cómo hacer que nuestros programas tomen decisiones con los condicionales `if`, `elif` y `else`. Nuestros programas ya pueden seguir diferentes caminos según las circunstancias. Pero, ¿no sería genial si pudieran reaccionar a la información que el propio usuario les proporciona en el momento? 🤔

Hoy vamos a descubrir cómo hacer precisamente eso. Aprenderemos a usar la función `input()` para que nuestros programas puedan "preguntar" cosas al usuario y luego utilizar esas respuestas para hacer cosas aún más interesantes y personalizadas. ¡Prepárense para abrir un canal de comunicación con sus programas!

---
## Objetivos de Aprendizaje de esta Sesión

Al finalizar esta lección, serás capaz de:

-   Utilizar la función `input()` para solicitar y recibir datos del usuario a través de la terminal.
-   Entender que `input()` siempre devuelve los datos como una **cadena de texto (`str`)**.
-   Convertir los datos recibidos con `input()` a otros tipos de datos (como `int` o `float`) cuando sea necesario para realizar operaciones.
-   Combinar `input()` con variables, condicionales y f-strings para crear programas interactivos y dinámicos.
-   Manejar posibles errores derivados de la conversión de tipos de datos introducidos por el usuario (una primera aproximación).

---
## Módulo 1: La Función `input()` - Abriendo el Diálogo

Hasta ahora, los datos que usan nuestros programas (números, textos, etc.) los hemos escrito directamente en el código. La función `input()` nos permite obtener datos del usuario *mientras el programa se está ejecutando*.

**¿Cómo funciona?**
1.  Cuando Python encuentra `input()`, detiene la ejecución del programa.
2.  Muestra un mensaje (opcional, pero muy recomendable) en la terminal, indicando al usuario qué información se espera.
3.  Espera a que el usuario escriba algo y presione la tecla "Enter".
4.  Lo que el usuario haya escrito se devuelve como resultado de la función `input()`.

**Sintaxis:**
```python
nombre_variable = input("Mensaje que se muestra al usuario: ")
```

**Ejemplo Básico:**
```python
print("¡Bienvenido al programa de saludos!")

nombre_usuario = input("Por favor, introduce tu nombre: ")
ciudad_usuario = input("¿Y de qué ciudad eres?: ")

print(f"¡Hola, {nombre_usuario} de {ciudad_usuario}! Encantado de conocerte. 👋")
```
Si ejecutas este código, verás que el programa te hace las preguntas y espera tus respuestas en la terminal.

---
## Módulo 2: ¡Ojo! `input()` Siempre Devuelve Texto (`str`)

Este es un punto **CRUCIAL** que debemos recordar siempre: **la función `input()` devuelve SIEMPRE una cadena de texto (`str`)**, incluso si el usuario escribe números.

Observa:
```python
edad_texto = input("Introduce tu edad: ") # Si el usuario escribe 25
print(f"El tipo de dato de edad_texto es: {type(edad_texto)}")

numero_favorito_texto = input("Introduce tu número favorito: ") # Si el usuario escribe 7
print(f"El tipo de dato de numero_favorito_texto es: {type(numero_favorito_texto)}")
```
Aunque el usuario introduzca "25" o "7", las variables `edad_texto` y `numero_favorito_texto` guardarán `"25"` y `"7"` (cadenas de texto), no los números `25` y `7`.

**¿Qué problema puede causar esto?**
Si intentamos hacer operaciones matemáticas directamente con estos valores, ¡tendremos un `TypeError`!
```python
# edad_texto = input("Introduce tu edad: ") # Supongamos que el usuario introduce "30"
# edad_en_10_anhos = edad_texto + 10       # ESTO DARÁ ERROR (TypeError: can only concatenate str (not "int") to str)
# print(edad_en_10_anhos)
```
Python no puede "sumar" una cadena de texto (`"30"`) y un número entero (`10`) de esa manera.

---
## Módulo 3: Convirtiendo los Datos de `input()` - El Poder de `int()`, `float()` y `str()`

Para poder usar los datos numéricos introducidos por el usuario en cálculos, necesitamos **convertirlos** al tipo de dato correcto. Las funciones que ya conocemos para esto son nuestras aliadas:

-   `int(valor_str)`: Convierte una cadena de texto que representa un número entero a un `int`.
-   `float(valor_str)`: Convierte una cadena de texto que representa un número (entero o decimal) a un `float`.
-   `str(valor_num)`: Convierte un número a una cadena de texto (menos común justo después de `input()`, pero útil en otros contextos).

**Ejemplo Corregido para Cálculos:**
```python
edad_texto = input("Introduce tu edad: ")
edad_numero = int(edad_texto) # Convertimos la cadena a entero

edad_en_10_anhos = edad_numero + 10
print(f"Dentro de 10 años, tendrás {edad_en_10_anhos} años.")

# Ejemplo con decimales
precio_producto_texto = input("Introduce el precio del producto (€): ")
precio_producto_float = float(precio_producto_texto) # Convertimos a float

precio_con_iva = precio_producto_float * 1.21 # Suponemos un IVA del 21%
print(f"El precio final con IVA es: {precio_con_iva:.2f} €") # Usamos :.2f para formatear a 2 decimales
```

**¿Qué pasa si el usuario no escribe un número válido?**
Si intentas convertir a `int` o `float` un texto que no puede interpretarse como un número (ej. `int("hola")` o `float("veinte")`), Python generará un error llamado `ValueError`. Por ahora, asumiremos que el usuario introduce datos correctos, pero más adelante aprenderemos a manejar estos errores de forma elegante con `try-except`.

---
## Módulo 4: Combinando `input()` con Condicionales

Ahora que podemos obtener datos del usuario y convertirlos, ¡podemos usarlos en nuestras estructuras condicionales `if`, `elif`, `else` para tomar decisiones basadas en lo que el usuario escriba!

**Ejemplo: Verificador de Acceso por Edad**
```python
print("--- Sistema de Verificación de Edad ---")
edad_usuario_texto = input("Por favor, introduce tu edad: ")
edad_usuario_numero = int(edad_usuario_texto)

if edad_usuario_numero >= 18:
    print("Acceso concedido. Eres mayor de edad. ✅")
else:
    print("Acceso denegado. Debes ser mayor de 18 años. ❌")
    anhos_faltantes = 18 - edad_usuario_numero
    print(f"Te faltan {anhos_faltantes} año(s) para poder acceder.")

print("------------------------------------")
```

**Ejemplo: Pequeño Juego de Adivinar un Número (Número Fijo)**
```python
numero_secreto = 77 # El número que hay que adivinar

print("¡Bienvenido al juego de Adivina el Número!")
print("He pensado un número entre 1 y 100. ¡Intenta adivinarlo!")

intento_texto = input("Introduce tu número: ")
intento_numero = int(intento_texto)

if intento_numero == numero_secreto:
    print(f"¡Felicidades! ¡Has adivinado el número! Era el {numero_secreto}. 🎉")
elif intento_numero < numero_secreto:
    print(f"¡Casi! El número {intento_numero} es MENOR que el número secreto. Inténtalo de nuevo.")
else: # Si no es igual ni menor, entonces es mayor
    print(f"¡Casi! El número {intento_numero} es MAYOR que el número secreto. Inténtalo de nuevo.")

print("Gracias por jugar.")
```

---

## Módulo 5: ¡A Programar de Forma Interactiva! (Ejercicios)

Ahora te toca poner en práctica estas estructuras, resuelve la colección de ejercicios `leccion2.2.py` que encontrarás en el repositorio.

Si te apetece crear tu propio ejercicio y añadirlo a continuación (append), ¡adelante!. También lo tendré en cuenta.

---

## Módulo 6: Conclusión y Siguientes Aventuras

¡Felicidades! Ahora tus programas pueden "escuchar" al usuario gracias a `input()`. Has aprendido la importancia de convertir los datos recibidos, especialmente cuando necesitas realizar operaciones numéricas, y cómo combinar esta nueva herramienta con variables y condicionales para crear aplicaciones mucho más dinámicas y personalizadas.

Este es un gran paso hacia la creación de programas más complejos y útiles. En las próximas lecciones, exploraremos cómo hacer que los programas repitan acciones con los **bucles**, lo que nos permitirá procesar grandes cantidades de datos o realizar tareas repetitivas de forma eficiente.

## Nota Importante: El Usuario y los Errores

Cuando pides datos al usuario, ¡puede escribir cualquier cosa! Si tu programa espera un número y el usuario escribe "hola", tu programa fallará con un `ValueError` al intentar hacer `int("hola")`. Aunque por ahora confiamos en que el usuario colabora, en el futuro aprenderás técnicas de **manejo de errores** (`try-except`) para hacer tus programas más robustos y a prueba de entradas inesperadas. ¡Paciencia, todo a su tiempo! 😉

---

## Nota Importante: Aprendizaje y Originalidad

Recuerda que la mejor forma de aprender a programar es **haciendo**, **experimentando** y **resolviendo los pequeños problemas** que surgen. Intenta modificar los ejemplos de esta lección, crea tus propios programas que pidan datos diferentes al usuario y observa cómo puedes usar esa información. ¡No tengas miedo a que tu programa dé un error al principio! Cada error, especialmente los `TypeError` por intentar operar con un string como si fuera un número, o los `ValueError` si el usuario escribe texto cuando esperas un número, es una pista valiosa que te ayuda a entender mejor cómo funciona Python.

>[!WARNING]
>Estos ejercicios están diseñados para que desarrolles tu lógica y tu capacidad de anticipar cómo interactuará un usuario con tu programa. Intenta resolverlos por tu cuenta antes de buscar soluciones o pedir ayuda extensiva. Ya sabéis que me reservo el derecho a hacer pequeñas pruebas escritas, especialmente sobre la conversión de tipos y el manejo de la entrada del usuario, si veo cosas raras en las soluciones. ¡El verdadero aprendizaje está en el proceso de descubrir y solucionar! 😊

**Puntos Clave de esta Lección:**

* **Interactividad con `input()`:** Hemos aprendido a usar `input()` para que nuestros programas puedan "dialogar" con el usuario y recibir datos mientras se ejecutan.
* **`input()` devuelve SIEMPRE strings (`str`):** Este es un concepto crucial. Todo lo que el usuario escribe y `input()` recoge, Python lo trata inicialmente como texto.
* **Conversión de Tipos Explícita:** Para usar la entrada del usuario en cálculos numéricos, es fundamental convertirla usando `int()` (para enteros) o `float()` (para números con decimales).
* **Mensajes Claros al Usuario:** Al usar `input()`, es importante proporcionar un mensaje claro que le indique al usuario qué tipo de información se espera.
* **Combinación de Herramientas:** Hemos visto cómo `input()` se integra perfectamente con variables (para guardar lo que el usuario escribe), f-strings (para mostrar mensajes personalizados con esos datos) y condicionales (para tomar decisiones basadas en la entrada del usuario).
* **Anticipando Problemas (Introducción):** Aunque no hemos visto cómo manejarlos formalmente, hemos empezado a ser conscientes de que el usuario puede introducir datos inesperados (ej. texto en lugar de números), lo que puede llevar a errores como `ValueError`.
