class turno:
    def __init__(self, paciente, hora):
        self.paciente = paciente
        self.hora = hora 
        self.estado = "Pendiente"
    def marcar_atendido(self):
        self.estado = "Atendido"

    def __str__(self):
        return f"Hora: {self.hora} - Paciente: {self.paciente} - Estado: {self.estado}"

class agenda:
    def __init__(self):
        self.turnos =[]

    def agregar_turno(self, turno):
        self.turnos.append(turno)

    def listar_pendientes(self, turno):
        print("==== TURNOS DISPONIBLES ====")
        for turno in self.turnos:
            if turno.estado == "Pendiente":
                print(turno)

turno1 = turno("Mariangeles González", "08:00")
turno2 = turno("Ariel Villaverde", "09:00")
turno3 = turno("Pamela Delgado", "10:00")

agenda = agenda()

agenda.agregar_turno(turno1)
agenda.agregar_turno(turno2)
agenda.agregar_turno(turno3)

print("==== AGENDA INICIAL ====")

for turno in agenda.turnos:
    print(turno)

turno1.marcar_atendido()
turno3.marcar_atendido()
print()
agenda.listar_pendientes(turno)
