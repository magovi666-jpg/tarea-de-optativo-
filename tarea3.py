class empleado:
    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def salario_anual(self):

        return self.salario_mensual * 13
    def __str__(self):

        return f"Nombre: {self.nombre}\nCargo: {self.cargo}\nSalario: {self.salario_mensual}:,.0f Gs."

empleado1 = empleado("Mariangeles González", "Vendedor", 4000000)
empleado2 = empleado("Fernanda Arce", "Contadora", 1500000)

print(empleado1)
print(f"Salario anual con aguinaldo: {empleado1.salario_anual():,.0f} Gs.")
print()#linea en blaco
print(empleado2)
print(f"Salario anual con aguinaldo: {empleado2.salario_anual():,.0f} Gs.")
