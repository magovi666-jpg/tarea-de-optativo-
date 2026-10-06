class habitacion:
    def __init__(self, numero, tipo, tarifa):
        self.numero = numero
        self.tipo = tipo
        self.tarifa = tarifa
        self.ocupada = False

    def ocupar(self):
        if self.ocupada:
            print(f"La habitación {self.numero} ya está ocupada.")
        else: 
            self.ocupada = True
            print(f"La habitación {self.numero} fue ocupada")

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            print(f"La habitación {self.numero} fue liberada")
        else:
            print(f"La habitación {self.numero} ya estaba libre")

    def calcular_estadia(self, noches):
        return self.tarifa * noches
    def __str__(self):
        if self.ocupada:
            estado = "Ocupada"
        else: 
            estado = "Libre"
        return (
            f"Habitación: {self.numero}\n"
            f"Tipo: {self.tipo}\n"
            f"Tarifa por noche: {self.tarifa:,.0f} Gs.\n"
            f"Estado: {estado}"
        )
habitacion = habitacion(205, "Doble", 350000)
print(habitacion)
print()
habitacion.ocupar()
print(habitacion)
print()
habitacion.ocupar()
costo = habitacion.calcular_estadia(3)
print(f"COSTO DE 3 NOCHES: {costo:,.0f} Gs.")
habitacion.liberar()
print(habitacion)