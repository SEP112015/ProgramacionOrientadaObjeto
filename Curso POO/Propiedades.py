class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    """LAS PROPIEDADES HACEN QUE SEA MAS DIFICIL HACER UN CAMBIO EN UNA CLASE PRIVADA O ATRIBUTO PRIVADO
       SI USO UN GETTER NO PODRÁ SER MODIFICADO A MENOS QUE USE OTRA PROPIEDAD LA CUAL LLAME AL SETTER Y ME
       Y ME PERMITA MODIFICARLO. LAS PROPIEDADES TAMBIÉN FÁCILITAN LA ESCRITURA DE CÓDIGO YA QUE REDUCE LO 
       QUE TENEMOS QUE ESCRIBIR. 
    """
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, n_nombre):
        self.__nombre = n_nombre
    
    @nombre.deleter
    def nombre(self):
       del self.__nombre

persona = Persona("Sebastian")

nombre = persona.nombre
print(nombre)

###AQUI SE USA LA PROPIEDAD DEL SETTER PARA PODER ACCEDER Y EDITAR LA INFORMACIÓN###

persona.nombre = "Jean Michael"

nombre = persona.nombre
print(nombre)


"""A LA HORA DE USAR EL DELETER NOS DARÁ ERROR SI INTENTAMOS VER LA INFORMACIÓN DE ESTA FUNCIÓN,
   PERO SINO, PUES OBVIO NO DARÁ ERROR SI NO ACCEDEMOS A ELLA """
del persona.nombre

nombre = persona.nombre
print(nombre)
