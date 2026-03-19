class Participante:
    def __init__(self, id_participante, nombre):
        self.id_participante = id_participante
        self.nombre = nombre
        self.oferta_actual = 0

    def realizar_oferta(self, subasta, monto):
        if(monto > self.oferta_actual):
            self.oferta_actual = monto
            print(f"\n{self.nombre} intenta ofertar {monto}")
            subasta.recibir_oferta(self)
        else: 
            print(f"\nNueva oferta de {self.nombre} es menor o igual a su anterior oferta!")

    #def __del__(this):
        #print(f"{this.nombre} se va!")