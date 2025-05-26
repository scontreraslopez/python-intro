# Lección 1: ¡Tu Programa Toma Decisiones! Introducción a los Condicionales

Hasta ahora, nuestros programas han seguido una secuencia de instrucciones, una detrás de otra, como una receta de cocina muy lineal. Hemos aprendido a guardar datos en variables, realizar operaciones y mostrar resultados. Pero, ¿qué pasa si queremos que nuestro programa haga una cosa en una situación y otra cosa diferente si la situación cambia?

Imagina en la vida real: **Si** está lloviendo, coges el paraguas. **Si no**, lo dejas en casa. **Si** tienes hambre, comes. Los programas también necesitan tomar este tipo de decisiones para ser realmente útiles y adaptarse. Hoy vamos a aprender cómo darles esa capacidad usando los **condicionales** en Python. ¡Al ataqueeer 🤡!

## Objetivos de Aprendizaje de esta Sesión

Al finalizar esta lección, serás capaz de:

- Entender qué es una condición y cómo se evalúa a un valor booleano (`True` o `False`).
- Conocer y utilizar los operadores de comparación (`==`, `!=`, `>`, `<`, `>=`, `<=`).
- Escribir y comprender la estructura condicional `if` para ejecutar código basado en una condición.
- Utilizar la estructura `if-else` para ejecutar un bloque de código alternativo si la condición no se cumple.
- Implementar la estructura `if-elif-else` para manejar múltiples condiciones excluyentes.
- Reconocer y aplicar correctamente la indentación para definir los bloques de código en los condicionales.
- (Opcional) Tener una primera idea de cómo combinar condiciones con operadores lógicos como `and` y `or`.

## Módulo 1: Condiciones y Comparaciones - La Base de las Decisiones

Para que un programa tome una decisión, primero necesita evaluar una **condición**. Una condición es simplemente una pregunta o una afirmación que puede ser Verdadera (`True`) o Falsa (`False`). Ya conocemos estos valores: son los booleanos.

Para formular estas condiciones, usamos los **operadores de comparación**:

| Operador | Significado          | Ejemplo        | Resultado del Ejemplo |
| :------- | :------------------- | :------------- | :-------------------- |
| `==`     | Igual a              | `5 == 5`       | `True`                |
|          |                      | `5 == 3`       | `False`               |
| `!=`     | Distinto de          | `5 != 3`       | `True`                |
|          |                      | `"hola" != "hola"` | `False`               |
| `>`      | Mayor que            | `10 > 5`       | `True`                |
| `<`      | Menor que            | `10 < 5`       | `False`               |
| `>=`     | Mayor o igual que    | `7 >= 7`       | `True`                |
|          |                      | `7 >= 8`       | `False`               |
| `<=`     | Menor o igual que    | `4 <= 5`       | `True`                |
|          |                      | `4 <= 3`       | `False`               |

> [!WARNING]
> **¡Mucho cuidado!** Es un error muy común confundir el operador de asignación (`=`) con el operador de comparación de igualdad (`==`).
> * `edad = 18`  (Asigna el valor 18 a la variable `edad`)
> * `edad == 18` (Comprueba si el valor de `edad` es igual a 18, y devuelve `True` o `False`)

Veamos cómo funcionan con variables. Copia si quieres este código en tu editor y ejecútalo para ver los resultados (es simplemente para que veas cómo funciona, no hay que hacer nada con él):

```python
temperatura_actual = 22
temperatura_ideal_playa = 25
hace_calor_para_playa = temperatura_actual >= temperatura_ideal_playa # Esto será False

print(f"Temperatura actual: {temperatura_actual}°C")
print(f"¿Hace calor suficiente para la playa? {hace_calor_para_playa}")

nota_examen = 6.5
necesita_aprobar = 5.0
ha_aprobado = nota_examen >= necesita_aprobar # Esto será True

print(f"Nota del examen: {nota_examen}")
print(f"¿Ha aprobado el examen? {ha_aprobado}")
```

## Módulo 2: La Sentencia `if` - Si se Cumple Algo, Hacemos Esto

La estructura más básica para tomar una decisión es la sentencia `if`. Le dice a Python: "**Si** esta condición es verdadera, entonces ejecuta el siguiente bloque de código".

**Sintaxis:**

```python
if condicion_a_evaluar:
    # Bloque de código que se ejecuta SI Y SOLO SI la condicion_a_evaluar es True
    # Este bloque DEBE estar indentado (generalmente 4 espacios)
    print("La condición era verdadera.")
    # Puedes tener más líneas aquí, todas indentadas

print("Esta línea se ejecuta siempre, esté o no indentada, después de que el if termine.")
```

**¡La Indentación es CRUCIAL en Python!**

Python no usa llaves `{}` como otros lenguajes para agrupar el código que pertenece a un `if` (o a un `else`, `elif`, `for`, `while`, funciones, etc.). En su lugar, usa la **indentación** (el espacio al principio de la línea).
* Todas las líneas de código que quieres que se ejecuten cuando la condición del `if` es `True` deben tener el mismo nivel de indentación (normalmente 4 espacios).
* Cuando Python encuentra una línea con menos indentación, entiende que el bloque del `if` ha terminado.

