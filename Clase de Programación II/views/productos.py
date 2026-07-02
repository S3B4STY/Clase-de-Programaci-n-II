productos = []

def agregar_producto():
    print("\n===== AGREGAR PRODUCTO =====")

    codigo = input("Código: ")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    productos.append(producto)

    print("\nProducto agregado correctamente.")


def listar_productos():

    print("\n===== LISTA DE PRODUCTOS =====")

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    for i, producto in enumerate(productos, start=1):
        print(f"\nProducto {i}")
        print(f"Código : {producto['codigo']}")
        print(f"Nombre : {producto['nombre']}")
        print(f"Precio : ${producto['precio']:.2f}")
        print(f"Stock  : {producto['stock']}")


def buscar_producto():

    codigo = input("\nIngrese el código del producto: ")

    for producto in productos:
        if producto["codigo"] == codigo:
            print("\n===== PRODUCTO ENCONTRADO =====")
            print(f"Código : {producto['codigo']}")
            print(f"Nombre : {producto['nombre']}")
            print(f"Precio : ${producto['precio']:.2f}")
            print(f"Stock  : {producto['stock']}")
            return

    print("Producto no encontrado.")


def editar_producto():

    codigo = input("\nIngrese el código del producto: ")

    for producto in productos:
        if producto["codigo"] == codigo:

            print("\nIngrese los nuevos datos.")

            producto["nombre"] = input("Nombre: ")
            producto["precio"] = float(input("Precio: "))
            producto["stock"] = int(input("Stock: "))

            print("\nProducto actualizado correctamente.")
            return

    print("Producto no encontrado.")


def eliminar_producto():

    codigo = input("\nIngrese el código del producto: ")

    for producto in productos:
        if producto["codigo"] == codigo:
            productos.remove(producto)
            print("\nProducto eliminado correctamente.")
            return

    print("Producto no encontrado.")


def menu_productos():

    while True:

        print("\n========== PRODUCTOS ==========")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Editar producto")
        print("5. Eliminar producto")
        print("6. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            listar_productos()

        elif opcion == "3":
            buscar_producto()

        elif opcion == "4":
            editar_producto()

        elif opcion == "5":
            eliminar_producto()

        elif opcion == "6":
            break

        else:
            print("Opción inválida.")
