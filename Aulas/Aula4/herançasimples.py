class Animal:
    def __init__ (self, especie, nome):
        self.especie = especie
        self.nome = nome

    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau"


def main():
    cachorro = Cachorro(especie="Canino", nome="Rex")
    gato = Gato(especie="Felino", nome="Mingau")
    
    print(f"O cachorro {cachorro.nome} da especie {cachorro.especie} faz o som: {cachorro.emitir_som()}")
    print(f"O gato {gato.nome} da especie {gato.especie} faz o som: {gato.emitir_som()}")


main()