**Ejemplos Prácticos:**
```python
edad_usuario = 20
if edad_usuario >= 18:
    print("Eres mayor de edad. ¡Bienvenido!")
    print("Puedes acceder a contenido exclusivo.")

print("Gracias por visitarnos.") # Esta línea se ejecuta siempre se controla con la indentación

# Otro ejemplo
puntos_necesarios_bonus = 100
puntos_obtenidos = 150

if puntos_obtenidos >= puntos_necesarios_bonus:
    print("¡Felicidades! Has ganado un bonus.")
    puntos_obtenidos = puntos_obtenidos + 50 # Damos el bonus
    print(f"Tus puntos ahora son: {puntos_obtenidos}")
```
Si en el primer ejemplo `edad_usuario` fuera `16`, los mensajes dentro del `if` no se imprimirían, y solo se vería "Gracias por visitarnos."

## Módulo 3: La Sentencia `if-else` - Si se Cumple o Si No...

Muchas veces, no solo queremos hacer algo si una condición es `True`, sino también hacer otra cosa diferente si es `False`. Para esto usamos la estructura `if-else`.

**Sintaxis:**
```python
if condicion_a_evaluar:
    # Bloque de código que se ejecuta si la condicion_a_evaluar es True
    # (indentado)
    print("La condición fue Verdadera.")
else:
    # Bloque de código que se ejecuta si y solo si la condicion_a_evaluar es False
    # (también indentado)
    print("La condición fue Falsa.")

print("Esta línea se ejecuta siempre al final.")
```
El bloque `else` es opcional, pero solo puede haber uno y debe ir después de un `if`.

**Ejemplos Prácticos:**
```python
numero_ingresado = 7

if numero_ingresado % 2 == 0: # % 2 == 0 comprueba si el resto de la división entre 2 es 0 (par)
    print(f"El número {numero_ingresado} es PAR.")
else:
    print(f"El número {numero_ingresado} es IMPAR.")

# Ejemplo con acceso a un evento
edad_minima_entrada = 16
edad_persona = 14

if edad_persona >= edad_minima_entrada:
    print("¡Puedes pasar al evento!")
else:
    print("Lo sentimos, no cumples la edad mínima para entrar.")
    anos_que_faltan = edad_minima_entrada - edad_persona
    print(f"Te faltan {anos_que_faltan} año(s) para poder acceder.")
```

## Módulo 4: La Sentencia `if-elif-else` - Múltiples Caminos Posibles

¿Qué pasa si tenemos más de dos posibilidades? Por ejemplo, si queremos clasificar una nota no solo como "aprobado" o "suspenso", sino como "suspenso", "aprobado", "notable" o "sobresaliente". Para esto usamos `if-elif-else`. `elif` es una abreviatura de "else if".

Python evalúa las condiciones en orden:
1.  Comprueba el `if`. Si es `True`, ejecuta su bloque y salta el resto de la estructura `elif-else`.
2.  Si el `if` es `False`, comprueba el primer `elif`. Si es `True`, ejecuta su bloque y salta el resto.
3.  Continúa con los siguientes `elif` de la misma manera.
4.  Si ninguna condición de `if` o `elif` es `True`, se ejecuta el bloque del `else` (si existe, es opcional).

**Sintaxis:**
```python
if primera_condicion:
    # Bloque si primera_condicion es True
    print("Se cumplió la primera condición.")
elif segunda_condicion:
    # Bloque si primera_condicion fue False Y segunda_condicion es True
    print("Se cumplió la segunda condición.")
elif tercera_condicion:
    # Bloque si las dos anteriores fueron False Y tercera_condicion es True
    print("Se cumplió la tercera condición.")
# ... puedes tener tantos elif como necesites ...
else:
    # Bloque si NINGUNA de las condiciones anteriores fue True (opcional)
    print("Ninguna de las condiciones anteriores se cumplió.")

print("Fin de la estructura condicional.")
```

**Ejemplo Práctico: Calificación de Notas**

Os sonará de cuando lo hicimos con el Excel, ahora en python con condicionales. A mi juicio, mucho más legible y fácil de entender.

```python
nota_alumno = 8.2

if nota_alumno < 0 or nota_alumno > 10: # Condición para nota inválida
    print("Nota inválida. Debe estar entre 0 y 10.")
elif nota_alumno < 5:
    calificacion = "Suspenso"
elif nota_alumno < 7: # Si llega aquí, es porque nota_alumno es >= 5
    calificacion = "Aprobado"
elif nota_alumno < 9: # Si llega aquí, es porque nota_alumno es >= 7
    calificacion = "Notable"
else: # Si llega aquí, es porque nota_alumno es >= 9 y <= 10
    calificacion = "Sobresaliente"

# Esta línea solo se ejecuta si la nota fue válida
if 0 <= nota_alumno <= 10:
    print(f"Con un {nota_alumno}, tu calificación es: {calificacion}")

```

