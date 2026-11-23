#!/usr/bin/env python3
"""
Test Runner: Valida la ejecución de todos los ejemplos en Python y Java.
"""
import subprocess
import sys
import shutil

def run_command(command, stdin_input=None):
    print(f"-> Ejecutando: {' '.join(command)}")
    try:
        proc = subprocess.run(
            command,
            input=stdin_input,
            text=True,
            capture_output=True,
            timeout=10
        )
        return proc
    except Exception as e:
        print(f"ERROR al ejecutar {command}: {e}")
        return None

def test_01_codigo_basico():
    print("\n[TEST] 01 - Código Básico (Funciones)")
    
    # 1. Python
    res_py = run_command([sys.executable, "01_codigo_basico/codigo_basico.py"])
    assert res_py and res_py.returncode == 0, f"Fallo en Python 01: {res_py.stderr if res_py else ''}"
    assert "Empieza el programa" in res_py.stdout and "10" in res_py.stdout
    print("  [OK] Python 01 exitoso.")

    # 2. Java Tradicional
    if shutil.which("java"):
        res_java_trad = run_command(["java", "01_codigo_basico/CodigoBasicoTradicional.java"])
        assert res_java_trad and res_java_trad.returncode == 0, f"Fallo en Java Tradicional 01: {res_java_trad.stderr if res_java_trad else ''}"
        assert "Empieza el programa" in res_java_trad.stdout and "10.0" in res_java_trad.stdout
        print("  [OK] Java Tradicional 01 exitoso.")

        # 3. Java Moderno 21+
        # Detectar versión principal de java
        ver_proc = subprocess.run(["java", "--version"], text=True, capture_output=True)
        # Extraer número de versión (e.g. 21, 22, 23, 25)
        ver_line = ver_proc.stdout.splitlines()[0] if ver_proc.stdout else ""
        words = ver_line.split()
        java_ver = "21"
        for w in words:
            if w[0].isdigit():
                java_ver = w.split(".")[0]
                break

        res_java_mod = run_command(["java", "--enable-preview", "--source", java_ver, "01_codigo_basico/CodigoBasico.java"])
        assert res_java_mod and res_java_mod.returncode == 0, f"Fallo en Java Moderno 01: {res_java_mod.stderr if res_java_mod else ''}"
        assert "Empieza el programa" in res_java_mod.stdout and "10.0" in res_java_mod.stdout
        print(f"  [OK] Java Moderno 01 (Java {java_ver}) exitoso.")

def test_02_entrada_datos():
    print("\n[TEST] 02 - Entrada de Datos")
    
    # 1. Python
    res_py = run_command([sys.executable, "02_entrada_datos/entrada_datos.py"], stdin_input="5\n")
    assert res_py and res_py.returncode == 0, f"Fallo en Python 02: {res_py.stderr if res_py else ''}"
    assert "El doble es: 10.0" in res_py.stdout
    assert "El triple es: 125.0" in res_py.stdout
    print("  [OK] Python 02 exitoso.")

    # 2. Java Tradicional
    if shutil.which("java"):
        res_java_trad = run_command(["java", "02_entrada_datos/EntradaDatosTradicional.java"], stdin_input="5\n")
        assert res_java_trad and res_java_trad.returncode == 0, f"Fallo en Java Tradicional 02: {res_java_trad.stderr if res_java_trad else ''}"
        assert "El doble es: 10.0" in res_java_trad.stdout
        assert "El triple es: 125.0" in res_java_trad.stdout
        print("  [OK] Java Tradicional 02 exitoso.")

        # 3. Java Moderno
        ver_proc = subprocess.run(["java", "--version"], text=True, capture_output=True)
        ver_line = ver_proc.stdout.splitlines()[0] if ver_proc.stdout else ""
        words = ver_line.split()
        java_ver = "21"
        for w in words:
            if w[0].isdigit():
                java_ver = w.split(".")[0]
                break

        res_java_mod = run_command(["java", "--enable-preview", "--source", java_ver, "02_entrada_datos/EntradaDatos.java"], stdin_input="5\n")
        assert res_java_mod and res_java_mod.returncode == 0, f"Fallo en Java Moderno 02: {res_java_mod.stderr if res_java_mod else ''}"
        assert "El doble es: 10.0" in res_java_mod.stdout
        assert "El triple es: 125.0" in res_java_mod.stdout
        print(f"  [OK] Java Moderno 02 (Java {java_ver}) exitoso.")

if __name__ == "__main__":
    print("==========================================")
    print(" Verificación Automatizada Python vs Java ")
    print("==========================================")
    try:
        test_01_codigo_basico()
        test_02_entrada_datos()
        print("\n🎉 ¡TODAS LAS PRUEBAS PASARON CORRECTAMENTE!")
    except AssertionError as err:
        print(f"\n❌ Error de aserción: {err}")
        sys.exit(1)
    except Exception as ex:
        print(f"\n❌ Error inesperado: {ex}")
        sys.exit(1)
