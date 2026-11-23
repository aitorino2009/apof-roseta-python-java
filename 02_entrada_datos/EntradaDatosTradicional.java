// Java Tradicional (Orientación a Objetos clásica)
// Ejecución: java EntradaDatosTradicional.java
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

    // --- Entrada de datos del usuario ---
    public static double pedirNumero() {
        System.out.print("Introduce un numero: ");
        Scanner scanner = new Scanner(System.in);
        return scanner.nextDouble();
    }

    // --- Flujo principal ---
    public static void main(String[] args) {
        System.out.println("Empieza el programa");

        double numUsuario = pedirNumero();

        double resultadoDoble = doblar(numUsuario);
        double resultadoTriple = triplica(numUsuario);

        System.out.println("El doble es: " + resultadoDoble);
        System.out.println("El triple es: " + resultadoTriple);
    }
}
