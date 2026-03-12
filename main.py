from info_estudiantes import nombres_estudiantes 
from info_proyecto import descripcion_proyecto
from Producto import Productos
from Subasta import Subasta
from PlataformaSubasta import PlataformaSubastas
import gc
import threading

# TODO: -Cambiar la logica del timer de subastas
#       -Arreglar la condición de carrera de la salida del terminar al iniciar la subasta
#       -Corregir errores ortograficos? Cambiar nombres de variables?

# Parametros para la simulación
personas = ["Juanito", "Pedrito", "Maria"]
producto = Productos("Iphone X",100,"Iphone X (no se que otro producto usar de ejemplo)")
duracion = 15

# Instancia de la plataforma de subastas
plataforma = PlataformaSubastas()


def mostrar_menu():
    print("\nOpción 1: Mostrar miembros")
    print("Opción 2: Mostrar descripción")
    print("Opcion 3: Iniciar programa de subasta")
    print("Opción 9: Cerrar programa")
    #print(threading.enumerate())
    #print(gc.garbage)
    gc.collect()

# Esto podria ser una clase?
def simulador_subasta():
    usuario = str(input("Ingrese su nommbre: "))
    plataforma.agregar_subasta(producto, duracion)
    plataforma.simular_subasta(personas, usuario)

# Ya añadi el metodo main, me confundí en el anterior Avance 2 
def main():
    opcion = 0
    print(">>> AVANCE 4 PROYECTO SISTEMAS OPERATIVOS GRUPO 1 <<<")

    while opcion != 9:
        mostrar_menu()

        try: 
            opcion = int(input("> Escoja una opción: "))
        except(ValueError):
            print("\nEscriba solo un número!")
            continue

        print()
        match opcion:
            case 1:
                nombres_estudiantes()
            case 2:
                descripcion_proyecto()
            case 3:
                simulador_subasta()
                
            case 9:
                print("Programa finalizado con éxito.")
                break
            case _:
                print("Entrada incorrecta!")

# ahora si, este condicional está limpio!
if __name__ == "__main__":
    main()
    
