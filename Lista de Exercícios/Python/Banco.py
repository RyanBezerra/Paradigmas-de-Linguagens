# Questão 3 e 15
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        raise AttributeError("Não é possível modificar o saldo diretamente. Use os métodos depositar() ou sacar().")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                return True
            else:
                raise SaldoInsuficienteException(self.__saldo, valor)
        return False

class SaldoInsuficienteException(Exception):
    def __init__(self, saldo_atual, valor_saque):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        super().__init__(f"Saldo insuficiente. Saldo atual: R${saldo_atual:.2f}, Valor do saque: R${valor_saque:.2f}")

conta_maria = ContaBancaria("Maria", 1000)

print(f"Titular: {conta_maria.titular}")
print(f"Saldo inicial: R${conta_maria.saldo:.2f}")

if conta_maria.depositar(500):
    print(f"Depósito realizado. Novo saldo: R${conta_maria.saldo:.2f}")
else:
    print("Falha no depósito.")

if conta_maria.sacar(200):
    print(f"Saque realizado. Novo saldo: R${conta_maria.saldo:.2f}")
else:
    print("Falha no saque.")

try:
    if conta_maria.sacar(2000):
        print(f"Saque realizado. Novo saldo: R${conta_maria.saldo:.2f}")
except SaldoInsuficienteException as e:
    print(f"Falha no saque: {e}")

try:
    conta_maria.saldo = 5000
except AttributeError as e:
    print(f"Erro ao tentar modificar o saldo: {e}")
