#--------------------------- dia 01/09----------------------------------
def mensaje_encriptado(mensaje, corrimiento, alfabeto):
    resultado= ""
    for caracter in mensaje:
        if caracter.lower() in alfabeto:
            indice= alfabeto.index(caracter.lower())
            inidce_modificado= (indice + corrimiento)% len(alfabeto)
            letra_nueva= alfabeto[inidce_modificado]
            if caracter.isupper():
                letra_nueva= letra_nueva.upper()
                resultado+= letra_nueva
        
        else:
            resultado+= caracter
    return resultado

alfabeto= "abcdefghijklmnñopqrstuvwxyz"
corrimiento= int(input("Ingrese el corrimiento(numero de lugares )"))

for i in range(1,6):    
    mensaje= input(f"Ingrese el mensaje {i}:")
    encriptado= mensaje_encriptado(mensaje,corrimiento,alfabeto)
    print(f"Mensaje encriptado {i}:{encriptado}")