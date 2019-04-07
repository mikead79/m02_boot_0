def Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
    
    def ladrar(self):
        if self.peso == None:
            print("Soy un fantasma")
        
        if self.peso >= 8:
            print("GUAU GUAU!")
        else:
            print("ay, ay!")

class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def ladrar(self):
        print(f"{self.nombre}: Guau, Guau!")
    
    def __str__(self):
        return f"{self.nombre}: {self.edad} anos y {self.peso} kilos"

class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False
    
    def __str__(self):
        return f"Perro de asistencia de {self.amo}"
    
    def pasear(self):
        print(f"{self.nombre} ayudo a mi dueno, {self.amo} a pasear")
        self.__trabajando = True
    
    def ladrar(self):
        if self.trabajando:
            print("No puerdo ladrar!")
        else:
            Perro.ladrar(self)
    
    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor

    