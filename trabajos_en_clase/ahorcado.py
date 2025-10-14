import random

def seleccionar_palabra():
    palabras = ["python","programacion","funcion","algoritmo","desarrollo","variable"]

    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):

    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + ""
        else:
            tablero += "_"
    return tablero.strip() 

def jugar_ahorcado(): #Función principal que contiene toda la lógica del juego

    palabra_secreta = seleccionar_palabra()
    letras_adivinadas = set() # set sirve para almacenar letras únicas más eficientemente
    intentos_maximos = 6      
    intentos_restantes = intentos_maximos
    juego_terminado = False

    print("¡Bienvenido al juego del Ahorcado! 🔪")
    print("-" * 40) #Para "decorar" va a mostrar 40 -----
    print(f"La palabra tiene {len(palabra_secreta)} letras. ¡Adivina!")
    print(mostrar_tablero(palabra_secreta, letras_adivinadas))
    print("-" * 40)

    while not juego_terminado:
        
            entrada = input("\nIngresa una letra: ").lower().strip()

            if not entrada.isalpha() or len(entrada) != 1:
                print("Entrada inválida. Por favor, ingresa una letra.")
                continue

            letra_actual = entrada

            if letra_actual in letras_adivinadas:
                print(f"Ya intentaste la letra '{letra_actual}'. Prueba con otra.")
                continue

            letras_adivinadas.add(letra_actual)

            if letra_actual in palabra_secreta:
                print("¡Adivinaste una letra correctamente!")
            else:
                intentos_restantes -= 1
                print(f" Letra incorrecta. Te quedan {intentos_restantes} intentos.")

            estado_actual = mostrar_tablero(palabra_secreta, letras_adivinadas)
            print(f"\nTablero: {estado_actual}")

            palabra_completa = True
            for letra in palabra_secreta:
          
                if letra not in letras_adivinadas:
                    palabra_completa = False
                    break 
            if palabra_completa:
                print("\n" + "="*40)
                print("¡FELICITACIONES Has ganado el juego del ahorcado!")
                print(f"La palabra secreta era: {palabra_secreta.upper()}")
                print("="*40)
                juego_terminado = True

            if intentos_restantes <= 0:
                print("\n" + "="*40)
                print("💀 Te quedaste sin intentos. Has perdido.")
                print(f"La palabra secreta era: {palabra_secreta.upper()}")
                print("="*40)
                juego_terminado = True
jugar_ahorcado()                




