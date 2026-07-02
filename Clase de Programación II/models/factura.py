class Factura:
    def __init__(self, id, cliente, producto, precio):
        self.id = id
        self.cliente = cliente
        self.producto = producto
        self.precio = precio

    def mostrar_factura(self):
        return {
            "id": self.id,
            "cliente": self.cliente,
            "producto": self.producto,
            "precio": self.precio
        }
