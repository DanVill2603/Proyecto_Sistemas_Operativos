from Participantes import Participante
import threading
import time
from random import randint

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

        # Bots
        self.hilos = []
        # Mutex para proteger el atributo oferta_mayor
        self.mutex = threading.Lock()
        # Mutex para proteger la lista de los participantes
        self.pmutex = threading.Lock()
        # Timer para cerrar la subasta
        self.timer = None
        # Usuario humano
        self.usuario = None

        # EVENTO PARA FINALIZAR SUBASTA
        self.event = threading.Event()



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
                print(f"Nueva oferta más alta: {monto} por {participante.nombre}")

            else:
                print(f"La oferta del participante {participante.nombre} es menor que la oferta actual.")


    def mostrar_oferta_actual(self):
        print(f"La oferta más alta actual es: {self.oferta_mayor}")


    def mostrar_participantes(self):
        for participante in self.participantes:
            print(f"Participante {participante.nombre}, ultima oferta de: {participante.oferta_actual}")


    def iniciar_timer(self):
        if self.timer:
            self.timer.cancel()

        if self.estado == "activa":
            self.timer = threading.Timer(self.duracion, self.finalizar_subasta)
            self.timer.start()

    def finalizar_subasta(self):
        with self.mutex:
            self.estado = "finalizada"

            self.event.set()
            print("\n--- ¡SUBASTA FINALIZADA! ---")
            print(f"Artículo: {self.producto.nombre_producto}")

            if self.ganador:
                print(f"Ganador: {self.ganador.nombre}")
            else:
                print("No hubo ganador")

            print(f"Precio final: {self.oferta_mayor}")
            print("----------------------------\n")
            with self.pmutex: 
                self.mostrar_participantes()
            print("Presione Enter para avanzar")


    # =========================
    # SIMULACION
    # =========================

    def iniciar_bots(self):
        self.hilos.clear()
        for participante in self.participantes:
            hilo = threading.Thread(
                target=self.accion_bot,
                args=(participante,))
            self.hilos.append(hilo)

    def accion_bot(self, participante):
        cantidad_pujas = 2
        for i in range(cantidad_pujas):
            if self.estado == "finalizada":
                return
            monto = randint(100,1500)
            tiempo_espera = randint(5,7)
            participante.realizar_oferta(self, monto)
            # ESPERA INTERRUMPIBLE
            if self.event.wait(tiempo_espera):
                return
        if self.estado == "finalizada":
            return
        print(f"Participante {participante.nombre} ya no quiere participar")

    def accion_usuario(self):
        while True:
            try: 
                monto = int(input(f"> Participante {self.usuario.nombre}, ingrese una oferta: "))  
            except(ValueError):
                if self.estado == "finalizada":
                    return
                print("\nEscriba solo números enteros!")
                continue
            if self.estado == "finalizada":
                return
            self.usuario.realizar_oferta(self,monto)
        
    #Quemando codigo para testear la entrada de futuros postores durante la subasta    
    def añadir_bot(self):
        time.sleep(7)
        bot = Participante(len(self.participantes) + 1, "Rodrigo")
        h1 = threading.Thread(target=self.accion_bot, args=(bot,))
        with self.pmutex:
            self.participantes.append(bot)
            print(f"{bot.nombre} se une a la subasta!")
        #h1.daemon = True
        h1.start()
        h1.join()

    def simular_subasta(self, nombre):
        self.estado = "activa"
        self.iniciar_bots()
        self.usuario = Participante(len(self.participantes) + 1, nombre)
        hilo_usuario = threading.Thread(target = self.accion_usuario)
        self.participantes.append(self.usuario)

        for hilo in self.hilos:
            hilo.start()
        hilo_usuario.start()
        self.añadir_bot()
        self.iniciar_timer()
        for hilo in self.hilos:
            hilo.join()
        hilo_usuario.join()
        print("Simulación terminada!")
