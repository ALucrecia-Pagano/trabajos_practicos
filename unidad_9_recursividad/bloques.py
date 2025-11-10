#Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.

def contar_bloques(n):
    if n == 1:  # Caso base
        return 1
    else:
        return n + contar_bloques(n - 1)  # Caso recursivo

# Programa principal
niveles = int(input("Ingrese la cantidad de bloques en la base: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")
