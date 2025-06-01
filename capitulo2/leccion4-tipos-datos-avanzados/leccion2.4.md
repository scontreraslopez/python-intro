# Lección 2.4: Organizando Colecciones de Datos - ¡Listas e introducción los Diccionarios! 📕

Hasta ahora, hemos trabajado principalmente con variables que guardan un solo dato a la vez (un número, un texto, un booleano). Pero, ¿qué ocurre si queremos manejar una **colección** de datos? Imagina que necesitas guardar los nombres de todos los alumnos de una clase, los ingredientes de una receta, o las puntuaciones de un videojuego. Guardar cada uno en una variable separada (`alumno1`, `alumno2`, `alumno3`...) sería muy poco práctico, ¿verdad?

Para solucionar esto, Python nos ofrece estructuras de datos más avanzadas. Hoy vamos a sumergirnos en una de las más versátiles y usadas: las **listas**. Las listas nos permiten almacenar múltiples ítems en una sola variable, de forma ordenada. Además, echaremos un primer vistazo a los **diccionarios**, otra forma muy potente de organizar información, pero usando "etiquetas" en lugar de posiciones.

---

## Objetivos de Aprendizaje de esta Sesión

Al finalizar esta lección, serás capaz de:

- Entender qué es una lista en Python y cómo crearla.
- Acceder a los elementos de una lista utilizando sus índices (posiciones).
- Modificar elementos existentes en una lista.
- Añadir nuevos elementos a una lista (`.append()`, `.insert()`).
- Eliminar elementos de una lista (`.pop()`, `.remove()`, `del`).
- Obtener la longitud de una lista con `len()`.
- Iterar (recorrer) los elementos de una lista utilizando bucles `for`.
- Comprobar si un elemento existe dentro de una lista usando el operador `in`.
- Tener una comprensión básica de qué es un diccionario, cómo crear uno simple y cómo acceder a sus valores mediante claves.

---

## Módulo 1: Listas - Colecciones Ordenadas y Flexibles

Una **lista** en Python es una colección ordenada y mutable de ítems:

- **Ordenada:** Los elementos se almacenan en un orden específico, y ese orden se mantiene.
- **Mutable:** ¡Podemos cambiar el contenido de una lista después de crearla! Añadir, eliminar o modificar elementos.
- **Versátil:** Una lista puede contener ítems de diferentes tipos de datos (números, strings, booleanos, ¡e incluso otras listas!). Aunque es común que las listas contengan ítems del mismo tipo.

### 1.1. Creación de Listas

Se crean usando corchetes `[]`, con los elementos separados por comas.

```python
# Una lista vacía
tareas_pendientes = []
print(f"Mi lista de tareas vacía: {tareas_pendientes}")

# Una lista de números enteros
numeros_pares = [2, 4, 6, 8, 10]
print(f"Números pares: {numeros_pares}")

# Una lista de strings (nombres)
nombres_clase = ["Ana", "Luis", "Eva", "Carlos"]
print(f"Nombres de la clase: {nombres_clase}")

# Una lista con diferentes tipos de datos (mixta)
info_persona = ["Sofía", 25, True, 1.65] # Nombre, edad, es_estudiante, altura
print(f"Información mixta: {info_persona}")
```

Fíjate la potencia, antes para los nombres hubiéramos creado variables como `nombre1`, `nombre2`, etc. Ahora, con una lista, podemos manejar todos los nombres juntos de forma ordenada y eficiente.

### 1.2. Accediendo a Elementos (Indexación)

Cada elemento en una lista tiene una posición, llamada **índice**. ¡Importante! Los índices en Python **empiezan en 0**.

- `mi_lista[0]` es el primer elemento.
- `mi_lista[1]` es el segundo elemento, y así sucesivamente.

También podemos usar **índices negativos**:

- `mi_lista[-1]` es el último elemento.
- `mi_lista[-2]` es el penúltimo, etc.

