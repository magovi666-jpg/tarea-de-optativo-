
class LineaTelefonica:
    def __init__(self, cliente, gigabytes_incluidos):
        self.cliente = cliente
        self.gigabytes_incluidos = gigabytes_incluidos
        self.gigabytes_consumidos = 0

    def registrar_consumo(self, gigabytes):
        if gigabytes <= 0:
            print("El consumo debe ser mayor que cero.")
        else:
            self.gigabytes_consumidos += gigabytes

            print(f"Consumo registrado: {gigabytes} GB.")

            if self.gigabytes_consumidos >= self.gigabytes_incluidos:
                print("AVISO: el paquete de datos se agotó.")

    def gigabytes_disponibles(self):
        disponibles = self.gigabytes_incluidos - self.gigabytes_consumidos

        if disponibles < 0:
            return 0

        return disponibles

    def __str__(self):
        return (
            f"Cliente: {self.cliente}\n"
            f"Plan: {self.gigabytes_incluidos} GB\n"
            f"Consumidos: {self.gigabytes_consumidos} GB\n"
            f"Disponibles: {self.gigabytes_disponibles()} GB"
        )


linea = LineaTelefonica("Mariangeles González", 10)

print(linea)

print()

linea.registrar_consumo(4)
print(linea)

print()

linea.registrar_consumo(3)
print(linea)

print()

linea.registrar_consumo(4)
print(linea)

