# 2. Entrada de Datos por el Usuario (Python vs Java Moderno)

Este módulo corresponde al segundo bloque de la comparativa entre **Python** y **Java Moderno (21+)**, centrado en la interacción con el usuario y la manipulación de tipos numéricos.

---

## 📌 Comparativa de Código

### Python (`entrada_datos.py`)

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

### Java Moderno 21+ (`EntradaDatos.java` / `EntradaDatosPreview21.java`)

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

    // Interpolación de variables en Java 21 Preview (JEP 430)
    // System.out.println(STR."El doble es: \{resultadoDoble}");
    // System.out.println(STR."El triple es: \{resultadoTriple}");

    System.out.println("El doble es: " + resultadoDoble);
    System.out.println("El triple es: " + resultadoTriple);
}
```

---

## 🔍 Puntos Clave Comparativos (Python vs Java Moderno)

### 1. Estructura del código (Top-Level Statements / Clases implícitas)
* **En Java Tradicional:** Era obligatorio empaquetar todo dentro de una clase (`public class Main`) y un método principal estático (`public static void main(String[] args)`).
* **En Java Moderno (21+):** Se permiten instrucciones y métodos a nivel superior en clases implícitas (JEP 445 / 463 / 477), con un método de instancia `void main()`, logrando una sencillez de lectura muy similar a la de Python.

### 2. Declaración de variables y Tipado (`var`)
* **En Python:** El tipado es dinámico implícito (`num_usuario = pedir_numero()`). El tipo de la variable lo determina el valor en tiempo de ejecución.
* **En Java Moderno:** Mantiene el **tipado estático** en tiempo de compilación, pero utiliza **inferencia de tipos** mediante la palabra clave reservada **`var`**, evitando tener que escribir tipos repetitivos como `double resultadoDoble = ...`.

### 3. Entrada de texto y conversión
* **En Python:** `input()` captura siempre una cadena de texto (`str`), por lo que requiere una conversión explícita posterior mediante `float(texto)` o `int(texto)`.
* **En Java Moderno:** La clase `Scanner` incluye métodos específicos (`scanner.nextDouble()`, `scanner.nextInt()`) que leen y convierten directamente el valor ingresado por teclado al tipo primitivo correspondiente.

### 4. Interpolación de texto y salida
* **En Python:** Admite argumentos separados por comas en `print()` (e.g. `print("El doble es:", resultado)`), además de f-strings (`f"El doble es: {resultado}"`).
* **En Java:**
  * Tradicionalmente usa concatenación (`"El doble es: " + resultado`) o `.formatted()`.
  * En Java 21 Preview (JEP 430) se introdujeron los *String Templates* con `STR."El doble es: \{resultadoDoble}"`.

---

## 📊 Tabla Resumen para la Pizarra

| Concepto | En Python | En Java Moderno |
| :--- | :--- | :--- |
| **Tipado / Inferencia** | Dinámico | Estático con inferencia `var` |
| **Leer teclado** | `input("Introduce: ")` | `scanner.nextDouble()` / `Scanner` |
| **Convertir a número** | `float(texto)` / `int(texto)` | Manejado por `Scanner` o `Double.parseDouble()` |
| **Mostrar en consola** | `print("El doble es:", resultado)` | `System.out.println("El doble es: " + resultado)` / `STR."..."` |
| **Delimitadores de bloque** | Indentación (espacios) | Llaves `{` ... `}` |

---

## 🚀 Cómo Ejecutar

### Ejecución en Python:
```bash
python 02_entrada_datos/entrada_datos.py
```

### Ejecución en Java Moderno (Java 21+):
```bash
java --enable-preview --source 25 02_entrada_datos/EntradaDatos.java
```

### Ejecución en Java Tradicional:
```bash
java 02_entrada_datos/EntradaDatosTradicional.java
```
