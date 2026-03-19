
class Producto:

    def __init__(self, nombre_producto, precio_base, descripcion):
        self.nombre_producto = nombre_producto
        self.precio_base = precio_base
        self.descripcion = descripcion

    def mostrar_info(self):
        print(f"Producto: {self.nombre_producto}")
        print(f"Precio base: {self.precio_base}")
        print(f"Descripción: {self.descripcion}")