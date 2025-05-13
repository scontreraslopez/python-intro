# Sesión 3: Introducción las Variables y Comentarios

¡Hola de nuevo, clase! En las sesiones anteriores, preparamos nuestro entorno, conocimos los tipos de datos básicos y aprendimos a pelearnos con la consola y entender los errores. ¡Buen trabajo! Hoy, vamos a explorar una de las herramientas más poderosas de la programación: las **variables**.

Aprenderemos a crear "cajas" para guardar información, a ponerles nombres con estilo, a dejar notas claras en nuestro código con comentarios y a trabajar de forma más avanzada con los textos usando las geniales f-strings. ¡Prepárense para organizar y potenciar sus programas!

## Objetivos de Aprendizaje de esta Sesión

Al finalizar esta lección, serás capaz de:

- Entender qué son las variables, cómo crearlas, asignarles valores y modificarlas.
- Aplicar la convención `snake_case` para nombrar variables de forma legible.
- Utilizar comentarios de una línea (`#`) y docstrings (`"""..."""`) para documentar tu código.
- Recordar los tipos de datos básicos y cómo se asignan a variables.
- Comprender y utilizar el tipo especial `None`.
- Entender el concepto de tipado dinámico en Python.
- Realizar operaciones básicas con variables numéricas y de tipo string (concatenación, multiplicación).
- Usar f-strings de manera efectiva para formatear e incluir variables en cadenas de texto.
- Declarar múltiples variables en una sola línea.
- Aplicar estos conocimientos en ejercicios prácticos, como calcular promedios y redondear.

## Módulo 1: Las Variables - Nuestras Cajas para Guardar Información

Imagina que estás cocinando y necesitas guardar ingredientes como la harina, el azúcar o la sal. No los dejas esparcidos por la mesa, ¿verdad? Usas recipientes y les pones una etiqueta para saber qué contienen. Sobre todo con la azúcar y la sal, si no te toca meter el dedo para probar... ¡puede ser un desastre!

![Dedo señalando, ilustrando la importancia de etiquetar bien las variables](/assets/images/1.3-dedo.png)

En programación, las **variables** son como esos recipientes etiquetados: son **espacios en la memoria del ordenador** donde guardamos datos (números, texto, etc.) y les damos un nombre para poder referirnos a ellos y usarlos más tarde. El ordenador guarda la posición de la variable y su valor, y nosotros solo tenemos que recordar el nombre, como si fuera una etiqueta, porque las direcciones de memorias tienen esta pinta `0x7fa9e40b`... ¡son un lío! 😅

### 1. ¿Qué es una Variable? Creación y Asignación

Una variable se crea en el momento en que le asignas un valor por primera vez. El símbolo que usamos para asignar un valor a una variable es el signo igual (`=`).

```python
# Creamos una variable llamada 'edad_companero' y le asignamos el valor 16
edad_companero = 16

# Creamos una variable llamada 'nombre_mascota' y le asignamos el valor "Sparky"
nombre_mascota = "Sparky"

# Ahora podemos usar estas variables, por ejemplo, para imprimirlas
print(edad_companero)
print(nombre_mascota)
```

### 2. Nombrando Variables: La Convención `snake_case`

Elegir buenos nombres para las variables es crucial para que tu código sea fácil de leer y entender (¡tanto por ti en el futuro como por otros!). En Python, la convención más extendida para nombrar variables (y funciones, que veremos más adelante) es `snake_case`:

- Se usan letras minúsculas.
- Si el nombre se compone de varias palabras, se separan por guiones bajos (`_`).

**Ejemplos de `snake_case`:**

```python
mi_variable_favorita = "Python"
numero_de_vidas = 3
velocidad_maxima_permitida = 120
primer_apellido = "García"
```

**¿Por qué es importante?**:

- **Legibilidad:** `velocidad_maxima_permitida` es mucho más fácil de leer que `velocidadmaximapermitida` o `VelocidadMaximaPermitida` (esto último se llama CamelCase y se usa en otros lenguajes, como el **Java** o para nombres de Clases en Python, ¡pero no para variables comunes!).
- **Consistencia:** Si todos seguimos la misma convención, es más fácil entender el código de otros y colaborar.

> [!IMPORTANT]
> **Reglas adicionales para nombres de variables:**
>
>- Deben empezar con una letra o un guion bajo (`_`). No pueden empezar con un número.
>- Solo pueden contener caracteres alfanuméricos (letras A-Z, a-z, números 0-9) y guiones bajos.
>- Los nombres de variables son "case-sensitive", es decir, `edad` y `Edad` serían dos variables diferentes. (¡Pero recuerda, usa `snake_case` en minúsculas!).
>- No uses palabras reservadas de Python como nombres de variables (ej. `print`, `if`, `for`, `while`, `True`, `False`, `None`, etc.).

### 3. Modificando el Valor de una Variable

Una vez que una variable ha sido creada, puedes cambiar su valor simplemente asignándole uno nuevo.

```python
puntos_partida = 100
print("Puntos iniciales:", puntos_partida)

puntos_partida = 150 # Modificamos el valor
print("Puntos después de bonus:", puntos_partida)

puntos_partida = puntos_partida - 20 # Le restamos 20 al valor actual
print("Puntos después de penalización:", puntos_partida)
```

### 4. Tipos de Datos en Variables (Repaso)

Como vimos en la Lección 2, los datos tienen tipos (`int`, `float`, `str`, `bool`). Cuando asignas un valor a una variable, esta "adopta" el tipo del dato que contiene. Aquí tienes ejemplos de cada tipo:

