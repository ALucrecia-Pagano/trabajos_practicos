#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundonumero: "))

for i in range(numero_1 + 1, numero_2):
      print(i)