```python
colores_arcoiris = ["rojo", "naranja", "amarillo", "verde", "azul", "añil", "violeta"]

print(f"El primer color es: {colores_arcoiris[0]}")   # Salida: rojo
print(f"El cuarto color es: {colores_arcoiris[3]}")   # Salida: verde
print(f"El último color es: {colores_arcoiris[-1]}")  # Salida: violeta
print(f"El penúltimo color es: {colores_arcoiris[-2]}")# Salida: añil

# Si intentas acceder a un índice que no existe, obtendrás un error: IndexError
# print(colores_arcoiris[10]) # Esto daría IndexError
```

### 1.3. Modificando Elementos

Como las listas son mutables, podemos cambiar un elemento asignándole un nuevo valor a su índice.

```python
mis_numeros = [10, 20, 30, 45, 50]
print(f"Lista original: {mis_numeros}")

mis_numeros[3] = 40 # Cambiamos el elemento en el índice 3 (que era 45)
print(f"Lista modificada: {mis_numeros}") # Salida: [10, 20, 30, 40, 50]
```

### 1.4. Longitud de una Lista con `len()`

La función `len()` nos dice cuántos elementos hay en una lista.

```python
frutas = ["manzana", "plátano", "cereza", "dátil"]
cantidad_frutas = len(frutas)
print(f"Hay {cantidad_frutas} frutas en la lista.") # Salida: 4
```

---

## Módulo 2: Trabajando con Listas - Operaciones Comunes

Python nos ofrece varias formas de manipular las listas.

### 2.1. Añadiendo Elementos

- **`.append(item)`**: Añade un `item` al **final** de la lista.

    ```python
    compras_semana = ["leche", "pan", "huevos"]
    print(f"Lista de compras inicial: {compras_semana}")
    compras_semana.append("zumo")
    print(f"Lista después de añadir zumo: {compras_semana}")
    ```

* **`.insert(indice, item)`**: Inserta un `item` en la posición `indice` especificada, desplazando los demás elementos.

    ```python
    compras_semana.insert(1, "yogur") # Inserta "yogur" en la posición 1
    print(f"Lista después de insertar yogur: {compras_semana}")
    ```

### 2.2. Eliminando Elementos

- **`.pop()`**: Elimina y **devuelve** el último elemento de la lista. Si la lista está vacía, da error.

    ```python
    ultimo_item_comprado = compras_semana.pop()
    print(f"Compré y eliminé de la lista: {ultimo_item_comprado}")
    print(f"Lista actual: {compras_semana}")
    ```

- **`.pop(indice)`**: Elimina y devuelve el elemento en la posición `indice`.

    ```python
    item_urgente_eliminado = compras_semana.pop(1) # Eliminamos "yogur"
    print(f"Eliminé por índice: {item_urgente_eliminado}")
    print(f"Lista actual: {compras_semana}")
    ```

- **`.remove(valor)`**: Elimina la **primera ocurrencia** del `valor` especificado en la lista. Si el valor no existe, da un `ValueError`.

    ```python
    # Suponiendo que "pan" está en la lista
    if "pan" in compras_semana:
        compras_semana.remove("pan")
        print(f"Después de quitar 'pan': {compras_semana}")
    else:
        print("'pan' no estaba en la lista.")
    ```

- **`del mi_lista[indice]`**: Elimina el elemento en la posición `indice` (no devuelve el valor). También puede usarse para eliminar porciones de listas (slicing, lo veremos más adelante).

    ```python
    # Suponiendo que la lista tiene al menos un elemento
    if len(compras_semana) > 0:
        del compras_semana[0] # Eliminamos el primer elemento restante
        print(f"Después de usar 'del' en el primer elemento: {compras_semana}")
    ```

### 2.3. Comprobando si un Elemento Existe (`in`)

Podemos verificar si un ítem está en una lista usando el operador `in`. Devuelve `True` o `False`.

