class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def ligar(self):
        print("O motor está ligado.")

    def desligar(self):
        print("O motor está desligado.")

class Pneu:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho

    def inflar(self):
        print("O pneu está inflado.")

    def desinflar(self):
        print("O pneu está desinflado.")


class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor("Gasolina", 150)  # Composição: Carro tem um Motor
        self.pneus = [Pneu("Pirelli", 18) for _ in range(4)]  # Composição: Carro tem 4 Pneus

    def ligar(self):
        self.motor.ligar()
        print("O carro está pronto para rodar.")

    def desligar(self):
        self.motor.desligar()
        print("O carro foi desligado.")

    def trocar_pneu(self, indice, novo_pneu):
        self.pneus[indice] = novo_pneu
        print(f"Pneu {indice + 1} trocado.")

# Exemplo de uso
carro = Carro("Toyota", "Corolla")
carro.ligar()
# Trocando o pneu da posição 2
novo_pneu = Pneu("Michelin", 17)
carro.trocar_pneu(2, novo_pneu)
carro.desligar()
