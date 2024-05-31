#C##Lasses###
class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def llamar(self):
        print(f"Estás haciendo una llamada desde un: {self.marca} {self.modelo}")

    def cortar(self):
        print(f"Estás cortando una llamada desde un: {self.marca} {self.modelo}")

###Agregar valores###
celular1 = Celular("Samsung", "Galaxy S4 Ultra")
celular2 = Celular("iPhone", "15 Pro Max")

celular1.llamar()
celular2.cortar()



