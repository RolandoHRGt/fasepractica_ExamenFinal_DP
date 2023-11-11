class Curso:
    def __init__(self, nombre, codigo):
        self.nombre =  nombre
        self.codigo = codigo
        self.estudiante_inscritos = []
    
    def inscribir_estudiante(self, estudiante):
        self.estudiante_inscritos.append(estudiante)

    def mostrar_estudiantes(self):
        print(f"Estudiantes inscritos en el curso '{self.nombre}':")
        for estudiante in self.estudiante_inscritos:
            print(estudiante)
    
    