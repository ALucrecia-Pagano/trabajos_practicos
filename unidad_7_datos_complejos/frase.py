#5) Solicita al usuario una frase e imprime:
#Las palabras únicas (usando un set).
#Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ").lower()
palabras = frase.split()

unicas = set(palabras)

print("Las palabras uniscas son", unicas)

repetidas = {}

for palabra in palabras:
    repetidas[palabra] = repetidas.get(palabra, 0) +1

print("Las palabras aparecen ", repetidas)
