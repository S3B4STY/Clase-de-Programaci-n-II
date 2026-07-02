def menu_facturas():

    while True:

        print("\n===== FACTURAS =====")
        print("1. Crear factura")
        print("2. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":

            crear_factura()

        elif opcion == "2":

            break

        else:

            print("Opción inválida.")
            break

        else:

            print("Opción inválida.")
