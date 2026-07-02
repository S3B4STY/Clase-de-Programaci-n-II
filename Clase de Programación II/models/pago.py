class Pago:
    def __init__(self, id_pago, metodo, fecha, monto):
        self.id_pago = id_pago
        self.metodo = metodo
        self.fecha = fecha
        self.monto = monto

    def mostrar(self):
        return f"Pago: {self.metodo} - ${self.monto:.2f}"
