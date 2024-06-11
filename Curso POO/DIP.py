#SOLID:  Este principio establece que los módulos de alto nivel 
# no deben depender de los módulos de bajo nivel, sino que ambos
#  deben depender de abstracciones. Además, las abstracciones no 
# deben depender de los detalles, sino que los detalles deben depender 
# de las abstracciones. 


from abc import ABC, abstractclassmethod

class VerficiarOrtografico(ABC):
    @abstractclassmethod
    def verificar_palabra(self, palabra):
        pass


class Diccionario(VerficiarOrtografico):
    def verificar_palabra(self, palabra):
        pass


class VerificadorOrtogradicoOnline(VerficiarOrtografico):
    def verificar_palabra(self, palabra):
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
