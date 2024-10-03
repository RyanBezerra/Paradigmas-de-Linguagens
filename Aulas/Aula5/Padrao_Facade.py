# Subsistema para fazer café
class Cafeteira:
    def moer_graos(self):
        print("Moendo grãos de café")

    def fazer_cafe(self):
        print("Fazendo café")

# Subsistema para fazer chá
class Chaleira:
    def ferver_agua(self):
        print("Fervendo água")

    def fazer_cha(self):
        print("Fazendo chá")

# Fachada
class BebidasFacade:
    def __init__(self):
        self.cafeteira = Cafeteira()
        self.chaleira = Chaleira()

    def preparar_cafe(self):
        print("\nPreparando café...")
        self.cafeteira.moer_graos()
        self.cafeteira.fazer_cafe()

    def preparar_cha(self):
        print("\nPreparando chá...")
        self.chaleira.ferver_agua()
        self.chaleira.fazer_cha()

# Cliente
if __name__ == "__main__":
    facade = BebidasFacade()
    facade.preparar_cafe()
    facade.preparar_cha()
