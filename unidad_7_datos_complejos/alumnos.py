#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombres = input(f"Ingresa el nombre del alumno {i+1}: ")
    notas = []

    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombres}: "))
        notas.append(nota)

    alumnos[nombres] = tuple(notas)

for nombres, notas in alumnos.items():
         promedio = sum(notas) / len(notas)
         print(f"El promedio de {nombres} es: {promedio:.2f}")
