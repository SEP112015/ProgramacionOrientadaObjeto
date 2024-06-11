 #Principio de Responsabilidad Única (Single Responsibility Principle - SRP):
 #Este principio establece que una clase debe tener una única responsabilidad 
 #y motivo para cambiar. Cada clase debe tener una sola razón para cambiar, lo 
 #que ayuda a mantener el código más cohesivo y fácil de mantener. 


class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad



class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia ):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            print("Recuerda que la gasolina no es gratis vete al paso")
        else:
            print("jeje, nos quedamos a pie")    
    
    def obtener_posicion(self):
        return self.posicion
    


tanque = TanqueDeCombustible()
auto = Auto(tanque)

print(auto.obtener_posicion())
print(auto.mover(10))
print(auto.obtener_posicion())
print(auto.mover(20))
print(auto.obtener_posicion())
print(auto.mover(60))
print(auto.obtener_posicion())
print(auto.mover(100))
print(auto.obtener_posicion())
print(auto.mover(100))
print(auto.obtener_posicion())