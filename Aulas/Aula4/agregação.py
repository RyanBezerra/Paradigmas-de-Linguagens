class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = None

    def adicionar_endereco(self, endereco):
        self.endereco = endereco

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
        if self.endereco:
            print("Endereco:")
            self.endereco.mostrar_endereco()
        else:
            print("Endereco nao disponivel")

class Endereco:
    def __init__(self, rua, cidade, estado, cep):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def mostrar_endereco(self):
        print(f"Rua: {self.rua}, Cidade: {self.cidade}, Estado: {self.estado}, CEP: {self.cep}")

class Empresa:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.funcionarios = []

    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario) 

    def listar_funcionarios(self):
        print(f"Funcionarios da empresa {self.nome}:")
        for funcionario in self.funcionarios:
            print(funcionario.nome)

def main():
    pessoa1 = Pessoa("Ana", 30)
    pessoa2 = Pessoa("Carlos", 25)

    endereco1 = Endereco("Rua das Flores, 123", "Sao Paulo", "SP", "01000-000")
    endereco2 = Endereco("Avenida Brasil, 456", "Rio de Janeiro", "RJ", "20000-000")

    pessoa1.adicionar_endereco(endereco1)
    pessoa2.adicionar_endereco(endereco2)

    empresa = Empresa("Tech Solutions", "12.345.678/0001-99")

    empresa.contratar_funcionario(pessoa1)
    empresa.contratar_funcionario(pessoa2)

    pessoa1.mostrar_informacoes()
    pessoa2.mostrar_informacoes()

    empresa.listar_funcionarios()

if __name__ == "__main__":
    main()
