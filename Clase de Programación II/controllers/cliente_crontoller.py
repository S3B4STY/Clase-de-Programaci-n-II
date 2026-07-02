from modelos.cliente import Cliente

class ClienteController:

    def agregar_cliente(self, nombre, cedula, telefono):
        cliente = Cliente(nombre, cedula, telefono)
        return cliente

    def listar_clientes(self):
        pass

    def buscar_cliente(self, id_cliente):
        pass

    def actualizar_cliente(self, id_cliente):
        pass

    def eliminar_cliente(self, id_cliente):
        pass
