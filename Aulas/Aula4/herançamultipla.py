class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def amamentar(self):
        print(f"{self.nome} esta amamentando")

class Ave(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def voar(self):
        print(f"{self.nome} esta voando")

class Morcego(Mamifero, Ave):
    def __init__(self, nome):
        Mamifero.__init__(self, nome)
        Ave.__init__(self, nome)

    def emitir_som(self):
        print("O morcego esta fazendo ruidos noturnos")

morcego = Morcego("Batemane")
morcego.emitir_som()
morcego.amamentar()
morcego.voar()
