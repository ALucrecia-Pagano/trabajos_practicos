
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

total = 0  
numero = int(input("Ingrese un número entero: "))

for num in range(numero +1):
    total += num
    print(f"la suma de los numeros de 0 a {numero} es {total}")