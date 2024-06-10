###ABSTRACCION##
class Auto():
    def __init__(self):
        self._estado = "Apagado"
    
    def encender(self):
        self._estado = "encendido"
        print("El auto está encendido")

    def conducir(self):
        if self._estado == "Apagado":
            self.encender()
            print("Conduciendo el auto")

mi_auto = Auto()
mi_auto.conducir()

