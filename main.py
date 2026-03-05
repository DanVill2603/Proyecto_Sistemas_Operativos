from info_estudiantes import nombres_estudiantes 
from info_proyecto import descripcion_proyecto


def mostrar_menu():
    print("\nOpción 1: Mostrar miembros")
    print("Opción 2: Mostrar descripción")
    print("Opción 3: Cerrar programa")

if __name__ == "__main__":
    opcion = 0
    print(">>> AVANCE 2 PROYECTO SISTEMAS OPERATIVOS GRUPO 1 <<<")

    while opcion != 3:
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
                print("Programa finalizado con éxito.")
                break
            case _:
                print("Entrada incorrecta!")
