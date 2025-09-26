#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(101):
    print(numero)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero_ingresado = int(input("Ingrese un numero: "))
contador = 0
num = numero_ingresado
while num > 0:
        num = num// 10 
        contador += 1


print(f"El número {numero_ingresado} tiene {contador} dígitos.")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundonumero: "))

for i in range(numero_1 + 1, numero_2):
      print(i)


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.



total = 0  

while True: 
    numero = int(input("Ingrese un número entero (0 para salir): "))
    
    if numero == 0: 
        break
    
    total += numero 

print(f"El total acumulado es: {total}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
intentos = 0
numero_aleatorio = random.randint(0,9)

while True:
    ingreso = int(input("Adivina un número entre 0 y 9: "))
    intentos += 1
    if ingreso == numero_aleatorio:
         print(f"Has ganado! al intento {intentos}")
         break
    else:
         print("Intenta otra vez!")     

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.   


for i in range(101,0,-1):
      if i % 2 == 0:
        print(i)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

total = 0  
numero = int(input("Ingrese un número entero: "))

for num in range(numero +1):
    total += num
    print(f"la suma de los numeros de 0 a {numero} es {total}")

#8)Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio)

cantidad = 100  

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

cantidad = 100

suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el nuemro que desee {i+1}: "))
    suma += numero

media = suma / cantidad

print(f"La media de los {cantidad} números ingresados es: {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un número entero: ")

numero_invertido = numero[::-1]

print(f"El número invertido es: {numero_invertido}")

