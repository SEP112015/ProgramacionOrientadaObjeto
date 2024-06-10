###HERENCIAS SIMPLE Y JERARQUICA"
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola estoy hablando un poco")


class Jefe(Persona):
     def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
class Empleado(Persona):
     def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario


class Vacante(Persona):
     def __init__(self, nombre, edad, nacionalidad, universidad, carrera):
        super().__init__(nombre, edad, nacionalidad)
        self.universidad = universidad
        self.carrera = carrera

roberto = Empleado("Carlos Andres", 34, "dominicano", "Programador", 200000)
roberto.hablar()
