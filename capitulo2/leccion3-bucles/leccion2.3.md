# Lección 2.3: ¡Automatizando Tareas! Introducción a los Bucles (`for` y `while`)

¡Saludos, chicos! 💻 En las lecciones anteriores, hemos aprendido a dar instrucciones secuenciales, guardar datos en variables, tomar decisiones con condicionales e interactuar con el usuario. Pero, ¿qué pasa si queremos que nuestro programa realice una misma acción muchas veces? ¿O que recorra una lista de elementos uno por uno? Escribir la misma línea de código cien veces no parece muy eficiente, ¿verdad? 😅

Aquí es donde entran en juego los **bucles**. Los bucles son estructuras de control que nos permiten repetir un bloque de código múltiples veces, ya sea un número determinado de veces o mientras se cumpla una cierta condición. ¡Son la clave para la automatización y para trabajar con grandes cantidades de datos! Hoy exploraremos los dos tipos principales de bucles en Python: el bucle `for` y el bucle `while`.

---

## Objetivos de Aprendizaje de esta Sesión

Al finalizar esta lección, serás capaz de:

- Entender el concepto de iteración y la necesidad de los bucles en programación.
- Conocer y utilizar el bucle `for` para iterar sobre secuencias (como cadenas de texto o rangos de números).
- Utilizar la función `range()` para generar secuencias numéricas para el bucle `for`.
- Aprender la sintaxis y el funcionamiento del bucle `while` para repetir código mientras una condición sea verdadera.
- Entender cómo controlar la ejecución de un bucle `while` mediante la actualización de una variable de control.
- Identificar el peligro de los bucles infinitos y cómo evitarlos.
- Aplicar los bucles `for` y `while` en ejercicios prácticos.

---

## Módulo 1: El Bucle `for` - Recorriendo Elementos Uno por Uno

El bucle `for` en Python es ideal para **iterar sobre los elementos de una secuencia** en orden. Una secuencia puede ser una cadena de texto (donde cada carácter es un elemento), una lista (que veremos en la siguiente lección), o un rango de números generado por la función `range()`.

**Sintaxis Básica:**

```python
for variable_iteradora in secuencia:
    # Bloque de código que se ejecuta para cada elemento de la secuencia
    # Este bloque DEBE estar indentado
    print(variable_iteradora) # Ejemplo: imprimir el elemento actual

print("El bucle for ha terminado.") # Esta línea se ejecuta después de recorrer todos los elementos
```

En cada "vuelta" o **iteración** del bucle, la `variable_iteradora` toma el valor del siguiente elemento de la `secuencia`.

### 1.1. Iterando sobre Cadenas de Texto

Podemos recorrer cada carácter de un string:

```python
nombre_heroe = "Batman"
print(f"Analizando el nombre: {nombre_heroe}")

for letra in nombre_heroe:
    print(f"Letra actual: {letra}")

print("¡Análisis completado!")
```

### 1.2. Iterando con `range()` - Secuencias de Números

La función `range()` es muy útil con los bucles `for` porque genera una secuencia de números que podemos recorrer.

- `range(limite_superior)`: Genera números desde 0 hasta `limite_superior - 1`.

    ```python
    print("Contando hasta 4 (sin incluirlo):")
    for numero in range(4): # Genera 0, 1, 2, 3
        print(numero)
    ```

- `range(inicio, limite_superior)`: Genera números desde `inicio` hasta `limite_superior - 1`.

    ```python
    print("\nNúmeros del 2 al 5 (sin incluirlo):")
    for numero in range(2, 5): # Genera 2, 3, 4
        print(numero)
    ```

- `range(inicio, limite_superior, paso)`: Genera números desde `inicio` hasta `limite_superior - 1`, incrementando en `paso`.

    ```python
    print("\nNúmeros pares del 0 al 10 (incluido el 10 si es par, hasta 11 para incluirlo):")
    for numero in range(0, 11, 2): # Genera 0, 2, 4, 6, 8, 10
        print(numero)

    print("\nCuenta atrás desde 5 hasta 1:")
    for numero in range(5, 0, -1): # Genera 5, 4, 3, 2, 1
        print(numero)
    ```

