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