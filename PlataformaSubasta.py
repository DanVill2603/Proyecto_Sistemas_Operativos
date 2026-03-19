from Participantes import Participante
from Subasta import Subasta


class PlataformaSubastas:

    def __init__(self):
        self.lista_subastas = []


    def agregar_subasta(self, producto, duracion):

        subasta = Subasta(producto, len(self.lista_subastas) + 1, duracion)
        self.lista_subastas.append(subasta)


    def simular_subasta(self, personas):

        print(">>> SIMULADOR SUBASTA <<<")

        opcion = input("¿Iniciar simulación? (si/no): ")

        if opcion.lower() != "si":
            print("Simulación cancelada")
            self.lista_subastas.clear()
            return

        subasta = self.lista_subastas[0]

        for persona in personas:
            participante = Participante(
                len(subasta.participantes) + 1,
                persona
            )
            subasta.registrar_participante(participante)

        subasta.simular_subasta()

        self.lista_subastas.clear()
      