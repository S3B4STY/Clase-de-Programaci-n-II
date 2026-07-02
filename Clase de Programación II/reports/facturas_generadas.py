from controladores.factura_controller import FacturaController


class FacturasGeneradas:

    def __init__(self):
        self.controlador = FacturaController()

    def mostrar_facturas(self):
        facturas = self.controlador.obtener_facturas()

        if not facturas:
            print("\nNo existen facturas registradas.")
            return

        print("\n========== FACTURAS GENERADAS ==========")
        print("{:<10} {:<20} {:<15} {:<10}".format(
            "Código", "Cliente", "Fecha", "Total"))

        for factura in facturas:
            print("{:<10} {:<20} {:<15} ${:<10.2f}".format(
                factura.codigo,
                factura.cliente.nombre,
                factura.fecha,
                factura.total
            ))
