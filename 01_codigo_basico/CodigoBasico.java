// Java 21+ (Clases sin nombre y métodos de instancia principales - JEP 445 / 463 / 477 / 495)
// Ejecutar con: java --enable-preview --source 25 CodigoBasico.java  (o versión instalada: 21, 22, 23...)

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
