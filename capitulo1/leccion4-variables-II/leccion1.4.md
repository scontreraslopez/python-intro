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

* **Concatenación (`+`):** Unir dos o más strings.

    ```python
    nombre = "Ana"
    apellido = "Pérez"
    saludo_inicial = "Hola, "
    
    nombre_completo = nombre + " " + apellido # Añadimos un espacio entre nombre y apellido
    mensaje_personalizado = saludo_inicial + nombre_completo
    
    print(nombre_completo)
    print(mensaje_personalizado)
    ```

* **Multiplicación (`*`):** Repetir un string un número determinado de veces.

    ```python
    separador_simple = "-"
    separador_largo = separador_simple * 20 # Repite el guion 20 veces
    print(separador_largo)
    
    eco = "Eco! " * 3
    print(eco)
    ```

* **Obtener la longitud con `len()`:** La función `len()` nos dice cuántos caracteres tiene un string.

    ```python
    frase_motivadora = "¡A programar se aprende programando!"
    longitud_frase = len(frase_motivadora)
    print(f"La frase '{frase_motivadora}' tiene {longitud_frase} caracteres.")
    ```
* **Cambiando a mayúsculas/minúsculas (métodos de string):** Los strings tienen "funciones incorporadas" llamadas métodos. Se usan con un punto (`.`) después de la variable string.
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

### 3. Profundizando en las f-strings: ¡La Forma Estrella de Mostrar Información!
Ya introdujimos las f-strings (cadenas formateadas) en la Lección 1 como un "TRUCAZO". Son la forma más moderna y legible de incluir valores de variables (y expresiones) dentro de cadenas de texto.
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

## Módulo 4: Pequeños Proyectos Prácticos

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

---

## Módulo 5: ¡A Minar Conocimiento! Ejercicio Minecraft con f-strings

¡Minecraft al rescate para practicar! Imagina que queremos describir un objeto del juego usando variables y f-strings.

**Tu Misión:**
1.  Elige tu bloque o ítem favorito de Minecraft (ej: Espada de Diamante, Pico de Netherita, Bloque de Pasto, un Creeper).
2.  Crea varias variables en Python para almacenar algunas de sus propiedades (usa `snake_case`):
    * `nombre_item` (str)
    * `tipo_item` (str, ej: "Herramienta", "Bloque", "Mob")
    * `material` (str, ej: "Diamante", "Netherita", "Tierra", "Pólvora")
    * `puntos_ataque` (int o float, si aplica, si no, puedes omitir esta o poner `None`)
    * `durabilidad` (int, si aplica, si no, puedes omitir esta o poner `None`)
    * `es_crafteable` (bool, `True` o `False`)
    * `stack_maximo` (int, cuántos puedes tener en un solo hueco del inventario)
3.  Utiliza **f-strings** para crear una descripción detallada y bien formateada del ítem, mostrando todas sus propiedades de una manera legible. ¡Sé creativo con la presentación!
4.  Añade comentarios a tu código explicando qué estás haciendo.

**Ejemplo de inicio (puedes elegir otro ítem y más propiedades):**
```python
# --- Propiedades de mi Ítem de Minecraft ---
# Nombre del archivo: minecraft_item.py

# TODO: Elegir un ítem y completar sus propiedades
nombre_item = "Espada de Diamante"
tipo_item = "Herramienta/Arma"
material = "Diamante"
puntos_ataque = 7
durabilidad = 1561 # Número de usos antes de romperse
es_crafteable = True
stack_maximo = 1

# --- Descripción con f-strings ---
# TODO: Crear una descripción chula usando f-strings y las variables de arriba

descripcion_item = f"""
=========================================
FICHA TÉCNICA DEL ÍTEM: {nombre_item.upper()}
=========================================
Tipo: {tipo_item}
Material Principal: {material}
-----------------------------------------
Estadísticas de Combate:
  Puntos de Ataque: {puntos_ataque}
  Durabilidad: {durabilidad} usos
-----------------------------------------
Información Adicional:
  ¿Es crafteable?: {"Sí" if es_crafteable else "No"}
  Stack Máximo en Inventario: {stack_maximo}
=========================================
"""

# Imprimimos la descripción
print(descripcion_item)

# ¡Ahora prueba con otro ítem y añade más detalles si quieres!
# Por ejemplo, podrías añadir una variable 'rareza' (str) o 'efectos_especiales' (str)
```

> [!TIP]
> En el ejemplo anterior, `{"Sí" if es_crafteable else "No"}` es una forma compacta de poner "Sí" si la variable booleana es `True`, y "No" si es `False`. ¡Es un pequeño adelanto de las estructuras condicionales que veremos pronto! Por ahora, puedes usarlo o simplemente imprimir `True`/`False`.

Guarda tu archivo como `minecraft_item.py`.

---

## Módulo 6: Conclusión y Próximos Pasos

¡Excelente trabajo, mineros del código! Hoy hemos añadido una herramienta fundamental a nuestro cinturón: las **variables**. Hemos aprendido a:
- Crear, nombrar (con `snake_case` 😎) y modificar variables.
- La importancia de los comentarios y docstrings.
- El tipo `None` y el concepto de tipado dinámico.
- Operar con números y strings usando variables.
- Formatear salidas de forma profesional con f-strings.
- Aplicarlo en pequeños cálculos y en un divertido ejercicio de Minecraft.

Las variables son la base para construir programas más complejos y dinámicos. En la próxima sesión, empezaremos a interactuar con el usuario pidiéndole datos con `input()` y tomaremos nuestras primeras decisiones lógicas con las estructuras condicionales (`if`, `else`). ¡La aventura se pone cada vez más interesante!

## Nota Importante: Aprendizaje y Originalidad

Ya lo sabes: la práctica hace al maestro. Experimenta con las variables, prueba diferentes operaciones, comenta tu código para entenderlo mejor en el futuro. El ejercicio de Minecraft es una oportunidad para ser creativo.

>[!WARNING]
>Como siempre, el objetivo es que interiorices los conceptos. Si tienes dudas, pregunta, investiga, ¡pero el código final debe ser fruto de tu comprensión y esfuerzo! 😊
```

**Consideraciones adicionales para ti:**

* **Ritmo:** Esta lección también es densa, especialmente el Módulo 1 que introduce muchos conceptos nuevos sobre variables. Asegúrate de dar tiempo para que los asimilen.
* **Ejercicio Minecraft:** Anímales a ser creativos y a buscar información real de los ítems si son fans, ¡eso aumenta el engagement!
* **Tipado Dinámico y Errores:** Puedes preparar algún ejemplo sencillo donde el cambio de tipo de una variable lleve a un `TypeError` si no se maneja con cuidado, para reforzar esa idea.
* **Operaciones con Strings:** Decidí incluir `len()` y los métodos `.upper()`/`.lower()` porque son muy comunes y fáciles de entender. Puedes ajustar esto según veas.

Espero que esta Lección 3 se ajuste a lo que tenías en mente y sea de gran utilidad para tus alumnos. ¡Seguimos!