**Ejemplo - Tabla de Multiplicar:**

Veamos ahora un ejemplo en el que utilizamos un bucle `for` para crear una tabla de multiplicar. Este ejemplo es interactivo y permite al usuario elegir el número del que quiere ver la tabla de multiplicar.

```python
tabla_del_texto = input("¿De qué número quieres la tabla de multiplicar?: ")
tabla_del = int(tabla_del_texto) # Convertimos la entrada a entero

print(f"\n--- Tabla de Multiplicar del {tabla_del} ---")
for i in range(1, 11): # Queremos multiplicar del 1 al 10
    resultado = tabla_del * i
    print(f"{tabla_del} x {i} = {resultado}")
```

---

## Módulo 2: El Bucle `while` - Repetir Mientras se Cumpla una Condición

El bucle `while` (mientras) ejecuta un bloque de código repetidamente **mientras una condición especificada sea `True`**. Es útil cuando no sabemos de antemano cuántas veces necesitamos repetir el código, sino que la repetición depende de que algo siga siendo cierto.

[!WARNING]
> Cuidado con los bucles infinitos. Primer aviso🙎🏻‍♂️

**Sintaxis Básica:**

```python
while condicion_a_evaluar:
    # Bloque de código que se ejecuta mientras la condicion_a_evaluar sea True
    # Este bloque DEBE estar indentado
    print("La condición sigue siendo verdadera.")
    # ¡IMPORTANTE! Dentro del bucle, algo debe ocurrir que eventualmente
    # haga que la condicion_a_evaluar se vuelva False, o tendremos un bucle infinito.

print("La condición se volvió falsa. El bucle while ha terminado.")
```

**Funcionamiento:**

1. Python evalúa la `condicion_a_evaluar`.
2. Si es `True`, ejecuta el bloque de código indentado.
3. Una vez que el bloque termina, Python vuelve al paso 1 y reevalúa la condición.
4. Si la condición es `False`, el bucle termina y el programa continúa con el código que sigue después del bucle.

**Ejemplo - Contador Simple:**

```python
contador = 1 # 1. Inicializamos una variable de control

print("Iniciando cuenta con while:")
while contador <= 5: # 2. Condición del bucle
    print(f"El contador es: {contador}")
    contador = contador + 1 # 3. ¡MUY IMPORTANTE! Actualizamos la variable de control

print("Cuenta finalizada.")
```

En este ejemplo:

1. `contador` empieza en 1.
2. La condición `contador <= 5` se comprueba.
3. Si es `True`, se imprime el valor de `contador` y luego `contador` se incrementa en 1.
4. Esto se repite hasta que `contador` llega a 6. En ese momento, `6 <= 5` es `False`, y el bucle termina.

### 2.1. El Peligro del Bucle Infinito 🚨

Si la condición de un bucle `while` **nunca** se vuelve `False`, el bucle se ejecutará para siempre. Esto se conoce como un **bucle infinito** y hará que tu programa se "cuelgue" o no responda.

**Ejemplo de Bucle Infinito (¡NO LO EJECUTES SIN SABER CÓMO PARARLO! Ctrl+C suele funcionar en la terminal):**

```python
# numero_infinito = 1
# while numero_infinito > 0:
#     print("¡Esto se imprimirá para siempre porque numero_infinito siempre será mayor que 0!")
#     # Falta algo que haga que numero_infinito deje de ser > 0
```

**Siempre asegúrate de que dentro de tu bucle `while` haya alguna lógica que eventualmente haga que la condición de salida se cumpla.**

**Ejemplo - Adivinar un Número (Interactivo):**

