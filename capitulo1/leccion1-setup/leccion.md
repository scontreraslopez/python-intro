# Sesión 1: Configurando el Entorno y Primer Programa en Python

¡Muy buenas! Felicitaros por haber decidido dar el primer paso en el mundo de la programación. En esta primera sesión, vamos a configurar nuestro entorno de trabajo y escribir nuestro primer programa en Python.

Python es un lenguaje de programación ideal para empezar: es potente, lo usan empresas gigantes como Google o Netflix, y además, ¡es más fácil de aprender de lo que piensas! Mucha gente dice que su sintaxis es como leer inglés.

En esta primera sesión, vamos a poner a punto nuestras herramientas y escribiremos nuestras primeras líneas de código. ¡Prepárate para decirle "Hola" al mundo de una forma nueva!

## Objetivos de Aprendizaje de esta Sesión

Al finalizar esta lección, serás capaz de:

- Configurar Visual Studio Code (VS Code) para trabajar con Python.
- Entender de forma básica qué es Python y por qué es tan popular.
- Escribir, ejecutar y guardar tu primer programa sencillo en Python utilizando VS Code.
- Saber cómo crear archivos Python (`.py`) y cómo entregarlos para revisión.

## ¡Empezamos! Desarrollo de la Sesión

### Módulo 1: Bienvenida e Introducción a Python (Teoría)

Como te decía, Python es un lenguaje amigable pero muy poderoso. Perteneces a la categoría de lenguajes interpretados, lo que significa que no necesitas compilar tu código antes de ejecutarlo. Esto es genial para aprender, ya que puedes ver los resultados de inmediato.

Python es un lenguaje popular en muchos campos: scripting, desarrollo web, análisis de datos, inteligencia artificial, automatización de tareas y mucho más. ¡Las posibilidades son infinitas!

#### Fortalezas de Python

- **Fácil de Aprender:** Su sintaxis es clara y legible, lo que facilita la comprensión. Además cuenta con una gran **comunidad activa:** por lo que hay muchos recursos, tutoriales y foros donde puedes encontrar ayuda.
- **Bibliotecas y Frameworks:** Python tiene una amplia gama de bibliotecas y frameworks que facilitan el desarrollo de aplicaciones complejas sin tener que reinventar la rueda. Por ejemplo si queremos leer un archivo Excel, podemos usar la biblioteca `pandas` y con una sola línea de código lo conseguimos.
- **Desarrollo rápido:** Python es un lenguaje de alto nivel que permite un desarrollo rápido y ágil, lo que significa que puedes crear prototipos y aplicaciones funcionales en poco tiempo. Te ahorra tener que gestionar la memoria y tener que tipar (decir el tipo de datos que vamos a usar, como hacíamos en SQL con `INTEGER`, `TEXT`, ...) de forma explícita las variables, lo que hace que el código sea más limpio y fácil de entender.
- **Versatilidad:** Puedes usar Python para casi cualquier cosa, desde scripts simples hasta aplicaciones web complejas y análisis de datos. Por ejemplo en los campos de **inteligencia artificial, data science y aprendizaje automático**, cuenta con librerías potentísimas como TensorFlow, scikit-learn, NumPy y Pandas.
- **Portabilidad e Interactividad:** Al ser un lenguaje interpretado, el código Python es multiplataforma y podemos ejecutarlo en diferentes sistemas operativos sin problemas. Del mismo modo, nos permite probar y experimentar con el código de inmediato, lo que facilita el aprendizaje y la exploración.

#### Debilidades de Python

