class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def __str__(self):
        return f"{self.tipo} - {self.potencia} cv"

class Carro:
    def __init__(self, marca, modelo, ano, tipo_motor, potencia_motor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        self.motor = Motor(tipo_motor, potencia_motor)

    def motor(self, tipo_motor):
        print(f"🔧 Motor do {self.modelo}: {tipo_motor}")

    def bateria(self, capacidade_bateria):
        print(f"🔋 Bateria do {self.modelo}: {capacidade_bateria} kWh")

    def pneus(self, tipo_pneu):
        print(f"🛞 Pneus do {self.modelo}: {tipo_pneu}")

    def sobre(self):
        print(f"🚗 {self.marca} {self.modelo} ({self.ano})")
        print(f"🔧 Motor: {self.motor}")

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"🚀 {self.modelo} acelerou para {self.velocidade} km/h")

    def frear(self, decremento):
        self.velocidade = max(0, self.velocidade - decremento)
        print(f"🛑 {self.modelo} freou para {self.velocidade} km/h")

    def exibir_velocidade(self):
        print(f"🏁 Velocidade do {self.modelo}: {self.velocidade} km/h")

carro1 = Carro("Toyota", "Corolla", 2020, "V6", 200)
carro2 = Carro("Honda", "Civic", 2018, "V4", 180)
carro3 = Carro("Ford", "Mustang", 2022, "V8", 450)

def imprimir_separador():
    print("=" * 40)

for carro in [carro1, carro2, carro3]:
    imprimir_separador()
    carro.sobre()
    carro.bateria(12 if carro.marca == "Toyota" else 14 if carro.marca == "Honda" else 15)
    carro.pneus("Radiais" if carro.marca == "Toyota" else "Esportivos" if carro.marca == "Honda" else "Off-road")

imprimir_separador()
print("\n📊 Teste de aceleração e frenagem (Toyota Corolla):")
imprimir_separador()

carro1.acelerar(50)
carro1.exibir_velocidade()
carro1.acelerar(30)
carro1.exibir_velocidade()
carro1.frear(20)
carro1.exibir_velocidade()
carro1.frear(100)
carro1.exibir_velocidade()

imprimir_separador()