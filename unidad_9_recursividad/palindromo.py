#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.

def es_palindromo(palabra):
    if len(palabra) <= 1:  # Caso base
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])  # Caso recursivo

# Programa principal
texto = input("Ingrese una palabra: ").lower()
print("Es palíndromo" if es_palindromo(texto) else "No es palíndromo")
