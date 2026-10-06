class cuentacorriente:
     def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo

     def acreditar(self, monto):
         if monto > 0:
             self.saldo += monto
             print(f"Se acreditaron {monto:,.0f} Gs.")
         else: 
             print("El monto a acreditar debe ser mayor a 0.")
     def consumir(self, monto):
         if monto <= 0:
           print("El consumo debe ser mayor que cero.")
         elif monto > self.saldo: 
           print("Compra rechazada: saldo insuficiente.")
         else:
            self.saldo -= monto
            print(f"Compra realizada por {monto:,.0f} Gs.")
         

     def __str__(self):

        return f"Cliente: {self.cliente} - Saldo: {self.saldo:,.0f} Gs."

cuenta = cuentacorriente("Mariangeles González", 100000)
print(cuenta)
cuenta.acreditar(50000)
print(cuenta)
cuenta.consumir(80000)
print(cuenta)
cuenta.consumir(100000)
print(cuenta)
cuenta.consumir(30000)
print(cuenta)


        
