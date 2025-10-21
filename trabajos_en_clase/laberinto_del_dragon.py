#(# = pared, = camino, D = dragón, E = salida).

laberinto = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", "D", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", "#", "E", "#", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]

def mostrar(laberinto):
    for fila in laberinto:
        print("".join(fila))
        print()

def buscar(laberinto, fila, columna):
    if fila < 0 or fila >= len(laberinto) or  columna < 0 or columna >= len(laberinto[0]):
        return False

    if laberinto[fila][columna] == "#" or laberinto[fila][columna] == ".":
        return False 

    if laberinto[fila][columna] == "E":
        print("ENCONTRO LA SALIDA")
        return True 

    if laberinto[fila][columna] !="D":
        laberinto[fila][columna] ="."    

    if (buscar(laberinto, fila -1, columna)or 
        buscar(laberinto, fila +1, columna)or
        buscar(laberinto, fila-1, columna)or
        buscar(laberinto, fila +1, columna)):
        return True

    if laberinto[fila][columna] !="D":
        laberinto[fila][columna] = ""
        return False

inicio = None

for i in range(len(laberinto)):
     for j in range(len(laberinto[0])):
         if laberinto[i][j] == "D":
                inicio = (i,j)

print("LABERINTO INICIAL")
mostrar(laberinto)

if inicio and buscar(laberinto, inicio[0], inicio[1]):
    print("Camino encontrado")
else:
    print("No hay salida posible!")
