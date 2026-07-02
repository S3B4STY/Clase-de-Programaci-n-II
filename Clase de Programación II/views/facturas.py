def crear_factura():
    print("\n===== CREAR FACTURA =====")
    
    cedula = input("Cédula del cliente: ")
    fecha = input("Fecha (dd/mm/aaaa): ")

    print("\nIngrese los productos.")
    print("Escriba 'fin' para terminar.\n")

    productos = []

    while True:
        nombre = input("Producto: ")

        if nombre.lower() == "fin":
            break

        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio unitario: "))

        subtotal = cantidad * precio

        productos.append({
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio,
            "subtotal": subtotal
        })

    total = sum(p["subtotal"] for p in productos)

    print("\n========= FACTURA =========")
    print("Cliente:", cedula)
    print("Fecha:", fecha)

    for producto in productos:
        print(
            f"{producto['nombre']} | "
            f"{producto['cantidad']} x "
            f"${producto['precio']:.2f} = "
            f"${producto['subtotal']:.2f}"
        )

    print("----------------------------")
    print(f"TOTAL: ${total:.2f}")
    print("============================")
