def tamaño_mochila():
    while True:
        try:
            tamaño= int(input("Ingrese cuantos espacios tendra su mochila: "))
            if tamaño <= 0:
                print("El tamaño debe ser un número entero positivo.")
                continue
            return tamaño
        except ValueError:
            print("Error valor invalido. Ingresa un numero entero")

def guardar_objetos(mochila):
    rango = len(mochila)-1
    posicion_str = input(f"Ingrese la posicion (0-{rango}): ").strip()
    objetos = input("Ingresa el objeto magico: ").strip()
    if not objetos:
        print("Error el nombre del objeto no debe estar vacio!!!")
        return
    try:
        posicion = int(posicion_str) 
        mochila[posicion] = objetos
        print(f"el {objetos} se guardo en el espacio {posicion}")
    except ValueError:
      
        print("Error la posición debe ser un número entero.")
    except IndexError:

        print(f"Error la posición {posicion} no existe. Rango válido: 0 a {rango}.")

def ver_contenido(mochila):
    print("\n CONTENIDO DE LA MOCHILA!")

    if not mochila:
        print("La mochila está vacía.")
        return
    for i in range(len(mochila)):
        item = mochila[i] 

        if item is None:
            print(f"Espacio {i}: --- vacío ---") 
        else:
            print(f"Espacio {i}: {item}")

def eliminar_objeto(mochila):
    rango = len(mochila)-1
    posicion_str = input(f"Ingrese la posición del objeto a eliminar (0-{rango}): ").strip()

    try:
        posicion = int(posicion_str) 
        if mochila[posicion] is None:
            print(f"El espacio {posicion} esta vacío. No hay nada que eliminar.")
            return
        
        objeto_eliminado = mochila[posicion]
        mochila[posicion] = None
        print(f"Objeto '{objeto_eliminado}' eliminado del espacio {posicion}.")

    except ValueError:
        print("Error: La posición debe ser un número entero.") 
        
    except IndexError:
        print(f"Error: La posición {posicion_str} no existe. Rango válido: 0 a {rango}.")

def mostrar_menu():
    
    print("\n======= Menú de la Mochila =======")
    print("1. Guardar objeto")
    print("2. Ver mochila")
    print("3. Salir") 
    print("4. Eliminar objeto (Extra)") 
    print("==================================")

def menu_principal():
    
    tamaño = tamaño_mochila()    
    mochila = [None] * tamaño 
    print(f"Mochila creada con {tamaño} espacios (0 a {tamaño - 1}).")

    salir = False
    while not salir:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip() 

        if opcion == "1":
            guardar_objetos(mochila)
        elif opcion == "2":
            ver_contenido(mochila)
        elif opcion == "3":
            print("\nGracias por usar la mochila mágica!") 
            salir = True
        elif opcion == "4":
            eliminar_objeto(mochila)
        else:
            print("Opción inválida. Intente nuevamente.")

menu_principal()









        
            
                
