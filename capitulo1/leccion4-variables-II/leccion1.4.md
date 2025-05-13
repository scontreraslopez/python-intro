# Sesión 4: Variables y Operaciones Básicas

## Módulo 1: Trabajando con Números y Strings con Variables

Ahora que sabemos qué son las variables, veamos cómo operar con ellas.

### 1. Operaciones Aritméticas con Variables Numéricas

Podemos usar variables que contienen números (`int` o `float`) en operaciones aritméticas. Esto incluye números negativos.

```python
precio_producto_a = 15.50  # float
cantidad_producto_a = 3    # int
descuento = -2.00          # float (un descuento de 2 euros)

subtotal_a = precio_producto_a * cantidad_producto_a
total_con_descuento = subtotal_a + descuento # Sumar un negativo es restar

print(f"Subtotal del producto A: {subtotal_a} euros")
print(f"Total con descuento: {total_con_descuento} euros")

# Otros operadores que ya conoces:
num1 = 10
num2 = 3
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")               # División "real"
print(f"{num1} // {num2} = {num1 // num2}")             # División entera (sin decimales)
print(f"{num1} % {num2} = {num1 % num2}")               # Módulo (resto)
print(f"{num1} ** {num2} = {num1 ** num2}")             # Potencia (10 al cubo)
```

### 2. Operaciones Comunes con Strings y Variables

Las variables que contienen texto (`str`) también tienen operaciones interesantes.

- **Concatenación (`+`):** Unir dos o más strings.

    ```python
    nombre = "Ana"
    apellido = "Pérez"
    saludo_inicial = "Hola, "
    
    nombre_completo = nombre + " " + apellido # Añadimos un espacio entre nombre y apellido
    mensaje_personalizado = saludo_inicial + nombre_completo
    
    print(nombre_completo)
    print(mensaje_personalizado)
    ```

- **Multiplicación (`*`):** Repetir un string un número determinado de veces.

    ```python
    separador_simple = "-"
    separador_largo = separador_simple * 20 # Repite el guion 20 veces
    print(separador_largo)
    
    eco = "Eco! " * 3
    print(eco)
    ```

- **Obtener la longitud con `len()`:** La función `len()` nos dice cuántos caracteres tiene un string.

    ```python
    frase_motivadora = "¡A programar se aprende programando!"
    longitud_frase = len(frase_motivadora)
    print(f"La frase '{frase_motivadora}' tiene {longitud_frase} caracteres.")
    ```

- **Cambiando a mayúsculas/minúsculas (métodos de string):** Los strings tienen "funciones incorporadas" llamadas métodos. Se usan con un punto (`.`) después de la variable string.

    ```python
    mi_texto = "Python Es Genial"
    texto_mayusculas = mi_texto.upper() # Convierte todo a mayúsculas
    texto_minusculas = mi_texto.lower() # Convierte todo a minúsculas
    
    print(f"Original: {mi_texto}")
    print(f"Mayúsculas: {texto_mayusculas}")
    print(f"Minúsculas: {texto_minusculas}")
    ```

> [!NOTE]
> Hay muchos más métodos útiles para strings (`.strip()`, `.replace()`, `.find()`, etc.) que iremos descubriendo.

### 3. Carácteres Especiales en Strings

A veces, queremos incluir caracteres especiales en nuestros strings, como comillas o saltos de línea. Para esto se utilizan los **carácteres de escape**. De todos el más usado, con diferencia, es el salto de línea `\n`, que nos permite dividir un string en varias líneas sin necesidad de usar strings multilínea, ni añadir sentencias `print()` adicionales.

Aquí tienes algunos ejemplos:

```python
# Usando el carácter de escape \ para incluir comillas dentro de un string
frase_con_escape = "Ella dijo: \"¡Hola!\""
print(frase_con_escape)
# Usando \n para saltos de línea
frase_con_salto = "Hola,\n¿cómo estás?"
print(frase_con_salto)
# Usando \t para tabulaciones
frase_con_tab = "Hola,\t¿cómo estás?"
print(frase_con_tab)
```

