class Participante:
    def __init__(self, id_participante, nombre):
        self.id_participante = id_participante
        self.nombre = nombre
        self.oferta_actual = 0

    def realizar_oferta(self, subasta, monto):
        print(f"{self.nombre} intenta ofertar {monto}")
        subasta.recibir_oferta(self, monto)