```python
numero_secreto_juego = 42
# Inicializamos intento_usuario con un valor que no sea el secreto para asegurar que el bucle comience
intento_usuario = 0 # Podría ser None también si se maneja la primera entrada de forma diferente

print("\n--- ¡Adivina el Número Secreto (con while)! ---")
print("Pista: está entre 1 y 100.")

while intento_usuario != numero_secreto_juego:
    intento_texto = input("Introduce tu número: ")
    # Es buena práctica validar que la entrada es un número, pero lo simplificamos por ahora
    intento_usuario = int(intento_texto)

    if intento_usuario < numero_secreto_juego:
        print("Demasiado bajo. ¡Intenta otra vez!")
    elif intento_usuario > numero_secreto_juego:
        print("Demasiado alto. ¡Intenta otra vez!")
    # No hay 'else' aquí, porque si es igual, la condición del while será False en la siguiente iteración y saldrá

print(f"¡Correcto! El número secreto era {numero_secreto_juego}. ¡Has ganado!")
```

---

## Módulo 3: `for` vs `while` - ¿Cuándo Usar Cuál?

- Usa un **bucle `for`** cuando sepas de antemano cuántas veces quieres iterar o cuando quieras recorrer cada elemento de una secuencia existente (como una cadena de texto, una lista, o un `range()`). Es como decir "para cada uno de estos elementos, haz esto".

- Usa un **bucle `while`** cuando la repetición dependa de que una condición se mantenga verdadera, y no sepas exactamente cuántas iteraciones tomará. Es como decir "mientras esto sea cierto, sigue haciendo esto". A menudo se usa para bucles controlados por eventos, entradas del usuario, o hasta que se alcance un estado específico.

---

## Módulo 4: ¡A Repetir se Ha Dicho! (Ejercicios)

Ahora te toca poner en práctica los bucles. Abre `leccion2.3.py` y resuelve los ejercicios.

## Nota Importante: Aprendizaje y Originalidad

Recuerda que la mejor forma de aprender a programar es **haciendo**, **experimentando** y **resolviendo los pequeños problemas** que surgen al intentar que tu código haga lo que deseas. Intenta modificar los ejemplos de bucles de esta lección, crea tus propios contadores, iteradores sobre palabras o menús interactivos. ¡No tengas miedo a que tu programa se quede en un bucle infinito al principio! Identificar por qué ocurre y cómo solucionarlo es una parte fundamental del aprendizaje. Cada `for` que no recorre lo que esperabas o cada `while` que no para (o para antes de tiempo) es una pista valiosa para entender mejor cómo funcionan estas estructuras.

>[!WARNING]
>Estos ejercicios están diseñados para que desarrolles tu lógica y tu capacidad de controlar flujos repetitivos. Intenta resolverlos por tu cuenta antes de buscar soluciones o pedir ayuda extensiva. Ya sabéis que me reservo el derecho a hacer pequeñas pruebas escritas, especialmente sobre cómo se inicializan, se controlan y terminan los bucles, o cómo se usan con `range()`, si veo cosas raras en las soluciones. ¡El verdadero aprendizaje está en el proceso de construir y depurar tus propios bucles! 😊

**Puntos Clave de esta Lección:**

- **Automatización con Bucles:** Hemos descubierto que los bucles `for` y `while` son esenciales para repetir bloques de código y automatizar tareas.
- **Bucle `for` para Secuencias:** El bucle `for` es ideal para iterar un número conocido de veces o para recorrer cada elemento de una secuencia (como los caracteres de un string o los números generados por `range()`).
- **`range()` para Generar Números:** La función `range()` es la compañera perfecta del bucle `for` cuando necesitamos repetir algo un número específico de veces o trabajar con secuencias numéricas.
- **Bucle `while` para Condiciones:** El bucle `while` ejecuta código mientras una condición se mantenga `True`, siendo perfecto para situaciones donde no sabemos de antemano cuántas repeticiones serán necesarias.
- **Control del Bucle `while`:** Es crucial que dentro de un bucle `while` exista lógica que eventualmente haga que su condición de control se vuelva `False` para evitar bucles infinitos.
- **Indentación (¡Otra vez!):** Al igual que con los condicionales, la indentación es la que define qué código pertenece al cuerpo del bucle y se repetirá.
- **Diferencia `for` vs `while`:** Entender cuándo usar uno u otro según si conocemos el número de iteraciones de antemano o si la repetición depende de una condición dinámica.

---
