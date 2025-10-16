#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

stock = {
    "Leche": 20,
    "Pan": 50,
    "Huevos": 100,
    "Harina": 15,
    "Jugo": 25,
    "Bandejas carne de res": 29,
    "Yerba": 150

}

while True:
    print("\n=== MENÚ DE STOCK ===")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Mostrar todo el stock")
    print("5. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        producto = input("Ingrese el producto a consultar: ")
        if producto in stock:
         print(f"Stock actual de {producto}: {stock[producto]} unidades")
        else:
           print("El producto no existe!")

    elif opcion == "2":
        producto = input("Ingrese el producto al que desea agregar unidades: ")
        if producto in stock:
            agregar = int(input("¿Cuántas unidades desea agregar?: "))
            stock[producto] += agregar
            print(f"Se agregaron {agregar} unidades. Nuevo stock de {producto}: {stock[producto]}")
        else:
            print("Ese producto no existe. Use la opción 3 para agregarlo nuevo.")

    elif opcion == "3":
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto in stock:
            print("El producto ya existe. Use la opción 2 para agregar unidades.")
        else:
            nuevo_stock = int(input("Ingrese la cantidad inicial: "))
            stock[producto] = nuevo_stock
            print(f"Producto {producto} agregado con {nuevo_stock} unidades.")

    elif opcion == "4":
        print("\n=== STOCK ACTUAL ===")
        for producto, cantidad in stock.items():
            print(f"{producto}: {cantidad} unidades")

    elif opcion == "5":
        print("👋 Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("⚠️ Opción inválida. Intente nuevamente.")
             