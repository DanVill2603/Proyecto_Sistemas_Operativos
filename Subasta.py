class Subasta:
    def __init__(self, producto):
        self.producto = producto
        self.oferta_mayor = producto.precio_base
        self.participantes = []

    def registrar_participante(self, participante):
        self.participantes.append(participante)

    def recibir_oferta(self, participante, monto):
        if monto > self.oferta_mayor:
            self.oferta_mayor = monto
            participante.oferta_actual = monto
            print(f"Nueva oferta más alta: {monto} por {participante.nombre}")
        else:
            print("La oferta es menor que la oferta actual.")

    def mostrar_oferta_actual(self):
        print(f"La oferta más alta actual es: {self.oferta_mayor}")