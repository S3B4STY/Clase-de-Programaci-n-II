from modelos.pago import Pago

class PagoController:

    def registrar_pago(self, factura_id, monto, metodo):
        pago = Pago(factura_id, monto, metodo)
        return pago

    def listar_pagos(self):
        pass

    def buscar_pago(self, id_pago):
        pass

    def eliminar_pago(self, id_pago):
        pass
