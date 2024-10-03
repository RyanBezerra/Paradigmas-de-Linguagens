# Questão 7
class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)
            professor.adicionar_escola(self)

    def remover_professor(self, professor):
        if professor in self.professores:
            self.professores.remove(professor)
            professor.remover_escola(self)

    def listar_professores(self):
        return [professor.nome for professor in self.professores]

class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.escolas = []

    def adicionar_escola(self, escola):
        if escola not in self.escolas:
            self.escolas.append(escola)

    def remover_escola(self, escola):
        if escola in self.escolas:
            self.escolas.remove(escola)

    def listar_escolas(self):
        return [escola.nome for escola in self.escolas]

# Exemplo de uso
if __name__ == "__main__":
    escola1 = Escola("Escola A")
    escola2 = Escola("Escola B")

    prof1 = Professor("João")
    prof2 = Professor("Maria")

    escola1.adicionar_professor(prof1)
    escola1.adicionar_professor(prof2)
    escola2.adicionar_professor(prof1)

    print(f"Professores da {escola1.nome}: {escola1.listar_professores()}")
    print(f"Professores da {escola2.nome}: {escola2.listar_professores()}")
    print(f"Escolas onde {prof1.nome} leciona: {prof1.listar_escolas()}")
    print(f"Escolas onde {prof2.nome} leciona: {prof2.listar_escolas()}")
