###HERENCIAS MULTIPLES###

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola estoy hablando un poco")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mortrar_habilidad(self):
        return f"mi habilidad es {self.habilidad}" 


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f"Hola soy {self.nombre}, {super().mortrar_habilidad()} y soy {self.empresa}")


Carlos = EmpleadoArtista("Carlos", 23, "español", "cantar", "Apple", 230000)
Carlos.presentarse()
