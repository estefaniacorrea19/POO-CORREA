class Animal:  #Declaramos la clase
    def hacer_sonido(self):  #Creamos una funcion
        return "El animal hace un sonido"

class Gato(Animal):  #Creamos la clase gatos
    def hacer_sonido(self):
        return "El gato maúlla"

class Perro(Animal):  #Heredemoas de la clase animal
    def hacer_sonido(self):
        return "El perro ladra"

# Lista de diferentes objetos
animales = [Gato(), Perro(), Animal()]  #Creamos una lista

for animal in animales: #Realizamos con un for
    print(animal.hacer_sonido())  #Con un for recorremos la lista