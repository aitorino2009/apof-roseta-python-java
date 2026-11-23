# 1. Código Básico: Definición de Funciones (Python vs Java Moderno)

Este módulo corresponde al primer bloque de la comparativa entre **Python** y **Java Moderno (21+)**.

---

## 📌 Comparativa de Código

### Python (`codigo_basico.py`)

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

### Java Moderno 21+ (`CodigoBasico.java`)

A partir de Java 21 (mediante JEP 445 / 463 / 477: *Implicitly Declared Classes & Instance Main Methods*), Java permite definir métodos y el punto de entrada sin necesidad de envolver todo en una clase pública explícita ni usar `public static void main(String[] args)`.

```java
// Java 21+
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

---

## 🔍 Explicación Paso a Paso

### 1. ¿Qué es una función / método? (La caja negra)
Una función es una **máquina** que recibe un ingrediente (*parámetro*), hace un trabajo con él y devuelve un producto (*resultado*).
* **Python:** Usa la palabra reservada `def` (de *define*). No se declaran tipos de forma obligatoria.
* **Java:** Especifica el tipo de dato que devuelve (`double`) y el tipo de los parámetros recibidos (`double numero`).

### 2. Delimitar el código: ¿Cómo sabe el ordenador qué está DENTRO de la función?
* **Python (El poder del espacio):** Usa los dos puntos (`:`) y la **indentación** (sangría/espacios hacia la derecha). Todo lo que esté sangrado pertenece al bloque de la función.
* **Java (Las llaves):** Usa llaves explícitas: `{` para abrir el bloque y `}` para cerrarlo. Los espacios en blanco no alteran la semántica del programa.

### 3. Devolver datos al exterior: El concepto de `return`
En ambos lenguajes se utiliza la palabra reservada explícita **`return`** para entregar el resultado final al código que invocó la función.

### 4. Flujo de ejecución
1. El compilador/intérprete lee las definiciones de `doblar` y `triplica` (las registra en memoria, pero no las ejecuta todavía).
2. La primera línea que realmente "ejecuta algo" es la impresión inicial (`print` / `System.out.println`).
3. Al llamar a `doblar(5)`, el programa da un salto a la función, procesa la operación, devuelve el resultado y lo asigna a la variable.

---

## 📊 Resumen Visual

| Concepto | ¿Qué significa? | Sintaxis en Python | Sintaxis en Java Moderno |
| :--- | :--- | :--- | :--- |
| **Definir función** | "Voy a crear una parte nueva" | `def doblar(numero):` | `double doblar(double numero) {` |
| **Límites** | "¿Dónde empieza y acaba?" | Indentación (espacios) | Llaves `{` ... `}` |
| **Devolver valor** | "Entrega el resultado final" | `return resultado` | `return resultado` |
| **Mostrar texto** | "Escribe algo en la consola" | `print('Texto')` | `System.out.println("Texto")` |

---

## 🚀 Cómo Ejecutar

### Ejecución en Python:
```bash
python 01_codigo_basico/codigo_basico.py
```

### Ejecución en Java Moderno (Java 21+ con soporte preview):
```bash
java --enable-preview --source 25 01_codigo_basico/CodigoBasico.java
```
*(Sustituir `25` por la versión instalada en el sistema, por ejemplo `21`)*

### Ejecución en Java Tradicional (compatible con cualquier versión):
```bash
java 01_codigo_basico/CodigoBasicoTradicional.java
```
