#Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:  # Caso base
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Programa principal
num = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(num)
print(f"El número {num} en binario es: {binario}")
