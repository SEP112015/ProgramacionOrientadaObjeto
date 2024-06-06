###POLIMORFISMO###
class Animal():
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        return "Miau"


class Perro(Animal):
    def sonido(self):
         return "Guau"


def hacer_sonido(animal):
    print(animal.sonido())


gato = Gato()
perro = Perro()

hacer_sonido(perro)
hacer_sonido(gato)

print (gato.sonido())

###POLIMORFISMO DE COERCIÓN AUTOMÁTICO###

# num1 = 3
# num2 = 4.4

# resultado = num1 + num2
# print(resultado)
# print(type(resultado))

### OTRO EJEMPLO DE POLIMORFISMO DE COERCIÓN###

# def recorer(elemento):
#     for intem in elemento:
#         print(intem)

# lista = [1,2,3,4,5,6,7]
# lista2 = ["Carlos", "La", "Maquina"]

# recorer(lista)
# recorer(lista2)
