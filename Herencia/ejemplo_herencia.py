class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def mostrar_marca(self):
        return f"Marca: {self.marca}"


class Coche(Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)  # Hereda de Vehiculo
        self.puertas = puertas

    def mostrar_info(self):
        return f"{self.mostrar_marca()}, Número de puertas: {self.puertas}"


mi_coche = Coche("Toyota", 4)
print(mi_coche.mostrar_info())