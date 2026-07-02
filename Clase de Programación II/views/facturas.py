def crear_factura():

    print("\n===== CREAR FACTURA =====")

    cedula = input("Cédula del cliente: ")
    fecha = input("Fecha (dd/mm/aaaa): ")

    productos = []

    while True:

        nombre = input("\nProducto (fin para terminar): ")

        if nombre.lower() == "fin":
            break

        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))

        subtotal = cantidad * precio

        productos.append({
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio,
            "subtotal": subtotal
        })

    total = sum(p["subtotal"] for p in productos)

    print("\n========== FACTURA ==========")
    print("Cliente:", cedula)
    print("Fecha:", fecha)

    for p in productos:
        print(
            f"{p['nombre']}  "
            f"{p['cantidad']} x ${p['precio']:.2f} = ${p['subtotal']:.2f}"
        )

    print("-----------------------------")
    print(f"TOTAL: ${total:.2f}")
    print("=============================")


def menu_facturas():

    while True:

        print("\n========== FACTURAS ==========")
        print("1. Crear factura")
        print("2. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":

            crear_factura()

        elif opcion == "2":

            break

        else:

            print("Opción inválida.")
