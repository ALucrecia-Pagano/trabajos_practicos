import random

num= random.sample(range(1,51), 25)
carton = [num[i:i+5]for i in range(0,25,5)]

bolillero= list(range(1,51))
random.shuffle(bolillero)

while True:
    print("\n presiona enter para sacar un numero")
    nro= bolillero.pop()
    encontrado = False
    for i in range(5):
        for j in range(5):
            if carton[i][j]== nro:
                carton[i][j]= 0
                encontrado= True
    if encontrado:
        print(f"se sorteo el numero: {nro} ------ Tu lo tienes en tu carton!!")
    else:
        print(f"se sorteo el numero: {nro}---- No lo tienes en tu carton!")

    for fila in carton:
        print(fila)

    if any(all(x == 0 for x in fila) for fila in carton):
        print("Linea!!")


    if all(all(x == 0 for x in fila) for fila in carton):
        print("¡¡BINGO!!")
        break        



