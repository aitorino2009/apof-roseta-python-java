# 📘 Comparativa: Python vs Java Moderno (21+)

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Java](https://img.shields.io/badge/Java-21%2B%20LTS-ED8B00?logo=openjdk&logoColor=white)](https://openjdk.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Repositorio educativo que documenta la evolución sintáctica y conceptual entre **Python** y **Java Moderno (Java 21+)**, demostrando cómo las características recientes de Java aproximan su legibilidad a lenguajes concisos como Python sin renunciar al tipado estático ni al rendimiento.

---

## 📑 Tabla de Contenidos

1. [Estructura del Proyecto](#-estructura-del-proyecto)
2. [Sección 1: Código Básico (Definición de Funciones)](#1-código-básico-definición-de-funciones)
   - [Código en Python](#código-en-python-1)
   - [El "Espejo" en Java Moderno (21+)](#el-espejo-en-java-moderno-java-21-1)
   - [Contraste: Java Tradicional](#contraste-java-tradicional-1)
   - [Explicación paso a paso](#explicación-paso-a-paso)
   - [Resumen visual](#resumen-visual)
3. [Sección 2: Entrada de Datos por el Usuario](#2-entrada-de-datos-por-el-usuario)
   - [Código en Python](#código-en-python-2)
   - [El "Espejo" en Java Moderno (21+)](#el-espejo-en-java-moderno-java-21-2)
   - [Contraste: Java Tradicional](#contraste-java-tradicional-2)
   - [Puntos clave comparativos](#puntos-clave-comparativos)
   - [Tabla resumen para la pizarra](#tabla-resumen-para-la-pizarra)
4. [JEPs Relevantes de Java Moderno](#-jeps-relevantes-de-java-moderno)
5. [Guía de Ejecución Rápida](#-guía-de-ejecución-rápida)
6. [Flujo de Trabajo Git](#-flujo-de-trabajo-git)

---

## 📂 Estructura del Proyecto

```text
apof-roseta-python-java/
├── .github/
│   └── workflows/
│       └── ci.yml                            # Integración Continua (CI)
├── 01_codigo_basico/
│   ├── codigo_basico.py                      # Script de funciones en Python
│   ├── CodigoBasico.java                     # Java 21+ (Clases implícitas / Unnamed classes)
│   ├── CodigoBasicoTradicional.java          # Java clásico (POO tradicional)
│   └── README.md                             # Detalle y explicaciones del Bloque 1
├── 02_entrada_datos/
│   ├── entrada_datos.py                      # Script de entrada de usuario en Python
│   ├── EntradaDatos.java                     # Java 21+ con Scanner y tipo inferido var
│   ├── EntradaDatosPreview21.java            # Java 21 Preview con String Templates (STR)
│   ├── EntradaDatosTradicional.java          # Java clásico con Scanner
│   └── README.md                             # Detalle y explicaciones del Bloque 2
├── .gitignore                                # Exclusiones de Git (compilados, temporales)
├── test_runner.py                            # Suite de verificación automatizada
└── README.md                                 # Guía general de la comparativa
```

---

## 1. Código Básico (Definición de Funciones)

### Código en Python (`01_codigo_basico/codigo_basico.py`)

```python
def doblar(numero):
    resultado = numero * 2
    return resultado

def triplica(valor):
    resultado = valor ** 3
    return resultado

print('Empieza el programa')
multiplica = doblar(5)
print(multiplica)
```

### El "Espejo" en Java Moderno (Java 21+) (`01_codigo_basico/CodigoBasico.java`)

```java
// Java 21+ (Clases implícitas / Unnamed classes & instance main methods)
double doblar(double numero) {
    var resultado = numero * 2;
    return resultado;
}

double triplica(double valor) {
    var resultado = Math.pow(valor, 3);
    return resultado;
}

void main() {
    System.out.println("Empieza el programa");
    var multiplica = doblar(5);
    System.out.println(multiplica);
}
```

### Contraste: Java Tradicional (`01_codigo_basico/CodigoBasicoTradicional.java`)

```java
public class CodigoBasicoTradicional {
    public static double doblar(double numero) {
        double resultado = numero * 2;
        return resultado;
    }

    public static double triplica(double valor) {
        double resultado = Math.pow(valor, 3);
        return resultado;
    }

    public static void main(String[] args) {
        System.out.println("Empieza el programa");
        double multiplica = doblar(5);
        System.out.println(multiplica);
    }
}
```

---

### Explicación paso a paso

#### 1. ¿Qué es una función / método? (La caja negra)
Una función es una **máquina** que recibe un ingrediente (*parámetro*), hace un trabajo con él y devuelve un producto (*resultado*).
* **Python:** Usa la palabra reservada `def` (de *define*). El tipado no es obligatorio en la firma.
* **Java:** Especifica explícitamente el tipo de dato que devuelve (por ejemplo `double`) y el tipo de cada parámetro recibido (`double numero`).

#### 2. Delimitar el código: ¿Cómo sabe el ordenador qué está DENTRO de la función?
* **Python (El poder del espacio):** Usa los dos puntos (`:`) y la **indentación** (sangría/espacios hacia la derecha). Todo lo que esté sangrado pertenece al cuerpo de la función.
* **Java (Las llaves):** Usa llaves explícitas: `{` para abrir el bloque y `}` para cerrarlo. El compilador ignora los saltos de línea y sangrías adicionales.

#### 3. Devolver datos al exterior: El concepto de `return`
En ambos lenguajes se utiliza la palabra reservada explícita **`return`** para entregar el resultado final al código principal.

#### 4. Flujo de ejecución
1. El compilador/intérprete lee las definiciones de `doblar` y `triplica` (las guarda en memoria, pero no las ejecuta todavía).
2. La primera línea que realmente "ejecuta algo" es la impresión inicial (`print` / `System.out.println`).
3. Al llamar a `doblar(5)`, el programa da un salto a la función, procesa la operación, devuelve el resultado y lo asigna a la variable.

---

### Resumen visual

| Concepto | ¿Qué significa? | Sintaxis en Python | Sintaxis en Java Moderno |
| :--- | :--- | :--- | :--- |
| **Definir función** | "Voy a crear una parte nueva" | `def doblar(numero):` | `double doblar(double numero) {` |
| **Límites** | "¿Dónde empieza y acaba?" | Indentación (espacios) | Llaves `{` ... `}` |
| **Devolver valor** | "Entrega el resultado final" | `return resultado` | `return resultado` |
| **Mostrar texto** | "Escribe algo en la consola" | `print('Texto')` | `System.out.println("Texto")` |

---

## 2. Entrada de Datos por el Usuario

### Código en Python (`02_entrada_datos/entrada_datos.py`)

```python
def doblar(numero):
    resultado = numero * 2
    return resultado

def triplica(valor):
    resultado = valor ** 3
    return resultado

# --- Entrada de datos del usuario ---
def pedir_numero():
    texto = input("Introduce un numero: ")
    numero = float(texto)  # Convertimos el texto a número decimal
    return numero

# --- Flujo del programa ---
print('Empieza el programa')

# Pedimos el número al usuario
num_usuario = pedir_numero()

# Calculamos y mostramos los resultados
resultado_doble = doblar(num_usuario)
resultado_triple = triplica(num_usuario)

print("El doble es:", resultado_doble)
print("El triple es:", resultado_triple)
```

---

### El "Espejo" en Java Moderno (Java 21+) (`02_entrada_datos/EntradaDatos.java`)

```java
import java.util.Scanner;

double doblar(double numero) {
    var resultado = numero * 2;
    return resultado;
}

double triplica(double valor) {
    var resultado = Math.pow(valor, 3);
    return resultado;
}

// --- Entrada de datos del usuario ---
double pedirNumero() {
    System.out.print("Introduce un numero: ");
    var scanner = new Scanner(System.in);
    return scanner.nextDouble();
}

// --- Flujo principal ---
void main() {
    System.out.println("Empieza el programa");

    var numUsuario = pedirNumero();

    var resultadoDoble = doblar(numUsuario);
    var resultadoTriple = triplica(numUsuario);

    // Salida formateada
    System.out.println("El doble es: " + resultadoDoble);
    System.out.println("El triple es: " + resultadoTriple);
}
```

> **Nota sobre String Templates (STR en Java 21 Preview):**  
> En Java 21 Preview (JEP 430), se introdujo la sintaxis:
> ```java
> System.out.println(STR."El doble es: \{resultadoDoble}");
> System.out.println(STR."El triple es: \{resultadoTriple}");
> ```
> Esta implementación exacta está disponible en el archivo [`EntradaDatosPreview21.java`](02_entrada_datos/EntradaDatosPreview21.java).

---

### Contraste: Java Tradicional (`02_entrada_datos/EntradaDatosTradicional.java`)

```java
import java.util.Scanner;

public class EntradaDatosTradicional {
    public static double doblar(double numero) {
        double resultado = numero * 2;
        return resultado;
    }

    public static double triplica(double valor) {
        double resultado = Math.pow(valor, 3);
        return resultado;
    }

    public static double pedirNumero() {
        System.out.print("Introduce un numero: ");
        Scanner scanner = new Scanner(System.in);
        return scanner.nextDouble();
    }

    public static void main(String[] args) {
        System.out.println("Empieza el programa");
        double numUsuario = pedirNumero();
        double resultadoDoble = doblar(numUsuario);
        double resultadoTriple = triplica(numUsuario);
        System.out.println("El doble es: " + resultadoDoble);
        System.out.println("El triple es: " + resultadoTriple);
    }
}
```

---

### Puntos clave comparativos (Python vs Java Moderno)

#### 1. Estructura del código (Top-Level Statements / Clases Implícitas)
* **En Java Tradicional:** Era obligatorio empaquetar todo dentro de una clase (`public class Main`) y un método principal estático con parámetros no utilizados por principiantes (`public static void main(String[] args)`).
* **En Java Moderno (21+):** Se permiten instrucciones y métodos a nivel de archivo dentro de clases sin nombre declaradas implícitamente (JEP 445 / 463 / 477), con un método de instancia `void main()`.

#### 2. Declaración de variables y Tipado (`var`)
* **En Python:** El tipado es dinámico implícito (`num_usuario = pedir_numero()`).
* **En Java Moderno:** Mantiene el tipado estático seguro, pero añade **inferencia de tipos local** mediante la palabra clave **`var`**, eliminando el exceso de repetición del tipo.

#### 3. Entrada de texto y conversión
* **En Python:** `input()` captura siempre un `str` que requiere conversión explícita mediante `float(texto)`.
* **En Java Moderno:** `Scanner` permite leer y parsear directamente el tipo numérico esperado (`scanner.nextDouble()`).

---

### Tabla resumen para la pizarra

| Concepto | En Python | En Java Moderno |
| :--- | :--- | :--- |
| **Tipado / Inferencia** | Dinámico | Estático con `var` |
| **Leer teclado** | `input("Introduce: ")` | `scanner.nextDouble()` / `Scanner` |
| **Convertir a número** | `float(texto)` / `int(texto)` | Manejado por `Scanner` o `Double.parseDouble()` |
| **Mostrar en consola** | `print("El doble es:", resultado)` | `System.out.println("El doble es: " + resultado)` / `STR."..."` |
| **Delimitadores de bloque** | Indentación | Llaves `{` ... `}` |

---

## ☕ JEPs Relevantes de Java Moderno

| JEP | Versión | Nombre | Impacto en la Comparativa |
| :--- | :--- | :--- | :--- |
| **JEP 286** | Java 10 | Local-Variable Type Inference | Permite el uso de `var` para inferir tipos locales. |
| **JEP 330** | Java 11 | Launch Single-File Source Programs | Permite ejecutar archivos `.java` directamente con `java Archivo.java` sin compilar previamente con `javac`. |
| **JEP 445** | Java 21 (Preview) | Unnamed Classes and Instance Main Methods | Elimina la necesidad de `class`, `public`, `static` y `String[] args` para principiantes. |
| **JEP 430** | Java 21 (Preview) | String Templates | Introduce el procesador `STR."..."` para interpolación de cadenas. |
| **JEP 463 / 477** | Java 22 / 23 (Preview) | Implicitly Declared Classes & Instance Main Methods | Segunda y tercera revisión del soporte para scripts y programas de archivo único. |

---

## 🚀 Guía de Ejecución Rápida

### Requisitos Previos
* **Python**: 3.10 o superior (`python --version`)
* **Java**: JDK 21 o superior (`java --version`)

### 1. Ejecutar Código Básico (Bloque 1)
```bash
# Python
python 01_codigo_basico/codigo_basico.py

# Java Moderno 21+ (con flags de preview según la versión de JDK)
java --enable-preview --source 25 01_codigo_basico/CodigoBasico.java

# Java Tradicional
java 01_codigo_basico/CodigoBasicoTradicional.java
```

### 2. Ejecutar Entrada de Datos (Bloque 2)
```bash
# Python
python 02_entrada_datos/entrada_datos.py

# Java Moderno 21+
java --enable-preview --source 25 02_entrada_datos/EntradaDatos.java

# Java Tradicional
java 02_entrada_datos/EntradaDatosTradicional.java
```

### 3. Ejecutar la Suite de Pruebas Automatizada
```bash
python test_runner.py
```

---

## 🌿 Flujo de Trabajo Git

El repositorio sigue una estrategia estructurada con ramas de características (*feature branches*) y commits semánticos (*Conventional Commits*):

* `main`: Rama principal estable protegida.
* `feature/01-codigo-basico`: Implementación del Bloque 1 (definición de funciones).
* `feature/02-entrada-datos`: Implementación del Bloque 2 (entrada de usuario e inferencia de tipos).
* `feature/docs-and-ci`: Documentación completa, runner de verificación automatizada y pipeline de CI.
