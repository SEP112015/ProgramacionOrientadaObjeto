"""class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def mostrar_grado(self):
        print(f"Grado: {self.grado}")


Juan = Estudiante("Juan", 24,  "7mo")

Juan.mostrar_datos()
Juan.mostrar_grado()"""

class Animal:
    def comer(self):
        print("El animal está comiendo")

class Ave(Animal):
    def volar(self):
        print("El animal está volando")

class Mamifero(Animal):
    def amamantar(self):
        print("El animal está amamantando")

class Murcielago(Ave, Mamifero):
    pass


murcielago = Murcielago()
ave = Ave()

ave.comer()
ave.volar()

murcielago.comer()
murcielago.volar()
murcielago.amamantar()




