pagos = []

def registrar_pago():
    print("\n===== REGISTRAR PAGO =====")

    numero_factura = input("Número de factura: ")
    cliente = input("Nombre del cliente: ")
    metodo = input("Método de pago (Efectivo/Tarjeta/Transferencia): ")
    monto = float(input("Monto pagado: "))

    pago = {
        "factura": numero_factura,
        "cliente": cliente,
        "metodo": metodo,
        "monto": monto
    }

    pagos.append(pago)

    print("\nPago registrado correctamente.")


def listar_pagos():

    print("\n===== LISTA DE PAGOS =====")

    if len(pagos) == 0:
        print("No existen pagos registrados.")
        return

    for i, pago in enumerate(pagos, start=1):
        print(f"\nPago {i}")
        print(f"Factura : {pago['factura']}")
        print(f"Cliente : {pago['cliente']}")
        print(f"Método  : {pago['metodo']}")
        print(f"Monto   : ${pago['monto']:.2f}")


def buscar_pago():

    numero = input("\nIngrese el número de factura: ")

    for pago in pagos:
        if pago["factura"] == numero:
            print("\n===== PAGO ENCONTRADO =====")
            print(f"Factura : {pago['factura']}")
            print(f"Cliente : {pago['cliente']}")
            print(f"Método  : {pago['metodo']}")
            print(f"Monto   : ${pago['monto']:.2f}")
            return

    print("No se encontró el pago.")


def eliminar_pago():

    numero = input("\nIngrese el número de factura: ")

    for pago in pagos:
        if pago["factura"] == numero:
            pagos.remove(pago)
            print("Pago eliminado correctamente.")
            return

    print("Pago no encontrado.")


def menu_pagos():

    while True:

        print("\n========== PAGOS ==========")
        print("1. Registrar pago")
        print("2. Listar pagos")
        print("3. Buscar pago")
        print("4. Eliminar pago")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_pago()

        elif opcion == "2":
            listar_pagos()

        elif opcion == "3":
            buscar_pago()

        elif opcion == "4":
            eliminar_pago()

        elif opcion == "5":
            break

        else:
            print("Opción inválida.")
