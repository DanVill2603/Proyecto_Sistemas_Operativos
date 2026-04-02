
class info_estudiantes:
    def __init__(self):
        self.lista_estudiantes = ["Daniel Sebastian Gómez Villafuerte"
                            , "Fernando Sebastian Arias Navarro"]
        
        
        

    def nombres_estudiantes(self): 
        print("\n=== Nombres de los estudiantes ===")
        for i in range(len(self.lista_estudiantes)):
            print(f"> Estudiante {i+1}: {self.lista_estudiantes[i]}.")  


