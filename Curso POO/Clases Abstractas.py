from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre 
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
      pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")
    

class Estudiante(Persona):
    def __init__(self,  nombre, edad, sexo, activdad):
        super().__init__(nombre, edad, sexo, activdad)

    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")


class Trabajador(Persona):
    def __init__(self,  nombre, edad, sexo, activdad):
        super().__init__(nombre, edad, sexo, activdad)

    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el área: {self.actividad}") 

Sebastian = Estudiante("Sebastian", 20, "masculino", "Programación")
Pablo = Trabajador("Pablo", 30, "Caballo", "Programador")

Sebastian.presentarse()
Sebastian.hacer_actividad()

Pablo.presentarse()
Pablo.hacer_actividad()
