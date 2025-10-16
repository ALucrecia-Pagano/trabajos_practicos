import csv

def verificar_archivo(nombre_filas, encabezados):
    try:
        with open(nombre_filas, mode="r", encoding="utf-8") as f:
            pass 
    except FileNotFoundError:
        with open(nombre_filas, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(encabezados) 
    except Exception as e:
        print("Error al verificar/crear el archivo")

def leer_productos(nombre_filas):
    productos = []
    try:
        with open(nombre_filas, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for fila in reader:
                try:
                    nombre = fila["nombre"].strip()
                    precio = float(fila["precio"])
                    productos.append({"nombre": nombre, "precio": precio})
                except(ValueError, KeyError):
                     print("Fila inválida en el archivo, se omitió.")
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error al leer productos: {e}")
    return productos

def escribir_productos(nombre_filas, encabezados, productos):
    try:
        with open(nombre_filas, mode="w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=encabezados)
            writer.writeheader()
            for p in productos:
                writer.writerow({"nombre": p["nombre"], "precio": f"{p['precio']:.2f}"})
    except Exception as e:
        print(f"Error al guardar productos: {e}")

def mostrar_productos(nombre_filas):
    try:
        productos = leer_productos(nombre_filas)
        if not productos:
            print("\nNo hay productos registrados.\n")
            return #Sirve para salir de la funcion
        print("\n=== LISTA DE PRODUCTOS ===")
        total = 0
        for p in productos:
            print(f"- {p['nombre']}: ${p['precio']:.2f}")
            total += p['precio']
        print(f"\nTotal general: ${total:.2f}\n")
    except Exception as e:
        print(f"Error al mostrar productos: {e}")

def agregar_producto(nombre_filas, encabezados):
    try:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return

        precio_str = input("Ingrese el precio: ").strip()
        try:
            precio = float(precio_str)
            if precio <= 0:
                print("El precio debe ser positivo.")
                return
        except ValueError:
            print("Debe ingresar un número válido.")
            return
        
        productos = leer_productos(nombre_filas)
        productos.append({"nombre": nombre, "precio": precio})
        escribir_productos(nombre_filas, encabezados, productos)
        print("Producto agregado correctamente.\n")
    except Exception as e:
        print(f"Error al agregar producto: {e}")

def eliminar_producto(nombre_filas, encabezados):
    try:
        nombre_buscar = input("Ingrese el nombre del producto a eliminar: ").strip().lower()
        if not nombre_buscar:
            print("Nombre vacío. Operación cancelada.")
            return
        productos = leer_productos(nombre_filas)
        nuevos = []
        for p in productos:
         if p["nombre"].lower() != nombre_buscar:
            nuevos.append(p)
        if len(nuevos) == len(productos):
            print("No se encontró ese producto.")
            return
        
        escribir_productos(nombre_filas, encabezados, nuevos)
        print("Producto eliminado correctamente.\n")
    except Exception as e:
        print(f"Error al eliminar producto: {e}")

# FUNCIÓN: actualizar_precio (DESAFÍO EXTRA)

def actualizar_precio(nombre_filas, encabezados):
    try:
        nombre_buscar = input("Ingrese el nombre del producto a actualizar: ").strip().lower()
        productos = leer_productos(nombre_filas)
        for p in productos:
            if p["nombre"].lower() == nombre_buscar:
                nuevo_precio = input(f"Ingrese nuevo precio para '{p['nombre']}': ").strip()
                try:
                    nuevo_precio = float(nuevo_precio)
                    if nuevo_precio <= 0:
                        print("El precio debe ser positivo.")
                        return
                    p["precio"] = nuevo_precio
                    escribir_productos(nombre_filas, encabezados, productos)
                    print("✅ Precio actualizado correctamente.\n")
                    return
                except ValueError:
                        print("Precio inválido.")
                        return
        print("Producto no encontrado.")
    except Exception as e:
            print(f"Error al actualizar precio: {e}")        

def mostrar_menu():
    print("======= MENÚ DE PRODUCTOS =======")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Actualizar precio")
    print("5. Salir")
    print("=================================")

def menu_principal():
    nombre_filas= "productos.csv"
    encabezados = ["nombre", "precio"]

    verificar_archivo(nombre_filas, encabezados)

    salir = False
    while not salir:
        try:
            mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                mostrar_productos(nombre_filas)
            elif opcion == "2":
                agregar_producto(nombre_filas, encabezados)
            elif opcion == "3":
                eliminar_producto(nombre_filas, encabezados)
            elif opcion == "4":
                actualizar_precio(nombre_filas, encabezados)
            elif opcion == "5":
                print("Saliendo del programa. ¡Hasta luego!")
                salir = True
            else:
                print("Opción inválida. Intente nuevamente.\n")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

menu_principal()




            







                    



