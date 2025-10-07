#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla

frase = input("Ingrese palabra o frase: ")
if frase.lower().endswith(('a', 'e', 'i', 'o', 'u')):
    print(frase + "!")
else:
    print(frase)