```python
ingredientes_pizza = ["queso", "tomate", "masa", "champiñones"]
tiene_pina = "piña" in ingredientes_pizza # Esto será False

if tiene_pina:
    print("¡Esta pizza tiene piña!")
else:
    print("Tranquilo, no hay piña en esta pizza.")
```

### 2.4. Concatenando y Repitiendo Listas

- **Concatenación (`+`):** Podemos unir dos listas para crear una nueva.

    ```python
    numeros_bajos = [1, 2, 3]
    numeros_altos = [4, 5, 6]
    todos_los_numeros = numeros_bajos + numeros_altos
    print(f"Todos los números juntos: {todos_los_numeros}")
    ```

* **Repetición (`*`):** Podemos repetir los elementos de una lista un número de veces.

    ```python
    patron = ["*", "-"] * 3 # Crea ['*', '-', '*', '-', '*', '-']
    print(f"Patrón repetido: {patron}")
    ```

---

## Módulo 3: Listas y Bucles - Recorriendo Colecciones

Los bucles `for` son la forma más natural y común de recorrer los elementos de una lista en Python. De hecho esta es para mí una de los puntos más potentes de Python: la facilidad con la que podemos iterar sobre colecciones de datos.

### 3.1. Iterando sobre una Lista con `for`

La `variable_iteradora` tomará el valor de cada elemento de la lista en cada pasada del bucle.

```python
sabores_helado = ["chocolate", "vainilla", "fresa", "menta"]

print("Mis sabores de helado favoritos son:")
for sabor in sabores_helado:
    print(f"- {sabor.capitalize()}") # .capitalize() pone la primera letra en mayúscula

# Ejemplo: Sumar todos los números de una lista
notas_parciales = [7.5, 8.0, 6.5, 9.0]
suma_total_notas = 0
for nota in notas_parciales:
    suma_total_notas = suma_total_notas + nota # o suma_total_notas += nota

print(f"La suma de las notas es: {suma_total_notas}")
promedio_notas = suma_total_notas / len(notas_parciales)
print(f"El promedio es: {promedio_notas:.2f}")
```

### 3.2. Iterando con `for` y `range(len(lista))` (si necesitas el índice)

A veces, además del elemento, necesitas saber su posición (índice) dentro de la lista. Aquí si que la sintaxis se pone un poco más fea.

```python
alumnos = ["Marcos", "Laura", "Pedro"]
print("\nLista de clase con su número:")
for i in range(len(alumnos)): # len(alumnos) es 3, range(3) genera 0, 1, 2
    print(f"{i+1}. {alumnos[i]}") # Usamos i para acceder al elemento y i+1 para mostrar
```

### 3.3. Listas y Condicionales dentro de Bucles

Podemos combinar bucles y condicionales para realizar acciones más complejas con los elementos de una lista, como filtrar o contar.

```python
numeros_varios = [1, 5, 12, 3, 8, 17, 20, 9, 4]
numeros_pares_encontrados = []
contador_mayores_que_10 = 0

for numero in numeros_varios:
    if numero % 2 == 0:
        print(f"{numero} es PAR.")
        numeros_pares_encontrados.append(numero) # Añadimos el par a una nueva lista
    
    if numero > 10:
        contador_mayores_que_10 += 1

print(f"\nLista de números pares encontrados: {numeros_pares_encontrados}")
print(f"Cantidad de números mayores que 10: {contador_mayores_que_10}")
```

---

## Módulo 4: Un Vistazo a los Diccionarios - Colecciones con Nombre

Mientras que las listas usan índices numéricos (0, 1, 2...) para acceder a sus elementos, los **diccionarios** usan **claves** (normalmente strings) para identificar y acceder a sus **valores**. Piensa en un diccionario real: buscas una palabra (la clave) para encontrar su definición (el valor).

- Son colecciones de pares `clave: valor`.
- Las claves deben ser **únicas** e **inmutables** (strings y números son claves comunes).
- Los valores pueden ser de cualquier tipo y repetirse.
- Son **mutables** (puedes añadir, cambiar o eliminar pares clave-valor).
- Desde Python 3.7+, los diccionarios mantienen el orden de inserción de los elementos.

