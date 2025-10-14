#Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def calcular_promedio(a, b, c):
    return   (a + b + c) / 3
 
nro1 = float(input("Ingrese primer numero: "))
nro2 = float(input("Ingrese segundo numero: "))
nro3 = float(input("Ingrese tercer numero: "))

promedio = calcular_promedio(nro1, nro2, nro3)
print(f"El promedio de los tres numeros es {promedio}")
