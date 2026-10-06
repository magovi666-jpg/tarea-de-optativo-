class productostock:
    def __init__(self, nombre, stock, stock_minimo):
        self.nombre = nombre
        self.stock = stock
        self.stock_minimo = stock_minimo

    def ingresar_mercaderias(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad
            print(f"Se ingresaron {cantidad} unidades.")
            self.verificar_stock()
        else:
            print("La cantidad debe ser mayor que cero.")

    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad vendida debe ser mayor que cero.")
        elif cantidad > self.stock:
            print("Venta rechazada: stock insuficiente.")
        else: 
            self.stock -= cantidad
            print(f"venta realizada: {cantidad} unidades.")
            self.verificar_stock()

    def verificar_stock(self):
        if self.stock < self.stock_minimo:
            print("ALERTA: Se necesita reponer mercadería.")
    def __str__(self):
        return f"Producto: {self.nombre} - Stock: {self.stock} unidades - Mínimo: {self.stock_minimo}"

producto = productostock("Galletitas", 10, 5)
print(producto)
producto.vender(4)
print(producto)
producto.vender(3)
print(producto)
producto.vender(10)

producto.ingresar_mercaderias(20)
print(producto)