### 4.1. Creación de Diccionarios

Se crean usando llaves `{}`.
```python
# Un diccionario vacío
dic_vacio = {}

# Un diccionario para un estudiante
estudiante = {
    "nombre": "Elena",
    "edad": 17,
    "curso": "1º Bachillerato",
    "nota_media": 8.75,
    "asignaturas_favoritas": ["Programación", "Historia"] # ¡Un valor puede ser una lista!
}
print(estudiante)
```

### 4.2. Accediendo a Valores

Se accede a un valor usando su clave entre corchetes `[]`.

```python
print(f"Nombre del estudiante: {estudiante['nombre']}")
print(f"Edad: {estudiante['edad']}")
print(f"Primera asignatura favorita: {estudiante['asignaturas_favoritas'][0]}") # Accediendo a un item de la lista dentro del dic

# Si intentas acceder a una clave que no existe, obtendrás un KeyError
# print(estudiante['apellido']) # Esto daría KeyError
```

### 4.3. Añadiendo o Modificando Pares Clave-Valor

- Si la clave no existe, se añade el nuevo par.
- Si la clave ya existe, su valor se actualiza.

```python
# Añadir nueva información
estudiante["ciudad"] = "Sevilla"
print(f"Estudiante con ciudad: {estudiante}")

# Modificar un valor existente
estudiante["nota_media"] = 9.0
print(f"Estudiante con nota actualizada: {estudiante}")
```

> [!NOTE]
> Hay mucho más sobre diccionarios (eliminar elementos, iterar sobre ellos con `.keys()`, `.values()`, `.items()`, etc.), pero esto es solo una introducción.

---

## Módulo 5: ¡A Organizar Datos! (Ejercicios)

Ahora te toca poner en práctica los bucles. Abre `leccion2.5.py` y resuelve los ejercicios.

---

## Nota Importante: Aprendizaje y Originalidad

Recuerda que la mejor forma de aprender a programar es **haciendo**, **experimentando** y **resolviendo los pequeños problemas** que surgen. Las listas y los diccionarios son increíblemente versátiles; intenta crear tus propias colecciones, modifícalas, recórrelas con bucles y observa qué ocurre. ¡Un `IndexError` o un `KeyError` al principio son normales y te enseñan los límites y el funcionamiento de estas estructuras!

>[!WARNING]
>Estos ejercicios están diseñados para que desarrolles tu lógica y tu habilidad para manejar colecciones de datos. Intenta resolverlos por tu cuenta antes de buscar soluciones o pedir ayuda extensiva. Ya sabéis que me reservo el derecho a hacer pequeñas pruebas escritas, especialmente sobre cómo acceder, modificar o iterar elementos en listas y diccionarios, si veo cosas raras en las soluciones. ¡El verdadero aprendizaje está en el proceso de descubrir y solucionar! 😊

**Puntos Clave de esta Lección:**

- **Listas para Colecciones Ordenadas:** Las listas (`[]`) son perfectas para guardar múltiples ítems en un orden específico y poder cambiarlos (son mutables).
- **Acceso por Índice:** Los elementos de una lista se acceden por su posición numérica (índice), comenzando en `0`.
- **Manipulación de Listas:** Hemos aprendido métodos clave como `.append()`, `.insert()`, `.pop()`, `.remove()` y la sentencia `del` para gestionar los elementos de una lista.
- **Bucles `for` con Listas:** La combinación de bucles `for` y listas es extremadamente poderosa para procesar cada elemento de una colección.
- **Diccionarios para Pares Clave-Valor:** Los diccionarios (`{}`) nos permiten almacenar información asociada a una "etiqueta" o clave única, facilitando la búsqueda y organización de datos con significado.
- **Mutabilidad:** Tanto listas como diccionarios son mutables, lo que significa que podemos alterar su contenido después de su creación.

---
