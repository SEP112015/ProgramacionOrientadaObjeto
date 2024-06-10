###ENCAPSULAMIENTO###

class MiClase:
    def __init__(self):
        self.__atributo_privado = "Valor"

    def __hablar(self):
        print("Hola, como estás?")
    


objeto = MiClase()
print(objeto.__atributo_privado)
print(objeto.__hablar())

