// Java 21 Preview con String Templates (JEP 430) y Unnamed Classes (JEP 445)
// NOTA: Requiere JDK 21 o JDK 22 y habilitar preview:
//   java --enable-preview --source 21 EntradaDatosPreview21.java
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

    // Interpolación de variables con el procesador de plantillas STR (Java 21 Preview)
    System.out.println(STR."El doble es: \{resultadoDoble}");
    System.out.println(STR."El triple es: \{resultadoTriple}");
}
