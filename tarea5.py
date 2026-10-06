class vehiculo:
     def __init__(self, marca, modelo, anio, precio):
          self.marca = marca
          self.modelo = modelo
          self.anio = anio
          self.precio = precio
     def descripcion_comercial(self):
      
      return f"{self.marca} {self.modelo} {self.anio} - {self.precio:,.0f} Gs."
     
     def __str__(self):
         return self.descripcion_comercial()

vehiculo1 = vehiculo("Ford", "Mustang fastback", 1968, 90000000)

vehiculo2 = vehiculo("Cadillac", "Escalade", 2026, 900000000)

vehiculo3 = vehiculo("RAM", "2500", 2020, 930000000)

vehiculo4 = vehiculo("Ford", "F-150 Raptor", 2015, 96000000)

print(vehiculo1)
print()
print(vehiculo2)
print()
print(vehiculo3)
print()
print(vehiculo4)
     

    