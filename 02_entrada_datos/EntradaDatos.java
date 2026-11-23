// Java 21+ (Clases implícitas / sin nombre y métodos de instancia principales)
// Ejecución: java --enable-preview --source 25 EntradaDatos.java (o versión instalada: 21, 22, 23...)
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

    // Salida por consola en Java Moderno (compatible universalmente)
    System.out.println("El doble es: " + resultadoDoble);
    System.out.println("El triple es: " + resultadoTriple);
}
