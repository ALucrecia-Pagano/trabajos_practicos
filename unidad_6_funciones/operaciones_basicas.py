#Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de
#sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
   suma = a + b
   resta = a - b
   multiplicacion = a * b
   if b != 0:
      division = a/b
   else:
      print("No se puede dividir por cero")

   return (suma, resta, multiplicacion, division)

nro1 = float(input("Ingrese el primer numero: "))
nro2 = float(input("Ingrese el segundo numero: "))

resultado = operaciones_basicas(nro1, nro2)


print("\n=== RESULTADOS DE LAS OPERACIONES ===")
print(f"el resultado de la suma es {resultado[0]}")
print(f"el resultado de la resta es {resultado[1]}")
print(f"el resultado de la multiplicacion es {resultado[2]}")
print(f"el resultado de la division es {resultado[3]}")
