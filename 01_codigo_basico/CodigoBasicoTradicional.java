// Java Tradicional (Orientado a Objetos clásico con clase pública y public static void main)
// Ejecutar con: java CodigoBasicoTradicional.java

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
