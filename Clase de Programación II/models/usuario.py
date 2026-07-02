class Usuario:
    def __init__(self, id_usuario, nombre, usuario, contraseña, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.usuario = usuario
        self.contraseña = contraseña
        self.rol = rol

    def mostrar(self):
        return f"{self.nombre} ({self.rol})"
