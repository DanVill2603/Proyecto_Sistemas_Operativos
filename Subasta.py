from Participantes import Participante
import threading
from random import randint
from datetime import datetime


class Subasta:

    def __init__(self, producto, subastaID, duracion = 30): 
        self.producto = producto
        self.subastaID = subastaID
        self.duracion = duracion

        # Valores protegidos por self.mutex
        self.oferta_mayor = producto.precio_base
        self.estado = "pendiente"
        self.participantes = []
        self.ganador = None

        self.hilos = []

        self.mutex = threading.Lock()
        self.event = threading.Event()

        # LOG
        self.log_lock = threading.Lock()
        self.log_file = "bitacora.log"


    def escribir_log(self, mensaje):
        with self.log_lock:
            with open(self.log_file, "a") as f:
                tiempo = datetime.now().strftime("%H:%M:%S")
                f.write(f"[{tiempo}] {mensaje}\n")



    def registrar_participante(self, participante):
            self.participantes.append(participante)


    def recibir_oferta(self, participante):
        with self.mutex:
            if self.estado == "finalizada":
                return


            monto = participante.oferta_actual
            if monto > self.oferta_mayor:
                self.oferta_mayor = monto
                self.ganador = participante


                mensaje = f"Nueva oferta: {monto} por {participante.nombre}"
                print(mensaje)
                self.escribir_log(mensaje)

            else:
                mensaje = f"Oferta rechazada de {participante.nombre}"
                print(mensaje)
                self.escribir_log(mensaje)


    def finalizar_subasta(self):
        with self.mutex:
            self.estado = "finalizada"
            self.event.set()

            print("\n--- SUBASTA FINALIZADA ---")
            print(f"Producto: {self.producto.nombre_producto}")


            if self.ganador:
                print(f"Ganador: {self.ganador.nombre}")
            else:
                print("Sin ganador")

            print(f"Precio final: {self.oferta_mayor}")
            print("--------------------------\n")
            self.escribir_log("SUBASTA FINALIZADA")


    def iniciar_bots(self):

        self.hilos.clear()

        for participante in self.participantes:
            hilo = threading.Thread(
                target=self.accion_bot,
                args=(participante,)
            )
            self.hilos.append(hilo)


    def accion_bot(self, participante):

        limite = randint(500, 2000)

        while not self.event.is_set():

            incremento = randint(10,100)
            nueva_oferta = participante.oferta_actual + incremento

            if nueva_oferta > limite:
                break

            participante.realizar_oferta(self, nueva_oferta)

            if self.event.wait(randint(1,3)):
                return
        print(f"{participante.nombre} dejó de ofertar")

    def simular_subasta(self):
        self.estado = "activa"
        self.iniciar_bots()
        for hilo in self.hilos:
            hilo.start()
        # temporizador manual
        threading.Timer(self.duracion, self.finalizar_subasta).start()
        for hilo in self.hilos:
            hilo.join()
        print("Simulación terminada")
