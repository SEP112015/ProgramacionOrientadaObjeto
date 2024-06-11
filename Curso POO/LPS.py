#Principio de Sustitución de Liskov (Liskov Substitution Principle - LSP):
#Este principio establece que los objetos de una clase base deben poder 
#ser sustituidos por objetos de sus subclases sin alterar la funcionalidad 
#del programa. En otras palabras, las subclases deben poder ser usadas en lugar 
#de la clase base sin cambiar el comportamiento del programa. 

class Ave:
    def __init__(self, nombre):
        self.nombre = nombre

    def mensaje(self):
        print(f"Soy un {self.nombre}")

class AveVoladora(Ave):
    def volar(self):
        print(f"Soy un {self.nombre} y estoy volando")

class AveNoVoladora(Ave):
    def Novolar(self):
        print(f"Soy un {self.nombre} y no puedo volar")

# Ejemplo de uso
ave1 = AveVoladora("Aguila")
ave1.mensaje()
ave1.volar()

ave2 = AveNoVoladora("Pinguino")
ave2.mensaje()
ave2.Novolar()