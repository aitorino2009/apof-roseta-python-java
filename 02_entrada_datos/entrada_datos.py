"""
Tema 2: Entrada de Datos por el Usuario
Comparativa: Python vs Java Moderno (21+)
"""

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
