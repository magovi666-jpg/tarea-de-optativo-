class cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}\nCédula: {self.cedula}\nTelefono: {self.telefono}"

cliente1 = cliente("Mariangeles González", "6.518.207", "0985 586 594")

cliente2 = cliente("Fernanda Arce", "5.271.963", "0986 459 875")

print("====FICHA DEL CLIENTE====")

print(cliente1)
print()#linea en blanco
print("====FICHA DEL CLIENTE====")
print(cliente2)