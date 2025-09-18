alumnos =["juan", "pepe"]
asistencias = [3,6]

while True:
    print("\n-------------MENU DE OPCIONES----------")
    print("1. Lista de estudiantes")
    print("2. Agregar estudiante")
    print("3. listado con asistencias")
    print("4. Consultar asistencias")
    print("5. Consultar asistencias 0")
    print("6. Marcar asistencia (sumar 1)")
    print("7. Lista completa")
    print("8. Salir")

    opcion= input("seleccione una opcion ")
    if opcion == "1" or opcion == "2":
        cantidad= int(input("¿Cuantos alumnos desea agregar? "))
        for i in range(cantidad):
            alumno= input(f"Ingrese el nombre del alumno {i+1} ")
            asistencia= int(input(f"ingrese la cantidad de asistencias {i+1} "))
            alumnos.append(alumno)
            asistencias.append(asistencia)

    elif opcion == "3" or opcion == "7":
        for i in range(len(alumnos)):
            print(f"Alumno {alumnos[i]} asistiencias {asistencias[i]} ")
        if len(alumnos) == 0:
            print("No hay alumnos por listar")

    elif opcion == "4":
        valor_buscado= input("Ingrese el nombre del alumno a consultar: ")
        if valor_buscado in alumnos:
            ind = alumnos.index(valor_buscado)
            print(f"El estudiante: {valor_buscado} tiene {asistencias[ind]} asistencias")
        else:
            print("El estudiante no esta registrado")  

    elif opcion == "5":
        for i in range(len(alumnos)):
            if asistencias[i] == 0:
                print(alumnos[i])
            else:
                print("todos los estudiantes tienen asistencia")    
    elif opcion == "6":
        estudiante = input("Ingrese el nombre del estudiante para marcar asistencia")
        if estudiante in alumnos:
            ind= alumnos.index(estudiante)
            asistencias[ind] += 1
            print(f"Asistencia marcada. {estudiante} ahora tiene {asistencias[ind]} asistencias.")
        else:
            print("El estudiante no está registrado.")
    elif opcion == "7":
             for i in range(len(alumnos)):
              print(f"{alumnos[i]}: {asistencias[i]} asistencias")
    elif opcion == "8":
        print("Saliendo del programa... Gracias!")
        break        
    else:
        print("Opcion no valida ingrese otra")    
            


                  
