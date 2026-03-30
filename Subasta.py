from Participantes import Participante
import threading
from random import randint
from random import choice
from datetime import datetime


class Subasta:

    def __init__(self, producto, subastaID, duracion = 30): 
        self.producto = producto
        self.subastaID = subastaID
        self.duracion = duracion

        # Valores protegidos por self.mutex
        self.oferta_mayor = producto.precio_base
        self.estado = "pendiente"
        self.ganador = None

        # Valores protegigos por self.pmutex
        self.participantes = []
        self.hilos = []

        self.mutex = threading.Lock()
        self.pmutex = threading.Lock() 
        self.event = threading.Event()
        self.timer = threading.Timer(self.duracion, self.finalizar_subasta) #Se agrego variable timer para mayor control

        # LOG
        self.log_lock = threading.Lock()
        self.log_file = "log_subasta.txt"


    def escribir_log(self, mensaje):
        with self.log_lock:
            with open(self.log_file, "a") as f:
                tiempo = datetime.now().strftime("%H:%M:%S")
                f.write(f"[{tiempo}] {mensaje}\n")



    def registrar_participante(self, participante):
        with self.pmutex:
            self.participantes.append(participante)
        self.escribir_log(f"{participante.nombre} se ha registrado en la subasta.")

    def ver_oferta(self, participante):
        with self.mutex:
            mensaje = f"{participante.nombre} revisa la oferta mayor: {self.oferta_mayor}"
            print ("\n"+mensaje)
            self.escribir_log(mensaje)
            return self.oferta_mayor

    def recibir_oferta(self, participante):
        with self.mutex:
            if self.estado == "finalizada":
                return

            monto = participante.oferta_actual
            if monto > self.oferta_mayor:
                self.oferta_mayor = monto
                self.ganador = participante

                mensaje = f"Nueva oferta más alta: {monto} por {participante.nombre}"
                print("\n" + mensaje)
                self.escribir_log(mensaje)

            else:
                mensaje = f"Oferta de {participante.nombre} rechazada por ser menor a la oferta mayor!"
                print(mensaje)
                self.escribir_log(mensaje)


    def finalizar_subasta(self):
        with self.mutex:
            self.estado = "finalizada"
            self.event.set()

            print("\n--- SUBASTA FINALIZADA ---")
            print(f"Producto: {self.producto.nombre_producto}")

            if self.ganador:
                print(f"Ganador/a: {self.ganador.nombre}")
            else:
                print("Sin ganador")

            print(f"Precio final: {self.oferta_mayor}")
            print("--------------------------\n")
            self.escribir_log("SUBASTA FINALIZADA")
            self.escribir_log(f"Ganador/a: {self.ganador.nombre} con precio final de {self.oferta_mayor}\n")


    def iniciar_bots(self):

        self.hilos.clear()

        for participante in self.participantes:
            hilo = threading.Thread(
                target=self.accion_bot,
                args=(participante,)
            )
            self.hilos.append(hilo)

    # Se ha añadido función para añadir un bot en medio de la subasta
    def añadir_bot(self, nombre):
        if self.event.wait(5):
                return
        bot = Participante(len(self.participantes) + 1, nombre)
        h1 = threading.Thread(target=self.accion_bot, args=(bot,))
        self.registrar_participante(bot)
        print(f"\n{bot.nombre} se une a la subasta!")
        self.hilos.append(h1)
        h1.start()
       
    def accion_bot(self, participante):

        limite = randint(500, 2000)
        pity = 1

        while not self.event.is_set():

            incremento = choice([50,100])
            prob_ofertar = randint(pity,6)
            temp = self.ver_oferta(participante)

            if(prob_ofertar<3):
                pity += 1
                mensaje = f"{participante.nombre} decide no ofertar esta vez"
                print(mensaje)
                self.escribir_log(mensaje)
                if self.event.wait(randint(1,3)):
                    return
                continue
            
            pity = 1
            nueva_oferta = temp + incremento

            if nueva_oferta > limite:
                break

            participante.realizar_oferta(self, nueva_oferta)

            if self.event.wait(randint(1,3)):
                return
        
        mensaje = f"{participante.nombre} dejará de ofertar"
        print(mensaje)
        self.escribir_log(mensaje)

    def simular_subasta(self):
        self.estado = "activa"
        self.iniciar_bots()
        
        for hilo in self.hilos:
            hilo.start()
        # Temporizador manual 
        self.timer.start()
        # Las llamadas a añadir_bot siempre iran despues de iniciar el timer
        self.añadir_bot("Don Pepe")

        for hilo in self.hilos:
            hilo.join()
        
        self.timer.join() #podria ser un daemon
        
        print("Simulación terminada")
