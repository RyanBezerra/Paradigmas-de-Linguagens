class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = None  # Inicialmente a pessoa não tem endereço

    def adicionar_endereco(self, endereco):
        self.endereco = endereco

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
        if self.endereco:
            print("Endereço:")
            self.endereco.mostrar_endereco()
        else:
            print("Endereço não disponível")


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
        print(f"Funcionários da empresa {self.nome}:")
        for funcionario in self.funcionarios:
            print(funcionario.nome)

# Exemplo de uso
endereco1 = Endereco("Av. Principal", "Cidade A", "Estado X", "12345-678")
pessoa1 = Pessoa("João", 30)
pessoa1.adicionar_endereco(endereco1)

endereco2 = Endereco("Rua Secundária", "Cidade B", "Estado Y", "98765-432")
pessoa2 = Pessoa("Maria", 25)
pessoa2.adicionar_endereco(endereco2)

empresa = Empresa("Empresa ABC", "12345678901234")
empresa.contratar_funcionario(pessoa1)
empresa.contratar_funcionario(pessoa2)

empresa.listar_funcionarios()
