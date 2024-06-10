###COMO NO SE DEBE LLAMAR UNA CLASE PRIVADA###

# class Persona:
#     def __init__(self, nombre, edad):
#         self._nombre = nombre
#         self._edad = edad


# Sebastian = Persona("Sebastian", 20)
# print(Sebastian._nombre)


###FORMA CORRECTA (USANDO GETTER) PARA CLASES PRIVADAS Y MUY PRIVADAS###

# class Persona:
#     def __init__(self, nombre, apellido, edad, estudios):
#         self.__nombre = nombre
#         self._apellido = apellido
#         self.__edad = edad
#         self._estudios = estudios

#     def get_nombre(self):
#         return self.__nombre
    
#     def get_apellido(self):
#         return self._apellido

#     def get_edad(self):
#         return self.__edad
    
#     def get_estudios(self):
#         return self._estudios

# Sebastian = Persona("Sebastian", "Escaño", 20, "Desarrollador de Software" )
# nombre = Sebastian.get_nombre()
# edad = Sebastian.get_edad()
# print(f"Hola mi nombre es {nombre} y tengo {edad} años de edad")




###FORMA CORRECTA (USANDO SETTER) PARA CLASES PRIVADAS Y MUY PRIVADAS###

class Persona:
    def __init__(self, nombre, apellido, edad, estudios):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._estudio = estudios

    def get_nombre(self):
        return self._nombre
    
    def get_apellido(self):
        return self._apellido
    
    def get_edad(self):
        return self._edad
    
    def get_estudio(self):
        return self._apellido

    def set_nombre(self, n_nombre):
        self._nombre = n_nombre

    def set_apellido(self, n_apellido):
        self._apellido = n_apellido


Sebastian = Persona("Sebastian", "Escaño", 20, "Desarrollador de Software" )
nombre = Sebastian.get_nombre()
edad = Sebastian.get_edad()
apellido = Sebastian.get_apellido()
estudios = Sebastian.get_estudio()
print(f"Hola mi nombre es {nombre} {apellido} tengo {edad} años de edad y estudio {estudios}")


Sebastian.set_nombre("Carlos")
Sebastian.set_apellido("Caraballo")
nombre = Sebastian.get_nombre()
apellido = Sebastian.get_apellido()
print(f"Hola mi nombre es {nombre} {apellido} tengo {edad} años de edad y estudio {estudios}")





