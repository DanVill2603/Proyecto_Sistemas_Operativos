from Participantes import Participante
from Subasta import Subasta
from SubastaGUI import SubastaGUI
from Producto import Producto


class PlataformaSubastas:

    def __init__(self):
        self.lista_subastas = []
        self.lista_subastasGUI = []
        self.personas = ["Juanito", "Pedrito", "Maria"]
        self.producto = Producto("Iphone X",100,"Iphone X (no se que otro producto usar de ejemplo)")
        self.duracion = 15



    def agregar_subasta(self):

        subasta = Subasta(self.producto, len(self.lista_subastas) + 1, self.duracion)
        self.lista_subastas.append(subasta)

        subastaGUI = SubastaGUI(self.producto, len(self.lista_subastas) + 1, self.duracion)
        self.lista_subastasGUI.append(subastaGUI)



    def simular_subasta(self):

        print(">>> SIMULADOR SUBASTA <<<")

        opcion = input("¿Iniciar simulación? (si/no): ")

        if opcion.lower() != "si":
            print("Simulación cancelada")
            self.lista_subastas.clear()
            return

        subasta = self.lista_subastas[0] #Esta linea es por si habrá más de una subasta 

        for persona in self.personas:
            participante = Participante(
                len(subasta.participantes) + 1,
                persona
            )
            subasta.registrar_participante(participante)

        subasta.simular_subasta()

        self.lista_subastas.clear()
        self.lista_subastasGUI.clear()

    def simular_subastaGUI(self):
        subasta = self.lista_subastasGUI[0] #Esta linea es por si habrá más de una subasta 

        for persona in self.personas:
            participante = Participante(
                len(subasta.participantes) + 1,
                persona
            )
            subasta.registrar_participante(participante)

        subasta.simular_subasta()

        self.lista_subastas.clear()
        self.lista_subastasGUI.clear()
      