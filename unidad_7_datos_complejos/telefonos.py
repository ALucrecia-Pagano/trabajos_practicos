#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

for i in range(2):
    nombre = input("Ingrese nombre del contacto: ")
    numero = int(input("Ingrese numero de telefono sin '.' ni ',': "))
    contactos[nombre] = numero

consultar = input("Ingrese el contacto que desea consultar: ") 
if consultar in contactos:
    print(f"El numero de {consultar}, es {contactos[consultar]}")
else:
    print("El contacto no existe!")   
