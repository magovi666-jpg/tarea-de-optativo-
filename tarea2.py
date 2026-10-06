class producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self):

        return self.precio * self.cantidad
    def __str__(self):

        return f"Producto: {self.nombre}, Precio: {self.precio:,.0f}, Cantidad: {self.cantidad} "

producto1 = producto("Arroz", 8000, 20)
producto2 = producto("Leche", 13000, 16)
producto3 = producto("Canela", 3500, 1)

#mostrar producto
print(producto1)
print(f"Valor total en stock: {producto1.valor_total():,.0f} Gs.")
print() #linea en blanco
print(producto2)
print(f"Valor total en stock: {producto2.valor_total():,.0f} Gs.")
print()#linea en blanco
print(producto3)
print(f"Valor total en stock: {producto3.valor_total():,.0f} Gs.")