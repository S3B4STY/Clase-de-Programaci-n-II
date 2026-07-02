from views.clientes import menu_clientes
from views.productos import menu_productos
from views.facturas import menu_facturas
from views.pagos import menu_pagos
from views.reportes import menu_reportes


def menu_principal():

    while True:

        print("\n======================================")
        print("      SISTEMA DE FACTURACIÓN")
        print("======================================")
        print("1. Clientes")
        print("2. Productos")
        print("3. Facturas")
        print("4. Pagos")
        print("5. Reportes")
        print("6. Salir")
        print("======================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes()

        elif opcion == "2":
            menu_productos()

        elif opcion == "3":
            menu_facturas()

        elif opcion == "4":
            menu_pagos()

        elif opcion == "5":
            menu_reportes()

        elif opcion == "6":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")
