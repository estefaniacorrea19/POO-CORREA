class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre  # Modifica el atributo

    def get_nombre(self):
        return self.__nombre  # Accede al atributo

persona = Persona("Stefania")
print(persona.get_nombre())  # Salida: José
persona.set_nombre("Carlos")
print(persona.get_nombre())  # Salida: Carlos