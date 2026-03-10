from Participantes import Participante
import threading
import time
from random import randint

class Subasta:
    # Agregue los atributos subastaID, duracion y estado
    def __init__(self, producto, subastaID, duracion = 30): 
        self.producto = producto
        self.subastaID = subastaID
        self.duracion = duracion
        self.oferta_mayor = producto.precio_base
        self.estado = "pendiente"
        self.participantes = []
        self.ganador = None

        #Bots
        self.hilos = []
        #Mutex para proteger el atributo oferta_mayor
        self.mutex = threading.Lock()
        #Timer para cerrar la subasta
        self.timer = None
        #Usuario humano
        self.usuario = None


    def registrar_participante(self, participante):
        self.participantes.append(participante)

    # Cambie la lógica para acceder a un monto ya guardado de un participante y 
    # proceder con la comparación en vez de solo actualizar el monto del
    # participante cuando su oferta sea mayor a la oferta actual de la subasta
    def recibir_oferta(self, participante):
        with self.mutex:
            # Dejare este if por si acaso
            if(self.estado == "finalizada"):
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
    
    # Se podria cambiar la logica de este timer para que los hilos no duerman más de la duración de la subasta
    def iniciar_timer(self):
        if self.timer:
            self.timer.cancel()
        # este if se puede usar para refrescar el tiempo restante de la subasta
        if self.estado == "activa":
            self.timer = threading.Timer(self.duracion, self.finalizar_subasta)
            self.timer.start()
            self.timer.join()
    
    # Alguna que otra cosa fue hecha con IA, como esta función.
    def finalizar_subasta(self):
        """Función que ejecuta el Timer al agotarse el tiempo."""
        with self.mutex:
            self.estado = "finalizada"
            print("\n--- ¡SUBASTA FINALIZADA! ---")
            print(f"Artículo: {self.producto.nombre_producto}")
            print(f"Ganador: {self.ganador.nombre}")
            print(f"Precio final: {self.oferta_mayor}")
            print("----------------------------\n")
            print("Presione Enter para avanzar")

    # =========================
    # Funciones para simular la subasta (Esto tambien podria ser una clase?)
    # =========================
        
    def iniciar_bots(self):
        # Limpiamos primero la lista de hilos
        self.hilos.clear() 
        for participante in self.participantes:
           self.hilos.append(threading.Thread(target=self.accion_bot, args=(participante,)))
    
    # Acciones que van a realizar los demas hilos
    # (Siento que hay una forma más elegante para no usar el mismo if seguido)
    def accion_bot(self, participante):
        cantidad_pujas = 2
        for i in range(cantidad_pujas):
            if (self.estado == "finalizada"):
                return
            monto = randint(100,1500)
            # Tengo que hacer que este numero sea menor al tiempo restante
            tiempo_espera = randint(5,7)
            participante.realizar_oferta(self,monto)
            time.sleep(tiempo_espera)
        if (self.estado == "finalizada"):
                return
        print(f"Participante {participante.nombre} ya no quiere participar")

    # Me olvide como resolver la condicion de carrera al momento de imprimir en el terminal
    def accion_usuario(self):
        while True:
            # Obviamente, se deberia implementar mejor este input para tomar valores decimales 
            # o usar algun algoritmo para pasar de float a string y de string a int 
            try: 
                monto = int(input(f"> Participante {self.usuario.nombre}, ingrese una oferta: "))  

            except(ValueError):
                if(self.estado == "finalizada"): 
                    return      
                print("\nEscriba solo números enteros!")
                continue

            if(self.estado == "finalizada"): 
                return  
                     
            self.usuario.realizar_oferta(self,monto)
        


    # INICIAR SUBASTA
    def simular_subasta(self, nombre):
        self.estado = "activa"
        self.iniciar_bots()
        self.usuario = Participante(len(self.participantes) + 1, nombre)
        hilo_usuario = threading.Thread(target = self.accion_usuario)
        

        for hilo in self.hilos:
            # Posiblemente esta sea la solución para que el programa avance más rapido (Actualización: algo asi)
            hilo.daemon = True
            hilo.start()
        
        hilo_usuario.start()
        self.iniciar_timer()
        
        hilo_usuario.join()
        
        # Porque aveces hay un delay al finalizar el programa? (Actualizacion: ya se porque)
        print("Simulación terminada!")
    
    # porque este objeto sigue existiendo cuando ya no tiene referencias? Maybe sea por los hilos que duermen
    # más que la duración de la subasta o por la referencia mutua entre esta clase y participantes
    #def __del__(self):
        #print("Esta subasta acabo!")