> [!NOTE]
> El carácter de escape `\` se usa para indicar que el siguiente carácter tiene un significado especial. Por ejemplo, `\n` es un salto de línea y `\t` es una tabulación. Si quieres incluir una barra invertida en tu string, usa `\\`.

### 4. Profundizando en las f-strings: ¡La Forma Estrella de Mostrar Información!

Ya introdujimos las f-strings (cadenas formateadas) en la Lección 1 como un "TRUCAZO" (guiño 😉 al Xokas y su trucazo inmortalizado para siempre junto con Pablo Motos en un spot publicitario del Ministerio de Igualdad, historia de Internet). Son la forma más moderna y legible de incluir valores de variables (y expresiones) dentro de cadenas de texto.

Se crean poniendo una `f` justo antes de la comilla de apertura de la cadena. Dentro de la cadena, cualquier variable o expresión entre llaves `{}` será reemplazada por su valor.

```python
jugador = "Alex"
puntuacion = 1250
nivel = 5

# Forma tradicional (más verbosa)
print("El jugador " + jugador + " tiene " + str(puntuacion) + " puntos y está en el nivel " + str(nivel) + ".")

# ¡Con f-strings es mucho más limpio!
print(f"El jugador {jugador} tiene {puntuacion} puntos y está en el nivel {nivel}.")

# Podemos incluso poner expresiones dentro de las llaves:
costo_item = 25.5
cantidad = 2
print(f"Compraste {cantidad} items. Costo total: {costo_item * cantidad:.2f} euros.")
```

En el último ejemplo, `:.2f` dentro de las llaves es una forma de formatear un número float para que muestre solo dos decimales. ¡Las f-strings son muy potentes!

---

## Módulo 2: Pequeñas Demostraciones Prácticas

¡Vamos a aplicar lo aprendido!

### 1. Calculando un Promedio

Imagina que tienes tres notas de exámenes y quieres calcular el promedio.

```python
nota_examen_1 = 7.5
nota_examen_2 = 8.0
nota_examen_3 = 6.5

# Calculamos la suma de las notas
suma_notas = nota_examen_1 + nota_examen_2 + nota_examen_3

# Calculamos el promedio (suma de notas dividido por el número de notas)
numero_de_examenes = 3
promedio_final = suma_notas / numero_de_examenes

print(f"Notas: {nota_examen_1}, {nota_examen_2}, {nota_examen_3}")
print(f"Suma de notas: {suma_notas}")
print(f"Promedio final: {promedio_final}")
```

### 2. Redondeando Números con `round()`

A veces, los resultados de las divisiones tienen muchos decimales. Python nos ofrece la función `round()` para redondear un número a una cantidad específica de decimales.

```python
numero_largo = 10 / 3  # Esto da 3.3333333333333335
print(f"Número sin redondear: {numero_largo}")

numero_redondeado_2_decimales = round(numero_largo, 2) # Redondea a 2 decimales
print(f"Número redondeado a 2 decimales: {numero_redondeado_2_decimales}")

numero_redondeado_0_decimales = round(numero_largo, 0) # Redondea al entero más cercano (devuelve float)
print(f"Número redondeado a 0 decimales (queda como float): {numero_redondeado_0_decimales}")
print(f"Si lo quieres como entero: {int(round(numero_largo, 0))}")

