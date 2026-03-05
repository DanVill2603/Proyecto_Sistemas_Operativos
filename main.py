from info_estudiantes import nombres_estudiantes 
from info_proyecto import descripcion_proyecto


def mostrar_menu():
    print("\nOpcion 1: Mostrar miembros")
    print("Opcion 2: Mostrar descripcion")
    print("Opcion 3: Cerrar programa")

if __name__ == "__main__":
    opcion = 0
    print(">>>AVANCE 2 PROYECTO SISTEMAS OPERATIVOS GRUPO 1<<<")

    while opcion != 3:
        mostrar_menu()

        try: 
            opcion = int(input("> Escoja una opcion: "))
        except(ValueError):
            print("\nEscriba solo un numero!")
            continue

        print()
        match opcion:
            case 1:
                nombres_estudiantes()
            case 2:
                descripcion_proyecto()
            case 3:
                print("Programa finalizado con exito.")
                break
            case _:
                print("Entrada incorrecta!")
