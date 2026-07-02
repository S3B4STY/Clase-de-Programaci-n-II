from views.menu import menu_principal

def mostrar_bienvenida():

    print("=" * 50)
    print("      SISTEMA DE FACTURACIÓN")
    print("=" * 50)
    print("Proyecto desarrollado en Python")
    print("Base de datos: Excel")
    print("=" * 50)


def main():

    mostrar_bienvenida()

    menu_principal()

    print("\nPrograma finalizado correctamente.")


if __name__ == "__main__":
    main()
