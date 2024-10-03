# Exemplo de aplicação Baseado no modelo de Herança com Python..
class Animal:
    def __init__(self, especie, nome):
        self.especie = especie
        self.nome = nome

    def emitir_som(self):
        pass  # Método a ser implementado nas subclasses

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"

# Fim - Exemplo de aplicação Baseado no modelo de Herança com Python..

