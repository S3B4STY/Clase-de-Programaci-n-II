class Cliente:
    def __init__(self, id, cedula, nombres, apellidos, telefono, correo, direccion):
        self.id = id
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def to_dict(self):
        return f"{self.nombres} {self.apellidos} - {self.cedula}"
