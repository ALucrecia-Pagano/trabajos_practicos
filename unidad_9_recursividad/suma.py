#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n < 10:  # Caso base
        return n
    else:
        return n % 10 + suma_digitos(n // 10)  # Caso recursivo

# Programa principal
num = int(input("Ingrese un número: "))
print(f"La suma de los dígitos es: {suma_digitos(num)}")
