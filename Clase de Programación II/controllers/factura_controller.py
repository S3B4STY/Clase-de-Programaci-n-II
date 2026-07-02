from modelos.factura import Factura

class FacturaController:

    def crear_factura(self, cliente, productos, total):
        factura = Factura(cliente, productos, total)
        return factura

    def listar_facturas(self):
        pass

    def buscar_factura(self, id_factura):
        pass

    def actualizar_factura(self, id_factura, datos):
        pass

    def eliminar_factura(self, id_factura):
        pass
