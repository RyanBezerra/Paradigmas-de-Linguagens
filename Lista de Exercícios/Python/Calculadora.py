from abc import ABC, abstractmethod

# Questão 10, 11, 12 e 13
class Calculadora:
    def somar_dois(self, a, b):
        return a + b
    
    def somar_tres(self, a, b, c):
        return a + b + c

# Exemplo de uso da Calculadora
calc = Calculadora()
print(calc.somar_dois(5, 3))
print(calc.somar_tres(5, 3, 2))

# Novas classes de funcionários
class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcularSalario(self):
        pass

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcularSalario(self):
        return self.horas_trabalhadas * self.valor_hora

class FuncionarioAssalariado(Funcionario):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal = salario_mensal

    def calcularSalario(self):
        return self.salario_mensal

# Exemplo de uso dos funcionários
horista = FuncionarioHorista("João", 160, 20)
assalariado = FuncionarioAssalariado("Maria", 3000)

print(f"Salário de {horista.nome}: R${horista.calcularSalario()}")
print(f"Salário de {assalariado.nome}: R${assalariado.calcularSalario()}")

# Nova classe Produto
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __add__(self, outro):
        if isinstance(outro, Produto):
            novo_nome = f"{self.nome} + {outro.nome}"
            novo_preco = self.preco + outro.preco
            return Produto(novo_nome, novo_preco)
        else:
            raise TypeError("Operação não suportada")
    
    def __str__(self):
        return f"{self.nome}: R${self.preco:.2f}"

# Exemplo de uso da classe Produto
produto1 = Produto("Camiseta", 50.0)
produto2 = Produto("Calça", 100.0)
produto_soma = produto1 + produto2

print(f"Produto 1: {produto1}")
print(f"Produto 2: {produto2}")
print(f"Soma dos produtos: {produto_soma}")

# Nova classe Matematica com método estático para fatorial
class Matematica:
    @staticmethod
    def fatorial(n):
        if n < 0:
            raise ValueError("O fatorial não está definido para números negativos")
        if n == 0 or n == 1:
            return 1
        return n * Matematica.fatorial(n - 1)

# Exemplo de uso da classe Matematica
print(f"Fatorial de 5: {Matematica.fatorial(5)}")
print(f"Fatorial de 0: {Matematica.fatorial(0)}")
