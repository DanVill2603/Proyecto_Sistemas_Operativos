#Descripcion Proyecto
class info_proyecto:
    def __init__(self):
        self.titulo = "Proyecto Sistemas Operativos"
        self.descripcion = "Este proyecto final de la materia UCOM 418 - " \
        "Sistemas Operativos consiste en desarrollar una aplicación que " \
        "permita aplicar los conceptos aprendidos en clase.\n" \
        "\nIdea de proyecto: Plataforma de Subastas.\n"\
        "Sistema que permite a múltiples usuarios participar en una subasta electrónica, " \
        "actualizando las ofertas y determinando el ganador al finalizar el tiempo establecido."

        print("Título del proyecto:")
        
    def descripcion_proyecto(self):
        print(self.titulo)
        print("\nDescripción del proyecto:")
        print(self.descripcion)

