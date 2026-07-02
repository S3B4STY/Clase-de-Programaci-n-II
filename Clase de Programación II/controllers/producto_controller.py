from modelos.producto import Producto

class ProductoController:

    def crear_producto(self, nombre, precio, stock):
        producto = Producto(nombre, precio, stock)
        return producto

    def obtener_productos(self):
        pass

    def buscar_producto(self, id_producto):
        pass

    def actualizar_producto(self, id_producto, datos):
        pass

    def eliminar_producto(self, id_producto):
        pass
