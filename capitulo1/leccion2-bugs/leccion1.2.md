# Sesión 2: Tipos de Datos Fundamentales y el Arte de Depurar Errores

¡Hola de nuevo, programadores! En la sesión anterior, configuramos nuestro entorno y escribimos nuestro primer "Hola, Mundo". ¡Un gran paso! Hoy, vamos a sumergirnos un poco más en los cimientos de Python: los **tipos de datos primitivos**. Además, aprenderemos algo súper importante: cómo Python nos habla cuando cometemos errores y qué tipos de "gazapos" podemos encontrar. ¡Entender los errores es el primer paso para solucionarlos y convertirnos en mejores programadores!

## Objetivos de Aprendizaje de esta Sesión

Al finalizar esta lección, serás capaz de:

- Identificar y utilizar los tipos de datos primitivos en Python: enteros (`int`), decimales (`float`), cadenas de texto (`str`) y booleanos (`bool`).
- Usar la función `type()` para determinar el tipo de dato de una variable o valor.
- Comprender la diferencia entre errores de sintaxis, errores en tiempo de ejecución y errores lógicos.
- Interpretar los mensajes de error básicos que Python proporciona (tracebacks).
- Depurar (corregir) un programa sencillo que contenga diversos tipos de errores.

## Módulo 1: Los Bloques de Construcción - Tipos de Datos Primitivos

Imagina que estás construyendo con LEGO. Tienes diferentes tipos de piezas, ¿verdad? En Python, cuando manejamos información, también tenemos diferentes "tipos de piezas" o **tipos de datos**. Los más básicos o "primitivos" son:

### 1. Enteros (`int`)

Representan números enteros, tanto positivos como negativos, sin parte decimal.
Ejemplos:

```python
edad = 16
goles_en_contra = -3
numero_de_alumnos = 25
temperatura_actual = 0

print(edad)
print(goles_en_contra)
```

Este tipo de datos es como `INTEGER` en SQLite.

### 2. Números Decimales (`float`)

Representan números que tienen una parte decimal. El nombre "float" viene de "punto flotante" (floating point), que es la forma en que el ordenador los almacena internamente.
Ejemplos:

```python
precio_kilo_manzanas = 2.75
pi_aproximado = 3.14159
altura_metros = 1.82
saldo_cuenta = -10.50

print(precio_kilo_manzanas)
print(pi_aproximado)
```

> [!NOTE]
> En Python (y en muchos lenguajes de programación), el separador decimal es el **punto `.`** y no la coma `,`.

Este tipo de datos es como `REAL` en SQLite.

### 3. Cadenas de Texto (`str`)

Representan secuencias de caracteres: letras, números, símbolos... ¡Básicamente, cualquier texto! Ya las usamos en la Lección 1 con `print()`. Se definen usando comillas simples (`'...'`) o comillas dobles (`"..."`). Da igual usar una u otra, pero asegúrate de ser consistente. Si empiezas con comillas simples, termina con comillas simples. Si empiezas con dobles, termina con dobles.

Ejemplos:

```python
nombre_asignatura = "Programación en Python"
mensaje_bienvenida = '¡Hola, exploradores del código!'
codigo_postal = "46001" # Aunque sean números, si van entre comillas, son texto.

print(nombre_asignatura)
print(mensaje_bienvenida)
print("El código postal es: " + codigo_postal) # Podemos "sumar" (concatenar) cadenas
```

### 4. Booleanos (`bool`)

Representan uno de dos valores posibles: verdadero (`True`) o falso (`False`). Son fundamentales para tomar decisiones en nuestros programas. Sus nombres siempre empiezan con mayúscula.
Ejemplos:

```python
hoy_llueve = False
eres_mayor_de_edad = True
python_es_divertido = True
el_sol_es_verde = False

print(hoy_llueve)
print(5 > 3) # Esto evaluará a True
print(10 == 20) # Esto evaluará a False (== es para comparar igualdad)
```

### Descubriendo Tipos con `type()`

Python tiene una función muy útil llamada `type()` que nos dice de qué tipo es un dato o una variable.

```python
numero_entero = 10
texto_ejemplo = "Soy un texto"
decimal_ejemplo = 7.5
booleano_ejemplo = False

print(type(numero_entero))
print(type(texto_ejemplo))
print(type(decimal_ejemplo))
print(type(booleano_ejemplo))
print(type(25))
print(type("Otro texto más"))
```

Al ejecutar esto, verás salidas como `<class 'int'>`, `<class 'str'>`, etc.

---

## Módulo 2: ¡Ups! Comprendiendo los Errores en Python

Programar es un proceso creativo y, como en todo proceso creativo, ¡los errores ocurren! Son una parte normal y muy valiosa del aprendizaje. Python intenta ayudarnos (no sé yo si con demasiado acierto... a veces es bastante críptico) señalando dónde y qué tipo de error ha encontrado. Vamos a conocer los más comunes:

