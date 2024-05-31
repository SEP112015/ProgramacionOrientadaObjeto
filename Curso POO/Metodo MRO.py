###MRO###

class A:
    def hablar(self):
        print("Hola desde A")


class B(A):
    def hablar(self):
        print("Hola desde B")


class C(B):
    def hablar(self):
        print("Hola desde C")


class D(C):
    def hablar(self):
        print("Hola desde D")


class E(D):
    def hablar(self):
        print("Hola desde E")


class F(E):
    def hablar(self):
        print("Hola desde F")

class G(F):
    def hablar(self):
        print("Hola desde G")



print(G.mro())