# También puedes redondear al entero más cercano sin especificar decimales
numero_redondeado_entero = round(numero_largo) # Igual que round(numero_largo, 0)
print(f"Redondeado al entero más cercano (usando solo round()): {numero_redondeado_entero}")
```

> [!NOTE]
> `round()` tiene un comportamiento particular con los números que terminan exactamente en `.5` (ej. `round(2.5)` puede dar `2`, y `round(3.5)` puede dar `4`). Esto se llama "redondeo a par" o "redondeo bancario", y es el estándar para evitar sesgos en series largas de sumas. ¡No te preocupes demasiado por esto ahora, pero es bueno saberlo!

**Completa ahora a los ejercicios prácticos que encontrarás en `leccion1.4.py` asociados a este módulo y resuélvelos**

---

## Módulo 3: Presentación de Datos con f-strings y strings multilínea

Las f-strings son una manera muy cómoda y legible de incluir el valor de nuestras variables dentro de cadenas de texto para mostrarlas. ¡Vamos a ver cómo se usan con un ejemplo!

Imagina que queremos mostrar una ficha con algunos datos de un deportista famoso.

```python
ficha_descriptiva = f"""
+++++++++++++++++++++++++++++++++++++++++++
PERFIL DEL DEPORTISTA: {nombre_deportista.upper()}
+++++++++++++++++++++++++++++++++++++++++++
Deporte: {deporte}
País: {pais_origen}
# ... (resto del contenido) ...
+++++++++++++++++++++++++++++++++++++++++++
"""
```

La variable `ficha_descriptiva` es, fundamentalmente, un **string (`str`)**.

La "f" que precede a las comillas triples `f"""..."""` indica que es una **f-string** (formatted string literal), lo que permite incrustar expresiones como `{nombre_deportista.upper()}` dentro de ella. Pero el *resultado* de evaluar esa f-string y el tipo de dato que se almacena en `ficha_descriptiva` es un string normal (`str`).

**El aspecto multilínea:**

El hecho de que esté definida usando triples comillas (ya sean `"""` o `'''`) es lo que la convierte en un **string multilínea**. Python permite definir strings que se extienden a lo largo de varias líneas de código utilizando esta sintaxis. Todo el contenido entre las triples comillas de apertura y cierre, incluyendo los saltos de línea que escribes en el editor, se convierte en parte del string.

En el ejemplo de la ficha del deportista, `ficha_descriptiva` es una **f-string multilínea**. Al final, el tipo de dato de `ficha_descriptiva` sigue siendo un string (`str`), pero uno que contiene saltos de línea y los valores de las variables incrustadas.

---

**Ejemplo completo de Ficha Deportiva:**

```python
# --- Ficha de un Deportista Famoso ---
# Nombre del archivo: ficha_deportista.py

# Definimos las variables con la información
nombre_deportista = "Rafael Nadal"
deporte = "Tenis"
pais_origen = "España"
titulos_grand_slam = 22
es_diestro = False # True si es diestro, False si es zurdo
top_ranking_atp = 1 # Mejor posición ATP alcanzada
superficie_favorita = "Tierra Batida"

# --- Creamos la descripción usando f-strings ---
ficha_descriptiva = f"""
+++++++++++++++++++++++++++++++++++++++++++
PERFIL DEL DEPORTISTA: {nombre_deportista.upper()}
+++++++++++++++++++++++++++++++++++++++++++
Deporte: {deporte}
País: {pais_origen}
-------------------------------------------
Logros Destacados:
  Títulos de Grand Slam: {titulos_grand_slam}
-------------------------------------------
Características:
  Mano dominante (juego): {"Zurdo" if not es_diestro else "Diestro"} 
  Superficie Favorita: {superficie_favorita}
  Top Ranking ATP (ejemplo): {top_ranking_atp}