### 1. Errores de Sintaxis (`SyntaxError`)

Estos errores ocurren cuando escribimos código que Python simplemente no puede entender porque no sigue sus reglas gramaticales. Es como escribir una frase en castellano con las palabras desordenadas o mal escritas. Python leerá el código y, si encuentra un `SyntaxError`, se detendrá antes de ejecutar nada.

**Ejemplos comunes:**

- Paréntesis sin cerrar: `print("Hola"`
- Comillas sin cerrar: `print('Adiós)`
- Mezclar comillas de forma incorrecta: `print("Esto es un error')` (empiezas con dobles, cierras con simple)
- Palabras clave mal escritas: `primt("Error")` (en lugar de `print`)
- Uso incorrecto de operadores: `edad = 16 +` (falta algo después del +)

Cuando ocurre un `SyntaxError`, Python suele señalar la línea (o cerca de ella) donde detectó el problema.

```python
# Ejemplo de SyntaxError (NO lo copies tal cual si no quieres un error inmediato)
# print("Olvidé cerrar el paréntesis...
# nombre = "Ana' # Comillas mezcladas
```

### 2. Errores en Tiempo de Ejecución (Runtime Errors)

Estos errores ocurren mientras el programa ya se está ejecutando. La sintaxis es correcta (Python entendió las instrucciones), pero algo sucede que impide que el programa continúe.

Imagina que le das a un robot instrucciones gramaticalmente perfectas como "Divide 10 entre 0". El robot entiende la frase, pero no puede realizar la acción.

Algunos tipos comunes de errores en tiempo de ejecución:

- **`TypeError`**: Ocurre cuando intentas realizar una operación en un tipo de dato que no la soporta.

    ```python
    # Ejemplo de TypeError
    # print("Tu edad es: " + 16) # No puedes sumar directamente un str con un int
    # Para corregirlo: print("Tu edad es: " + str(16)) # str() convierte el número a texto
    ```

- **`NameError`**: Ocurre cuando intentas usar una variable o función que no ha sido definida previamente.

    ```python
    # Ejemplo de NameError
    # print(mi_nombre_es) # Si 'mi_nombre_es' no existe, dará error
    ```

- **`ZeroDivisionError`**: Ocurre, como su nombre indica, cuando intentas dividir un número entre cero.

    ```python
    # Ejemplo de ZeroDivisionError
    # resultado = 10 / 0
    ```

- **`IndexError`** (los veremos más con listas/cadenas): Intentar acceder a una posición que no existe.
- **`ValueError`**: Se usa una función con un valor del tipo correcto pero un valor inapropiado. Ejemplo: `int("hola")`.

Python nos da un "Traceback" (rastreo) que nos indica la línea donde ocurrió el error y el tipo de error.

