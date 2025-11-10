#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

def fibonacci(n):
    if n <= 1:  # Casos base
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Caso recursivo

# Programa principal
n = int(input("Ingrese la cantidad de términos: "))
for i in range(n):
    print(fibonacci(i), end=" ")