+++++++++++++++++++++++++++++++++++++++++++
"""

# Nota: Rafa Nadal es zurdo para jugar al tenis, aunque diestro para otras cosas.
# El ejemplo con 'es_diestro = True' y luego la lógica de la f-string es para mostrar el condicional.
# Si pusiéramos es_diestro = False, la salida sería "Zurdo".

# Imprimimos la ficha
print(ficha_descriptiva)
```

> [!TIP]
> En el ejemplo anterior, `{"Zurdo" if not es_diestro else "Diestro"}` es una forma compacta de decidir qué texto mostrar basado en el valor de la variable booleana `es_diestro`. Es un pequeño adelanto de las estructuras condicionales. Por ahora, si esto te confunde, podrías crear una variable extra para el texto de la mano dominante.

---

### Ejercicio Práctico: Describiendo tu Ítem Favorito de Minecraft

Ahora te toca a ti. Vamos a aplicar lo aprendido para crear una descripción de un ítem, personaje o concepto de tu videojuego, serie, libro o película favorita. Este enunciado se corresponde con el ejercicio 10 de la lección 1.4 de la práctica.

**Tu Misión:**

1. **Elige tu bloque o ítem favorito de Minecraft** (ej: Espada de Diamante, Pico de Netherita, Bloque de Pasto, un Creeper). Puedes acudir a la [wiki de Minecraft](https://minecraft.wiki/w/Item) para buscar información.
2. **Crea varias variables en Python** para almacenar algunas de sus propiedades (usa `snake_case`):
    - `nombre_item` (str)
    - `tipo_item` (str, ej: "Herramienta", "Bloque", "Mob")
    - `material` (str, ej: "Diamante", "Netherita", "Tierra", "Pólvora")
    - `puntos_ataque` (int o float, si aplica, si no, puedes omitir esta o poner `None`)
    - `durabilidad` (int, si aplica, si no, puedes omitir esta o poner `None`)
    - `es_crafteable` (bool, `True` o `False`)
    - `stack_maximo` (int, cuántos puedes tener en un solo hueco del inventario, para los no-stackables pon `1`)
    - `color_principal` (str)
3. **Crea la Ficha con f-strings:** Utiliza f-strings para construir una cadena de texto multilínea que presente estas propiedades de forma organizada y legible. Intenta que tu salida se parezca al formato del ejemplo que te daremos más abajo.
4. **Comenta tu Código:** Añade comentarios para explicar las variables que has creado.
5. **Guarda tu archivo** dentro de `leccion1.4.py`.

**Objetivo de Salida (Ejemplo para un Ítem de Minecraft):**

Intenta que la salida de tu programa, al imprimir la ficha de tu elemento, tenga una estructura similar a esta (obviamente, con los datos de **TU elemento elegido**):

```text
*****************************************
REGISTRO DEL ELEMENTO: PICO DE DIAMANTE
*****************************************
Tipo de ítem: Herramienta
-----------------------------------------
Características Principales:
  Material: Diamante
  Puntos de Ataque: 5
  Durabilidad: 1561 usos
-----------------------------------------
Información Adicional:
  ¿Es crafteable?: Sí
  Stack Máximo: 1
  Color Principal: Azul
*****************************************
```

> [!WARNING]
> PICO DE DIAMANTE es solo un ejemplo. Puedes elegir cualquier ítem, bloque o personaje de Minecraft que te guste. ¡Sé creativo!

**Instrucciones Adicionales:**

- Sé creativo con el formato de tu "ficha". Puedes usar diferentes separadores (como `*`, `-`, `=`) para hacerla visualmente atractiva. También puedes copiar el formato de la propuesta, sinceramente no hay problema.
- Recuerda usar `.upper()` o `.lower()` en alguna de tus variables dentro de la f-string si quieres cambiar cómo se muestra el texto (por ejemplo, el nombre del elemento en mayúsculas).
- Si alguna propiedad es booleana (como `es_crafteable`), puedes **(opcional - avanzado)** usar la técnica del `{"Texto si True" if variable_booleana else "Texto si False"}` dentro de la f-string para mostrar un texto más descriptivo en lugar de solo `True` o `False`.

---

## Módulo 4: Conclusión y Próximos Pasos

¡Buen trabajo! Con este par de lecciones acerca de las **variables**. Hemos aprendido a:

- Crear, nombrar (con `snake_case` 😎) y modificar variables.
- La importancia de los comentarios y docstrings.
- El tipo `None` y el concepto de tipado dinámico.
- Operar con números y strings usando variables.
- Formatear salidas de forma profesional con f-strings y strings multilínea.
- Usar caracteres de escape para incluir comillas y saltos de línea.
- Aplicarlo en pequeños cálculos y en un ejercicio final de Minecraft.

Las variables son la base para construir programas más complejos y dinámicos. En la próxima sesión, empezaremos a interactuar con el usuario pidiéndole datos con `input()` y tomaremos nuestras primeras decisiones lógicas con las estructuras condicionales (`if`, `else`). ¡La aventura se pone cada vez más interesante!

## Nota Importante: Aprendizaje y Originalidad

Ya lo sabes: es solo intentándolo que conseguimos alcanzar una aprendizaje significativo. Experimenta con las variables, prueba diferentes operaciones, comenta tu código para entenderlo mejor en el futuro. El ejercicio de Minecraft es una oportunidad para ser creativo.

>[!WARNING]
>Como siempre, el objetivo es que interiorices los conceptos. Si tienes dudas, pregunta, investiga, ¡pero el código final debe ser fruto de tu comprensión y esfuerzo! 😊
>Si me haces la del chat-gpt, o entregar un código copiado, lo que haré será evaluación por pruebas objetivas, y no por trabajos. Así que, ¡a programar se ha dicho!
