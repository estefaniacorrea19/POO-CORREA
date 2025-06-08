from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass  # Método abstracto sin implementación

class Perro(Animal):
    def hacer_sonido(self):
        return "El perro ladra"

mi_perro = Perro()
print(mi_perro.hacer_sonido())  # Salida