- **Velocidad:** Python es más lento que lenguajes compilados como C o C++. Esto puede ser un inconveniente en aplicaciones que requieren un alto rendimiento, pero para la mayoría de los casos de uso, la velocidad no es un problema significativo.
- **Consumo de Memoria:** Python tiende a consumir más memoria que otros lenguajes, lo que puede ser un problema en dispositivos con recursos limitados. Sin embargo, esto no suele ser un problema en la mayoría de los casos, especialmente en aplicaciones de escritorio o web.
- **Complicado para grandes desarrollos:** Aunque Python es excelente para prototipos y desarrollo rápido, en proyectos muy grandes puede volverse difícil de mantener. Esto se debe a que su flexibilidad puede llevar a un código menos estructurado si no se tiene cuidado. ¡Además errores en tiempo de ejecución que pueden ser difíciles de depurar! Sin embargo, con buenas prácticas de programación y el uso de herramientas adecuadas, esto se puede mitigar.
- **Dependencias:** A veces, las bibliotecas de Python pueden tener dependencias complicadas, lo que puede dificultar la instalación y el mantenimiento de proyectos. Sin embargo, herramientas como `pip` y `virtualenv` ayudan a gestionar estas dependencias de manera efectiva.

### Módulo 2: Preparando Nuestro Entorno de Programación (Práctica)

Ya conocéis los IDEs (Entornos de Desarrollo Integrados). De nuevo, nosotros vamos a usar **Visual Studio Code (VS Code)**, y que ya debería estar instalado en los ordenadores de clase en **Lliurex**.

>[!IMPORTANT]
> Usaremos Lliurex, sin necesidad de máquina virtual. Si acaba dándonos problemas ya crearé una imagen de máquina virtual con el entorno de trabajo y la configuración necesaria para que no tengáis que preocuparos por nada. De momento, vamos a intentar usar Lliurex.

1. **Abre VS Code.**
2. **Instala la Extensión de Python (de Microsoft):**
    - En la barra lateral izquierda, busca un icono que parece un conjunto de cuadrados (o presiona `Ctrl+Shift+X`). Esta es la vista de Extensiones.
    - En el buscador de extensiones, escribe `Python`.
    - Busca la extensión que dice "Python" y es ofrecida por Microsoft. Haz clic en el botón "Instalar".
    - *¿Qué hace esto?* Esta extensión le da a VS Code "superpoderes" para entender Python: te ayudará a escribir código, depurarlo y mucho más.

3. **Selecciona el Intérprete de Python:**
    - A veces VS Code lo detecta solo, pero es bueno saber cómo hacerlo.
    - Abre la Paleta de Comandos: `Ctrl+Shift+P` (o `Cmd+Shift+P` en Mac).
    - Escribe `Python: Select Interpreter` y selecciónalo de la lista.
    - Te mostrará las versiones de Python que tengas instaladas.
    - *¿Qué es esto?* Es como decirle a VS Code: "Cuando ejecute código Python, usa *esta* versión específica de Python que tengo instalada."

4. **Crea tu Espacio de Trabajo:**
    - Es fundamental ser organizado. En tu escritorio crea la carpeta `dev`
    - Dentro de esa carpeta, crea otra para este curso de Python: `python-intro`.
    - Dentro de `python-intro`, crea una carpeta para este capítulo: `capitulo1`.
    - Ahora, en VS Code, ve a `Archivo` > `Abrir carpeta...` (o `File` > `Open Folder...`) y selecciona la carpeta `python-intro` que acabas de crear.
    - VS Code ahora se centrará en esa carpeta. ¡Es tu espacio de trabajo para python!

### Módulo 3: ¡Manos a la Obra!

![Manos a la obra](/assets/images/manos_obra.jpeg)

Llegó el momento de la verdad. Vamos a crear nuestro primer archivo Python y a escribir código.

1. **Crea un Nuevo Archivo Python:**
    - En el panel "Explorador" de VS Code (normalmente a la izquierda, verás una carpeta que se llama `capitulo1`), haz clic derecho sobre el nombre de la carpeta.
    - Selecciona `Nuevo archivo` (o `New File`).
    - Nombra el archivo: `hola_mundo.py`.
    - **Importante:** La extensión `.py` al final le dice al sistema (y a VS Code) que este es un archivo de Python.

    ![Archivo hola_mundo.py en Visual Studio Code](/assets/images/1.1-archivo_hola_mundo.png)

