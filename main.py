from info_estudiantes import info_estudiantes
from info_proyecto import info_proyecto
from Producto import Producto
from PlataformaSubasta import PlataformaSubastas
import gc


# TODO: No se xd

# Instancia de la plataforma de subastas
plataforma = PlataformaSubastas()
estudiantes = info_estudiantes()
descripcion = info_proyecto()


def mostrar_menu():
    print("\nOpción 1: Mostrar miembros")
    print("Opción 2: Mostrar descripción")
    print("Opcion 3: Iniciar programa de subasta")
    print("Opción 4: Limpiar log")
    print("Opción 9: Cerrar programa")
    #print(threading.enumerate())
    #print(gc.garbage)

# Esto podria ser una clase?
def simulador_subasta():
    plataforma.agregar_subasta()
    plataforma.simular_subasta()

# Limpiar log 
# (No habria condición de carrera con otras partes del código pues 
# todos los hilos de Subasta.py habrán sido eliminados al ejecutar este bloque)
def limpiar_log():
    opcion = input("Desea limpiar el log? si/no: ")
    if (opcion.lower() == "si" ):
        try:
            open('log_subasta.txt', 'w').close() # Esto crea un Log aunque no exista y lo limpia...
            print("Log limpiado exitosamente!")
        except:
            print("No se pudo limpiar el log!")
    else:
        print("No se limpiará el log")


def main():
    opcion = 0
    print(">>> AVANCE 4 PROYECTO SISTEMAS OPERATIVOS GRUPO 1 <<<")

    while opcion != 9:
        mostrar_menu()
        gc.collect()

        try: 
            opcion = int(input("> Escoja una opción: "))
        except(ValueError):
            print("\nEscriba solo un número!")
            continue

        print()
        match opcion:
            case 1:
                estudiantes.nombres_estudiantes()
            case 2:
                descripcion.descripcion_proyecto()
            case 3:
                simulador_subasta()
            case 4:
                limpiar_log()    
            case 9:
                print("Programa finalizado con éxito.")
                break
            case _:
                print("Entrada incorrecta!")


if __name__ == "__main__":
    main()
    
