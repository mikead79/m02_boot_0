class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def ladrar(self):
        print(f"{self.nombre}: Guau, Guau!")