2. **Escribe tu Primer Código:**
    - En el archivo `hola_mundo.py` que se acaba de abrir, escribe lo siguiente:

    ```python
    # Mi primer programa en Python
    
    print("¡Hola, Mundo!")

    print("La función print() muestra texto en la pantalla.")
    print("Python también puede hacer cálculos, mira: 5 + 3 =", 5 + 3)
    ```

    - **Analicemos un poco:**
        - La línea que empieza con `#` es un **comentario**. Python la ignora, es decir que el código que aparezca en la misma línea que la almohadilla no se ejecutará. Sirve para que los humanos dejemos notas en el código.
        - `print()` es una **función** incorporada de Python. Su trabajo es mostrar en la pantalla lo que le pongas entre paréntesis.
        - Si quieres mostrar texto, debes ponerlo entre comillas (simples `'...'` o dobles `"..."`).
        - Fíjate que para mostrar el resultado del cálculo `5 + 3`, no usamos comillas alrededor de `5 + 3`.

3. **Guarda el Archivo:**
    - Presiona `Ctrl+S` (o `Cmd+S` en Mac). ¡Acostúmbrate a guardar a menudo!

4. **¡Ejecuta tu Programa!**
    - Hay varias formas. La más sencilla en VS Code:
        - Busca un botón de "Play" (un triángulo) en la esquina superior derecha de la ventana de VS Code. Haz clic en él. (A veces dice "Run Python File in Terminal").
        - Alternativamente, haz clic derecho en cualquier parte del editor donde escribiste el código y selecciona `Ejecutar archivo de Python en la terminal` (o `Run Python File in Terminal`).
    - Debería abrirse un panel en la parte inferior llamado "TERMINAL". Ahí verás la salida de tu programa:

    ![Botón ejecutar VS Code](/assets/images/1.1-run_button.png)
    ![Salida terminal](/assets/images/1.1-terminal_output.png)

    **¡FELICIDADES! ¡Acabas de ejecutar tu primer programa Python!**

5. **Experimenta un Poco:**

    - Crea un nuevo archivo Python llamado `leccion1.py` que genera la siguiente salida por consola:

    ```powershell
    
    Para escribir texto, usa comillas dentro de los paréntesis.
    Cada print() muestra una línea nueva
    Para calcular, no uses comillas, es lo que distingue un número de un texto.

    Además de sumas, puedes hacer restas, multiplicaciones y divisiones. Por ejemplo:
    
    5 - 3 = 2
    5 * 3 = 15
    5 / 3 = 1.6666666666666667
   
    ```

> [!NOTA]
> **TRUCAZO**: En python existe una sintaxis especial que se llama *f-strings* que permite incluir variables dentro de cadenas de texto. Por ejemplo, print(f"El resultado de 5 + 3 es {5 + 3}"). Esto es muy útil para mostrar resultados de cálculos dentro de un texto. ¡Prueba a usarlo!

### Módulo 4: Wrapping Up

¡Excelente trabajo hoy! Hemos preparado VS Code, hemos aprendido qué es (a grandes rasgos) Python y, lo más importante, ¡hemos hecho que el ordenador nos salude y haga un cálculo!

## Nota Importante: Aprendizaje y Originalidad

Estos ejercicios están diseñados para que desarrolles tu capacidad de resolver problemas y entiendas cómo funciona la programación. Herramientas como la IA pueden ser útiles para consultar dudas puntuales (¡como un libro o un buscador!), pero la clave está en que tú mismo/a pienses, pruebes y cometas errores (¡así se aprende!).

Me reservo el derecho de hacer pequeñas pruebas o preguntas para asegurar que los conceptos fundamentales se están asimilando correctamente, especialmente si observo un uso que no favorezca el aprendizaje individual. ¡Confío plenamente en tu esfuerzo y curiosidad!
