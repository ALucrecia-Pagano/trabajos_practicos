#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero_ingresado = int(input("Ingrese un numero: "))
contador = 0
num = numero_ingresado
while num > 0:
        num = num// 10 
        contador += 1


print(f"El número {numero_ingresado} tiene {contador} dígitos.")
