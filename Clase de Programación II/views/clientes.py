clientes = []

def agregar_cliente():
    print("\n--- AGREGAR CLIENTE ---")
    cedula = input("Cédula: ")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")

    cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion
    }

    clientes.append(cliente)
    print("Cliente registrado correctamente.\n")


def listar_clientes():
    print("\n--- LISTA DE CLIENTES ---")

    if len(clientes) == 0:
        print("No hay clientes registrados.\n")
        return

    for i, cliente in enumerate(clientes, start=1):
        print(f"\nCliente {i}")
        print(f"Cédula   : {cliente['cedula']}")
        print(f"Nombre   : {cliente['nombre']}")
        print(f"Teléfono : {cliente['telefono']}")
        print(f"Dirección: {cliente['direccion']}")


def buscar_cliente():
    cedula = input("\nIngrese la cédula del cliente: ")

    for cliente in clientes:
        if cliente["cedula"] == cedula:
            print("\nCliente encontrado")
            print(f"Nombre   : {cliente['nombre']}")
            print(f"Teléfono : {cliente['telefono']}")
            print(f"Dirección: {cliente['direccion']}")
            return cliente

    print("Cliente no encontrado.")
    return None


def editar_cliente():
    cedula = input("\nIngrese la cédula del cliente a editar: ")

    for cliente in clientes:
        if cliente["cedula"] == cedula:
            cliente["nombre"] = input("Nuevo nombre: ")
            cliente["telefono"] = input("Nuevo teléfono: ")
            cliente["direccion"] = input("Nueva dirección: ")
            print("Cliente actualizado correctamente.")
            return

    print("Cliente no encontrado.")


def eliminar_cliente():
    cedula = input("\nIngrese la cédula del cliente a eliminar: ")

    for cliente in clientes:
        if cliente["cedula"] == cedula:
            clientes.remove(cliente)
            print("Cliente eliminado correctamente.")
            return

    print("Cliente no encontrado.")


def menu_clientes():
    while True:
        print("\n========== CLIENTES ==========")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Editar cliente")
        print("5. Eliminar cliente")
        print("6. Regresar")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            editar_cliente()
        elif opcion == "5":
            eliminar_cliente()
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")
