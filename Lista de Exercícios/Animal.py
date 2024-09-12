class Animal:
    def som(self):
        pass

    def tipo(self):
        return self.__class__.__name__

class Cachorro(Animal):
    def som(self):
        return "Au au!"

class Gato(Animal):
    def som(self):
        return "Miau!"

class Vaca(Animal):
    def som(self):
        return "Muuu!"

def fazer_barulho(animais):
    for animal in animais:
        print(f"O {animal.tipo()} faz: {animal.som()}")

cachorro = Cachorro()
gato = Gato()
vaca = Vaca()

animais = [cachorro, gato, vaca]

fazer_barulho(animais)
