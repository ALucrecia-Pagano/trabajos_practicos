# productos.py
import os

ARCHIVO = "productos.txt"

def crear_archivo_inicial():
    """Crea productos.txt con 3 productos si no existe o está vacío."""
    if not os.path.exists(ARCHIVO) or os.path.getsize(ARCHIVO) == 0:
        inicial = [
            "Lapicera,120.5,30",
            "Cuaderno,250.0,50",
            "Tijera,80.0,15"
        ]
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            for linea in inicial:
                f.write(linea + "\n")
        print(f"Se creó '{ARCHIVO}' con {len(inicial)} productos iniciales.")

def cargar_productos():
    """
    Lee el archivo y devuelve una lista de diccionarios:
    [{'nombre': str, 'precio': float, 'cantidad': int}, ...]
    También ignora líneas mal formadas y muestra aviso.
    """
    productos = []
    if not os.path.exists(ARCHIVO):
        return productos
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for nlinea, linea in enumerate(f, start=1):
            linea = linea.strip()
            if not linea:
                continue
            partes = [p.strip() for p in linea.split(",")]
            if len(partes) != 3:
                print(f"Aviso: línea {nlinea} mal formada (se esperan 3 campos): '{linea}' - se omite.")
                continue
            nombre, precio_s, cant_s = partes
            try:
                precio = float(precio_s)
                cantidad = int(float(cant_s))  # acepta "15.0" también
            except ValueError:
                print(f"Aviso: línea {nlinea} valores numéricos inválidos: '{linea}' - se omite.")
                continue
            productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    return productos

def mostrar_productos(productos):
    """Muestra los productos en el formato pedido."""
    if not productos:
        print("No hay productos para mostrar.")
        return
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

def agregar_producto(productos):
    """
    Pide al usuario datos de un nuevo producto, lo agrega a la lista y
    lo añade al archivo sin borrar su contenido existente (modo 'a').
    Permite ingresar varios productos hasta que el usuario diga 'n'.
    """
    while True:
        print("\nIngrese los datos del nuevo producto (o deje el nombre vacío para cancelar):")
        nombre = input("  Nombre: ").strip()
        if nombre == "":
            print("Alta cancelada por el usuario.")
            break
        precio_s = input("  Precio: ").strip()
        cantidad_s = input("  Cantidad: ").strip()

        # Validar y convertir
        try:
            precio = float(precio_s)
            cantidad = int(float(cantidad_s))
        except ValueError:
            print("  Error: 'precio' debe ser número (ej. 120.5) y 'cantidad' debe ser entero. Intente de nuevo.")
            continue

        # Construir diccionario y añadir a la lista
        nuevo = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        productos.append(nuevo)

        # Añadir al archivo en modo append para no borrar lo existente (según requisito 3)
        with open(ARCHIVO, "a", encoding="utf-8") as f:
            f.write(f"{nombre},{precio},{cantidad}\n")

        print(f"  Producto '{nombre}' agregado correctamente.")

        mas = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
        if mas != "s":
            break

def buscar_producto(productos):
    """
    Pide un nombre y busca en la lista. Búsqueda case-insensitive.
    Si encuentra, muestra los datos; si no, muestra error.
    """
    if not productos:
        print("La lista de productos está vacía, no se puede buscar.")
        return
    termino = input("\nIngrese el nombre del producto a buscar: ").strip()
    if termino == "":
        print("Búsqueda cancelada.")
        return
    encontrado = None
    for p in productos:
        if p["nombre"].lower() == termino.lower():
            encontrado = p
            break
    if encontrado:
        print("Producto encontrado:")
        print(f"  Nombre: {encontrado['nombre']}")
        print(f"  Precio: ${encontrado['precio']}")
        print(f"  Cantidad: {encontrado['cantidad']}")
    else:
        print(f"Error: el producto '{termino}' no existe en la lista.")

def guardar_productos(productos):
    """
    Sobrescribe productos.txt escribiendo todos los productos desde la lista.
    (Requisito 6)
    """
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print(f"\nSe guardaron {len(productos)} productos en '{ARCHIVO}' (archivo sobrescrito).")

def main():
    crear_archivo_inicial()

    # 2 y 4: leer archivo y cargar lista de diccionarios
    productos = cargar_productos()

    # 2: mostrar productos
    print("\n--- Productos actuales ---")
    mostrar_productos(productos)

    # 3: agregar productos desde teclado (se añaden al archivo en modo 'a' y a la lista)
    agregar_producto(productos)

    # 5: buscar producto por nombre
    buscar_producto(productos)

    # 6: guardar productos actualizados sobrescribiendo el archivo
    guardar_productos(productos)
    print("Programa finalizado.")

if __name__ == "__main__":
    main()