## Módulo 5: Un Vistazo a las Condiciones Compuestas

A veces necesitamos comprobar más de una cosa a la vez para tomar una decisión. Python nos da operadores lógicos para esto: `and`, `or`, y `not`. Esto lo habéis trabajado también en SQL, así que os debería sonar.

* **`and` (Y lógico):** El resultado es `True` solo si AMBAS condiciones son `True`.
    ```python
    edad = 25
    tiene_permiso_conducir = True
    if edad >= 18 and tiene_permiso_conducir:
        print("Puede alquilar un coche estándar.")
    ```

* **`or` (O lógico):** El resultado es `True` si AL MENOS UNA de las condiciones es `True`.
    ```python
    es_fin_de_semana = False
    es_dia_festivo = True
    if es_fin_de_semana or es_dia_festivo:
        print("¡Día de descanso! No hay que trabajar.")
    else:
        print("A trabajar...")
    ```

* **`not` (NO lógico):** Invierte el valor booleano de una condición. Si era `True`, la convierte en `False`, y viceversa.
    ```python
    esta_lloviendo = False
    if not esta_lloviendo:
        print("Buen día para salir a pasear.")
    ```
No te preocupes si esto parece mucho ahora, ¡ya profundizaremos más adelante! Solo es para que te suenen.

---

## Módulo 6: ¡A Practicar las Decisiones! (Ejercicios)

Ahora te toca poner en práctica estas estructuras. Abre un nuevo archivo `.py` y resuelve los siguientes desafíos:

1.  **Verificador de Edad para Votar:**
    * Crea una variable `edad_votante`. Asígnale un valor (ej. 17).
    * Escribe un programa que imprima "Puedes votar" si `edad_votante` es 18 o más.
    * Si es menor de 18, debe imprimir "No puedes votar todavía".

2.  **Número Positivo, Negativo o Cero:**
    * Crea una variable `numero_a_evaluar`. Asígnale un valor (ej. -5, 0, o 10).
    * Escribe un programa que imprima si el número es "Positivo", "Negativo" o "Cero". (Necesitarás `if-elif-else`).

3.  **Descuento en Tienda:**
    * Crea una variable `total_compra`. Asígnale un valor (ej. 45.00 o 120.50).
    * Si `total_compra` es mayor que 100.00 euros, se aplica un descuento del 10%.
    * El programa debe calcular el precio final (con o sin descuento) e imprimir:
        * El total de la compra original.
        * El descuento aplicado (si lo hay, en euros).
        * El precio final a pagar.
        * Ejemplo de salida si hay descuento:
            ```
            Total de la compra: 120.50 euros
            Descuento aplicado (10%): 12.05 euros
            Precio final a pagar: 108.45 euros
            ```
        * Ejemplo de salida si NO hay descuento:
            ```
            Total de la compra: 45.00 euros
            No se aplica descuento.
            Precio final a pagar: 45.00 euros
            ```

---

## Módulo 7: Conclusión y Próximos Pasos

¡Enhorabuena! Hoy has aprendido una de las partes más importantes de la programación: cómo hacer que tus programas tomen decisiones usando `if`, `elif` y `else`. Has visto cómo los operadores de comparación nos ayudan a crear condiciones y la importancia vital de la indentación.

Con los condicionales, tus programas pueden reaccionar de forma mucho más inteligente y adaptarse a diferentes entradas o situaciones.

En la próxima lección, veremos cómo podemos hacer que nuestros programas sean aún más interactivos pidiendo datos al usuario con la función `input()`, y cómo podemos repetir tareas con los bucles. ¡La cosa se pone cada vez más potente!

## Nota Importante: Aprendizaje y Originalidad

Recuerda que la mejor forma de aprender es practicando y experimentando. Intenta modificar los ejemplos, crea tus propias condiciones y observa qué ocurre. ¡No temas a los errores, son oportunidades para aprender!

>[!WARNING]
>Estos ejercicios están diseñados para que desarrolles tu lógica. Intenta resolverlos por tu cuenta antes de buscar soluciones. ¡El verdadero aprendizaje está en el proceso! 😊
```

**Puntos Clave de esta Lección:**

* **Analogías:** Se usan ejemplos de la vida cotidiana para hacer los conceptos más cercanos.
* **Énfasis en Indentación:** Se remarca su importancia varias veces.
* **Progresión Lógica:** `if` -> `if-else` -> `if-elif-else`.
* **Operadores de Comparación Claros:** Se presentan en una tabla y se usan en ejemplos.
* **Ejemplos Prácticos:** Cada estructura se ilustra con código que los alumnos pueden probar.
* **Ejercicios Aplicados:** Los ejercicios del final les permiten construir pequeños programas que usan las estructuras aprendidas.
* **Introducción Suave a `and`/`or`/`not`:** Para que les suene, sin profundizar demasiado aún.

Espero que esta estructura y contenido sean adecuados para tus alumnos. ¡Cualquier ajuste, me dices!