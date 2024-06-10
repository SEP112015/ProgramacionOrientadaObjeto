# class Ave:
#     def __init__(self, nombre):
#         self.nombre = nombre


# class AveVoladora(Ave):
#     def volar(self):
#         print(f"Soy un {self.nombre} y estoy volando")
    
# class AveNoVoladora(Ave):
#     def Novolar(self):
#         print(f"Soy un {self.nombre} y no puedo volar")


# ave1 = AveVoladora("Aguila")
# ave1.volar()


# ave1 = AveNoVoladora("Pingüino")
# ave1.Novolar()


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

ave2 = AveNoVoladora("Pinguino")
ave2.mensaje()