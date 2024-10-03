from typing import Protocol

# Questão 8 e 9
class Empregado:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nome} - {self.cargo} (Salário: R${self.salario:.2f})"

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.empregados = []

    def adicionar_empregado(self, empregado):
        self.empregados.append(empregado)

    def listar_empregados(self):
        print(f"Empregados da {self.nome}:")
        for empregado in self.empregados:
            print(empregado)

class Imprimivel(Protocol):
    def imprimir(self) -> None:
        ...

class Relatorio:
    def __init__(self, titulo: str):
        self.titulo = titulo

    def imprimir(self) -> None:
        print(f"Imprimindo relatório: {self.titulo}")
        print("Conteúdo do relatório...")

class Contrato:
    def __init__(self, numero: str):
        self.numero = numero

    def imprimir(self) -> None:
        print(f"Imprimindo contrato número: {self.numero}")
        print("Termos e condições do contrato...")

def imprimir_documento(doc: Imprimivel) -> None:
    doc.imprimir()

# Exemplo de uso
if __name__ == "__main__":
    empresa = Empresa("Minha Empresa Ltda.")

    emp1 = Empregado("João Silva", "Desenvolvedor", 5000)
    emp2 = Empregado("Maria Santos", "Gerente de Projetos", 7000)
    emp3 = Empregado("Carlos Oliveira", "Analista de Dados", 4500)

    empresa.adicionar_empregado(emp1)
    empresa.adicionar_empregado(emp2)
    empresa.adicionar_empregado(emp3)

    empresa.listar_empregados()

    print("\nTestando a interface Imprimivel:")
    relatorio = Relatorio("Relatório Anual")
    contrato = Contrato("C-12345")

    imprimir_documento(relatorio)
    print()
    imprimir_documento(contrato)
