class Pago:
    def __init__(self, id, metodo, monto):
        self.id = id
        self.metodo = metodo
        self.monto = monto

    def to_dict(self):
        return {
            "id": self.id,
            "metodo": self.metodo,
            "monto": self.monto
        }
