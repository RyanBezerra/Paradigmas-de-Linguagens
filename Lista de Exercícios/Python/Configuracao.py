# Questão 14
class Configuracao:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.inicializar()
        return cls._instancia

    def inicializar(self):
        self.tema = "claro"
        self.idioma = "português"

    def set_tema(self, tema):
        self.tema = tema

    def set_idioma(self, idioma):
        self.idioma = idioma

    def get_configuracoes(self):
        return f"Tema: {self.tema}, Idioma: {self.idioma}"

# Exemplo de uso da classe Configuracao
config1 = Configuracao()
config1.set_tema("escuro")

config2 = Configuracao()
config2.set_idioma("inglês")

print(config1.get_configuracoes())
print(config2.get_configuracoes())
print(config1 is config2)