> [!NOTE]
> El detalle de todos los errores se puede consutar en la [documentación oficial de Python](https://docs.python.org/3/library/exceptions.html). Pero no es necesario memorizar todos los tipos de errores. Lo importante es entender que existen y que Python nos ayuda a identificarlos.

### 3. Errores Lógicos

Estos son los que más dolor de cabeza dan. El programa se ejecuta sin errores de sintaxis ni de tiempo de ejecución, pero **no hace lo que esperabas que hiciera**. El resultado es incorrecto.

Python no puede ayudarte directamente con estos, porque él ha hecho exactamente lo que le has pedido. ¡Aquí es donde la experiencia, capacidades analíticas y pericia entran en juego!

**Ejemplos comunes:**

- Usar un operador incorrecto: `suma_edades = edad1 - edad2` (querías sumar, pero restaste).
- Error en una fórmula matemática: `area_triangulo = base * altura / 3` (olvidaste que es `/ 2`).
- Condiciones lógicas mal planteadas (lo veremos más adelante).

### Leyendo los Mensajes de Error (Tracebacks)

Cuando Python encuentra un error en tiempo de ejecución, te muestra un "Traceback". Es importante aprender a leerlo:

1. **Tipo de Error:** Te dice qué clase de error es (ej. `TypeError`, `NameError`).
2. **Archivo y Línea:** Te indica el archivo (`.py`) y el número de línea donde ocurrió el error.
3. **Línea de Código:** A menudo te muestra la propia línea de código que causó el problema.
4. **Mensaje:** Una breve descripción del error.

Ejemplo de Traceback (simplificado):

``` text
Traceback (most recent call last):
  File "mi_programa.py", line 5, in <module>
    resultado = "edad: " + 25
TypeError: can only concatenate str (not "int") to str
```

Esto nos dice: En el archivo `mi_programa.py`, en la línea 5, hay un `TypeError` porque intentaste concatenar un `str` con un `int`.

---

## Módulo 3: ¡Modo Detective! Ejercicio de Caza de Errores

¡Es hora de poner a prueba tus nuevas habilidades de depuración!

![Detective Python](/assets/images/detective_python.jpeg)

**Tu Misión:**

Copia el siguiente código en un nuevo archivo Python (puedes llamarlo `leccion2.py`). El programa intenta realizar algunos cálculos y mostrar información sobre un estudiante ficticio, pero está plagado de errores de diferentes tipos.

Tu tarea es:

1. Ejecutar el código.
2. Observar el primer error que Python te señale.
3. Identificar qué tipo de error es (Sintaxis, TypeError, NameError, Lógico...).
4. Corregir el error.
5. Guardar y ejecutar de nuevo.
6. Repetir hasta que el programa se ejecute sin errores y produzca la **salida esperada** (ver más abajo).

[!NOTE]
> Recuerda que la línea que empieza con `#` es un **comentario**. Python la ignora, es decir que el código que aparezca en la misma línea que la almohadilla no se ejecutará. Sirve para que los humanos dejemos notas en el código.

**Código con "Sorpresas":**

```python
# leccion1.2.py - ¡A corregir se ha dicho!

nombre_estudiante = "Carlos Santana"
asignaturas_matriculadas = 5
precio_asignatura = "150.50" # Repasar el tipo de dato
nota_media_esperada = 8.5

print("Bienvenido, " + nombre_estudiant)

total_matricula = asignaturas_matriculadas + coste_por_asignatura
print("El coste total de la matrícula es: ", total_matricula

# Queremos calcular si aprueba con la nota esperada (consideramos aprobado >= 5)
aprueba = nota_media_esperada > 5.0
print("¿Aprobará con la nota esperada?", aprueba)

# Cálculo de un descuento del 10% sobre la matrícula. Este descuento tiene varias cosas sospechosas...
descuento = 0,10 # 10%
matricula_con_descuento = total_matricula + (total_matricula * descuento)
print("La matrícula con un supuesto 'descuento' es: ", matricula_con_descuento)

print(mensaje_despedida) # ¿Hemos definido este mensaje?

# Y un último saludo
print("¡Gracias por usar el programa!) # ¿Están bien los paréntesis y comillas?
```

**Salida Esperada (Una vez corregido y con la lógica del descuento arreglada):**
(La salida exacta del costo puede variar ligeramente por cómo se manejan los floats, pero debe ser coherente)

```text
Bienvenido, Carlos Santana
El coste total de la matrícula es: 752.5
¿Aprobará con la nota esperada? True
La matrícula con descuento es: 677.25
¡Gracias por usar el programa!
```

(Para la última línea de "Gracias...", si `mensaje_despedida` no tiene un valor asignado, simplemente no debería intentar imprimirse o deberías definirlo con un mensaje adecuado para que no dé `NameError`. Para este ejercicio, si no se pide explícitamente un mensaje de despedida en la salida, la opción más simple es comentar o eliminar la línea `print(mensaje_despedida)` si causa un NameError que no forma parte de un error lógico a corregir para la salida esperada).

**Pistas:**

- Revisa bien los nombres de las variables.
- Asegúrate de que los tipos de datos son compatibles para las operaciones que realizas (especialmente sumas y multiplicaciones). Puede que necesites convertir tipos con `int()`, `float()`, `str()`.
- Los errores lógicos no harán que el programa falle, pero el resultado no será el correcto. ¡Piensa en lo que el programa *debería* hacer! (Ej: un descuento *reduce* el precio).
- No te olvides de la sintaxis básica: comillas, paréntesis...

---

## Módulo 4: Conclusión y Próximos Pasos

¡Felicidades, detective! Si has llegado hasta aquí y has logrado que el programa funcione como se esperaba, has dado un paso enorme. Hoy hemos aprendido sobre:

- Los tipos de datos `int`, `float`, `str` y `bool`.
- Cómo usar `type()` para verificar los tipos.
- Los diferentes tipos de errores: `SyntaxError`, errores en tiempo de ejecución (`TypeError`, `NameError`, etc.) y errores lógicos.
- La importancia de leer los mensajes de error (Tracebacks).
- Y, lo más importante, ¡hemos practicado la depuración!

En la próxima sesión, profundizaremos en las **variables**, cómo pedir datos al usuario con `input()` y empezaremos a tomar decisiones en nuestros programas con estructuras condicionales.

Para preparar la entrega, símplemente guarda el código corregido como `leccion2.py` y asegúrate de que funciona correctamente. No olvides comentar el código para que sea más fácil de entender.

## Nota Importante: Aprendizaje y Originalidad

Como siempre, estos ejercicios están diseñados para que desarrolles tu propia lógica y capacidad de resolución. Los errores son parte del camino. Si te atascas, revisa la teoría, los ejemplos y, sobre todo, ¡lee con atención los mensajes de error de Python!

>[!WARNING]
>Me reservo el derecho de hacer pequeñas pruebas o preguntas para asegurar que los conceptos fundamentales se están asimilando correctamente. ¡El objetivo es que aprendas a "pensar en Python"! 😊
