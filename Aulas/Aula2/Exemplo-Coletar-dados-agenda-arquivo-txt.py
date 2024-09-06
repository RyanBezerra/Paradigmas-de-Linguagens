
# Coleta Dados do Usuário: Recebe uma lista de nomes e idades.
# Armazena Dados em um Dicionário: Usa um dicionário para associar cada nome à sua idade.
# Salva Dados em um Arquivo .txt: Grava os dados armazenados no dicionário em um arquivo de texto.
# Autor: Ricardo Roberto de Lima..

def coletar_dados():
    """
    Coleta nomes e idades do usuário e os armazena em uma lista de dicionários.
    """
    dados = []
    while True:
        nome = input("Digite o nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        idade = input("Digite a idade: ")
        try:
            idade = int(idade)
        except ValueError:
            print("Idade deve ser um número inteiro. Tente novamente.")
            continue
        
        dados.append({'nome': nome, 'idade': idade})
    return dados

def salvar_em_arquivo(dados, nome_arquivo):
    """
    Salva a lista de dicionários em um arquivo de texto.
    """
    with open(nome_arquivo, 'w') as arquivo:
        for item in dados:
            linha = f"Nome: {item['nome']}, Idade: {item['idade']}\n"
            arquivo.write(linha)

def main():
    """
    Função principal que coordena o fluxo do programa.
    """
    dados = coletar_dados()
    if dados:
        salvar_em_arquivo(dados, 'dados_pessoas.txt')
        print("Dados salvos no arquivo 'dados_pessoas.txt'.")
    else:
        print("Nenhum dado foi coletado.")

if __name__ == "__main__":
    main()
