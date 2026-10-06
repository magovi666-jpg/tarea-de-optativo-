class estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = {}

    def agregar_notas(self, materia, nota):
        self.notas[materia] = nota

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas.values()) / len(self.notas)

    def esta_aprobado(self):
        promedio = self.calcular_promedio()

        return promedio >= 60
    
    def mostrar_boletin(self):
        print(f"==== BOLETÍN DE {self.nombre} ====")

        for materia, nota in self.notas.items():
            print(f"{materia}: {nota}")
        print(f"Promedio: {self.calcular_promedio():.2f}")
        if self.esta_aprobado():
            print("Condición: Aprobado")
        else:
            print("Condición: Reprobado")
    def __str__(self):
        return f"Estudiantes: {self.nombre}"

estudiante = estudiante("Mariangeles González")

estudiante.agregar_notas("Programación", 82)
estudiante.agregar_notas("Matemática", 100)
estudiante.agregar_notas("Sistemas", 100)

estudiante.mostrar_boletin()        

    