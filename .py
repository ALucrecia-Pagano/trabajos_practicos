cantidad = 15

suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el nuemro que desee {i+1}: "))
    suma += numero

media = suma / cantidad
print(f"La media de los {cantidad} números ingresados es: {media}")