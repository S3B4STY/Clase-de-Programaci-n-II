from modelos.usuario import Usuario

class UsuarioController:

    def crear_usuario(self, nombre, usuario, clave):
        nuevo = Usuario(nombre, usuario, clave)
        return nuevo

    def iniciar_sesion(self, usuario, clave):
        pass

    def listar_usuarios(self):
        pass

    def actualizar_usuario(self, id_usuario, datos):
        pass

    def eliminar_usuario(self, id_usuario):
        pass
