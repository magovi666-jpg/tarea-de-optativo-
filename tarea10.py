class producto:
    def __init__(self, nombre,precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - {self.precio:,.0f} Gs."
    
class item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad} = {self.subtotal():,.0f} Gs."

class carrito:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item.subtotal()
        return total
    
    def mostrar_detalle(self):
        print("==== DETALLE DE COMPRA ====")

        for item in self.items:
            print(item)

        print(f"TOTAL: {self.calcular_total():,.0f} Gs.")

arroz = producto("Arroz", 8000)
aceite = producto("Aceite", 12000)
azucar = producto("Azucar", 7000)

item1 = item(arroz, 2)
item2 = item(aceite, 1)
item3 = item(azucar, 3)

carrito = carrito()

carrito.agregar_item(item1)
carrito.agregar_item(item2)
carrito.agregar_item(item3)

carrito.mostrar_detalle()