```python
cantidad_manzanas = 12         # int
precio_por_manzana = 0.5       # float
saludo = "Buenos días"         # str
es_fin_de_semana = False       # bool

print(type(cantidad_manzanas))
print(type(precio_por_manzana))
print(type(saludo))
print(type(es_fin_de_semana))
```

### 5. El Tipo Especial `None`

En Python, existe un tipo de dato especial llamado `NoneType`, cuyo único valor posible es `None`. Se utiliza para representar la ausencia de un valor o un valor nulo. Como nuestro `NULL` en SQL. Es importante entender que `None` **no es lo mismo que `0`**, ni que una cadena de texto vacía `""`, ni que `False`.

```python
ganador_del_sorteo = None # Aún no hay ganador
print(ganador_del_sorteo)
print(type(ganador_del_sorteo))

# Más adelante, podríamos asignarle un valor
# ganador_del_sorteo = "Laura"
# print(ganador_del_sorteo)
```

### 6. El Tipado Dinámico de Python: Flexibilidad y Precauciones

Python es un lenguaje de **tipado dinámico**. Esto significa que no necesitas declarar el tipo de una variable antes de usarla (como sí ocurre en otros lenguajes como Java o C++). Además, una misma variable puede contener datos de diferentes tipos en diferentes momentos del programa.

```python
mi_dato = 10
print(mi_dato, type(mi_dato)) # Es un int

mi_dato = "Ahora soy un texto"
print(mi_dato, type(mi_dato)) # Ahora es un str

mi_dato = True
print(mi_dato, type(mi_dato)) # Y ahora un bool
```

Esta flexibilidad es muy cómoda, pero también requiere **máxima precaución**. Si intentas hacer una operación con una variable esperando que sea de un tipo cuando en realidad es de otro, ¡obtendrás un `TypeError`!

```python
valor = "5"
# resultado = valor + 2 # Esto daría TypeError: can only concatenate str (not "int") to str
# Deberías convertirlo primero si quieres sumar numéricamente:
resultado_numerico = int(valor) + 2
print("Resultado numérico:", resultado_numerico)
```

### 7. Declaración Múltiple de Variables

Python permite asignar el mismo valor a varias variables a la vez, o diferentes valores a diferentes variables en una sola línea.

```python
# Asignar el mismo valor a múltiples variables
x = y = z = 0
print(x, y, z)

# Asignar diferentes valores a diferentes variables
nombre, edad, ciudad = "Ana", 25, "Valencia"
print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")
```

---

## Módulo 2: Comentando Nuestro Código - Dejando Pistas Claras

Los comentarios son texto que Python ignora al ejecutar el programa, pero que son increíblemente útiles para los humanos que leen el código. Sirven para explicar qué hace una parte del código, por qué se tomó una decisión, o para dejar recordatorios.

### 1. Comentarios de una Línea (`#`)

Ya los hemos usado. Cualquier cosa que escribas en una línea después del símbolo `#` es un comentario. También podemos usar la palabra clave `TODO` para marcar tareas pendientes. Recuerda que los comentarios son esenciales para mantener el código legible y comprensible.

```python
# Esto es un comentario de una línea
temperatura_celsius = 25 # Podemos poner un comentario al final de una línea de código
# TODO: Recordar verificar la fórmula de conversión más adelante
```

**Buenas prácticas para comentarios de una línea:**

- Úsalos para explicar partes complejas o decisiones no obvias.
- Usa la palabra clave `TODO` (del inglés To do...) para marcar tareas pendientes.
- No comentes lo obvio (ej. `numero = 5 # Asigno 5 a numero`).
- Mantenlos actualizados si cambias el código.

### 2. Docstrings (`"""..."""` o `'''...'''`)

Los docstrings (cadenas de documentación) son comentarios multilínea que se escriben encerrados entre triples comillas (ya sean dobles `"""` o simples `'''`).
Tienen un propósito especial: documentar qué hacen los módulos (archivos `.py`), funciones, clases y métodos.

```python
"""
Este es un docstring a nivel de módulo (archivo).
Puede ocupar varias líneas y explica el propósito general de este script.
Por ejemplo, este script podría ser para calcular áreas de figuras geométricas.
"""

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Esta es una función que toma la base y la altura como parámetros
    y devuelve el área calculada. Es un ejemplo de docstring para una función.
    """
    area = base * altura
    return area

# Aunque los docstrings se usan principalmente para lo anterior,
# técnicamente también puedes usarlos para comentarios multilínea generales:
"""
Esto también es un comentario
que ocupa varias líneas, aunque
no esté documentando una función o módulo.
Pero para esto, es más común usar múltiples #.
"""
# O así:
# Esto también es un comentario
# que ocupa varias líneas,
# usando el símbolo # en cada una.

print(calcular_area_rectangulo(5, 10))
```

>![INFO]
> Más de detalle de los docstrings en [Real Python Documenting Python Code](https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings).
> Y la que a mi juicio es la mejor guía de estilo para los docstrings: [Numpy docstring style](https://numpydoc.readthedocs.io/en/latest/format.html) 

Por ahora, quédate con que los `#` son para comentarios cortos y los `"""Docstrings"""` para explicaciones más largas y, sobre todo, para la documentación formal de partes de tu código (algo que será más relevante cuando definamos nuestras propias funciones).

---

## Nota Importante: Aprendizaje y Originalidad

Ya lo sabes: la práctica hace al maestro. Experimenta con las variables, prueba diferentes operaciones, comenta tu código para entenderlo mejor en el futuro.

>[!WARNING]
>Como siempre, el objetivo es que interiorices los conceptos. Si tienes dudas, pregunta, investiga, ¡pero el código final debe ser fruto de tu comprensión y esfuerzo! 😊
```

