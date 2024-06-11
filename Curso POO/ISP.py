#El Principio de Segregación de Interfaces (Interface Segregation Principle - ISP)
#es otro de los principios SOLID en el desarrollo de software. Este principio establece
#que una clase no debe depender de interfaces que no utiliza. En lugar de tener
#interfaces grandes y complejas que contienen muchos métodos, se deben dividir 
#en interfaces más pequeñas y específicas para que las clases solo implementen
#las interfaces que necesitan. Esto ayuda a reducir la complejidad y el acoplamiento
#en el código, así como a mejorar la cohesión y la flexibilidad del sistema.

from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    def comer(self):
        pass

class Durmiente(ABC):
    pass


class Humano(Trabajador, Comedor, Durmiente):
    def trabajar(self):
       print("El humano está comiendo")

    def comer(self):
       print("El humano está comiendo")

    def dormir(self):
       print("El humano está comiendo")


class Robot(Trabajador):
    def trabajar(self):
        print("El robot está trabajando")


humano = Humano()
robot = Robot()



humano.trabajar()
humano.comer()
humano.dormir()
robot.trabajar()