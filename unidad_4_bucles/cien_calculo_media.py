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
