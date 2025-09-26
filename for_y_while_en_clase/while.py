#-------------------------------trabajo dia 01/09-----------------------------------
import random
puntaje_jugador= 0
puntaje_maquina= 0
opciones= ["piedra", "papel", "tijera"]
while True:
    print("\n-----MENU-----")
    print("1. piedra")
    print("2. papel")
    print("3. tijera")
    print("4. salir")
    eleccion= input("ingrese su eleccion del 1 al 4")
    if eleccion == 4:
        break
    if eleccion not in["1","2","3"]:
        print("opcion invalida")
        continue
    jugador= opciones[int(eleccion)-1]
    computadora= random.choice(opciones)
    print("f tu{jugador} | computadora {computadora}")

    if jugador == computadora:
        print("Empate")
    elif (jugador, computadora) in [("piedra" , "tijera"), ("tijera" , "papel"), ("papel", "piedra")]:
        print("Ganaste!")
        puntaje_jugador +=1 
    else:
        print("Perdiste")  
        puntaje_maquina +=1

    print(f"Puntaje-> jugador: {puntaje_jugador},| computadora {puntaje_maquina} ")    
    print(f"""Resultado final
          jugador: {puntaje_jugador}
       computadora: {puntaje_maquina}""")  