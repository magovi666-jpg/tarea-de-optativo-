class cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.duracion} min.)"

class listareproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def duracion_total(self):
        total = 0

        for cancion in self.canciones:
            total += cancion.duracion
        return total
    
    def mostrar_lista(self):
        print(f"==== {self.nombre} ====")

        for cancion in self.canciones:
          print(cancion)
        print (f"Duracion total: {self.duracion_total()} minutos")

cancion1 = cancion("Alive", "Pearl jam", 3.51)
cancion2 = cancion("Brother-Live at the Majestic Theatre, Brooklyn, NY-April 1996", "Alice in Chains", 5.27)
cancion3 = cancion("Down in a Hole", "Alice in chains", 5.38)
cancion4 = cancion("Jeremy", "Pearl jam", 4.18)
cancion5 = cancion("Unhinged", "Slackjaw", 5.28)
cancion6 = cancion("Love, Hate, Love", "Alice in chains", 6.28)
cancion7 = cancion("Rooster (2022 Remaster)", "Alice in chains", 6.18)
cancion8 = cancion("Man in the box", "Alice in chains", 4.45)

lista = listareproduccion("Mis canciones que escuche mientas hacia este codigo")

lista.agregar_cancion(cancion1)
lista.agregar_cancion(cancion2)
lista.agregar_cancion(cancion3)
lista.agregar_cancion(cancion4)
lista.agregar_cancion(cancion5)
lista.agregar_cancion(cancion6)
lista.agregar_cancion(cancion7)
lista.agregar_cancion(cancion8)       
lista.mostrar_lista()