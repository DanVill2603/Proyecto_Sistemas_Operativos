class PlataformaSubastas:
    def __init__(self):
        self.lista_subastas = []

    def agregar_subasta(self, subasta):
        self.lista_subastas.append(subasta)

    def mostrar_subastas(self):
        for subasta in self.lista_subastas:
            print(f"Subasta del producto: {subasta.producto.nombre_producto}")