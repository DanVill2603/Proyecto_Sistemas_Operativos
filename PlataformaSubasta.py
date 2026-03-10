from Participantes import Participante
from Subasta import Subasta
class PlataformaSubastas:
    def __init__(self):
        self.lista_subastas = []

    # Ahora la plataforma subasta es la que va a crear la subasta para luego añadirla
    # en su array con un ID incremental 
    def agregar_subasta(self, producto, duracion):
        self.lista_subastas.append(Subasta(producto, len(self.lista_subastas) + 1, duracion))

    # Esto se podria usar luego para escoger que subasta simular
    def mostrar_subastas(self):
        for subasta in self.lista_subastas:
            print(f"Subasta del producto: {subasta.producto.nombre_producto}")
    
    # Quemare el código aqui, pues es una simulación de nuestro prototipo
    def simular_subasta(self, personas, usuario):
        opcion = ""
        print(">>> SIMULADOR SUBASTA <<<")
        print("Se subastará un Iphone X con valor inicial de 100")

        # Menu para iniciar o no la simulación
        while opcion != "no":
            print("Desea participar?")
            opcion = input("Si/No: ")

            if(opcion.lower() == "no"):
                print(f"Te esperaremos a la proxima, {usuario}!")
                self.lista_subastas.clear()
                return
            
            elif(opcion.lower() == "si"):
                print("INICIANDO SIMULACION")
                subasta = self.lista_subastas[0]

                for persona in personas:
                    participante = Participante(len(subasta.participantes) + 1, persona)
                    subasta.registrar_participante(participante)
   
                subasta.simular_subasta(usuario)
                self.lista_subastas.clear()    
                return

            else: 
                print("Ingrese una opción correcta!")
               

    #def __del__(self):
        #print("Esta plataforma acabo!")