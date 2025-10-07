#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

terremoto = float(input("Ingrese la magnitud del terremoto segun la escala de Ritcher: "))
if terremoto <= 3:
    magnitud = "Leve (ligeramente perceptible)"
elif terremoto == 4:
    magnitud = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif terremoto == 5:
    magnitud = "Fuerte (puede causar daños en estructuras débiles)" 
elif terremoto == 6:
     magnitud =   "Muy Fuerte (puede causar daños significativos)"
elif terremoto == 7:
    magnitud =  "Extremo (puede causar graves daños a gran escala)"
else:
    magnitud = "Ingrese un valor valido"

print(magnitud)
