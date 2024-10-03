import random

def ler_vetor():
    # Inicializar o vetor vazio.
    vetor = []

    # Fazer a leitura e preenchimento dos elementos do vetor.
    for i in range(10):
        vetor.append(int(input(f"Digite o elemento {i}: ")))

    return vetor

def calcular_maior_menor_soma(vetor):
    # Inicializando as variáveis maior e menor.
    maior = vetor[0]
    menor = vetor[0]
    soma = 0

    # Fazer o laço para armazenar os conteúdos dos elementos nas variáveis maior e menor e calcular a soma.
    for i in range(len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
        if vetor[i] < menor:
            menor = vetor[i]
        soma += vetor[i]

    # Exibir o resultado final das variáveis maior, menor e soma.
    print("O maior elemento do vetor é {}.".format(maior))
    print("O menor elemento do vetor é {}.".format(menor))

def calcular_soma(vetor):
    # Lê os valores X e Y
    x = int(input("Digite o valor de X: "))
    y = int(input("Digite o valor de Y: "))

    # Verifica se as posições X e Y são válidas
    if x < 0 or x >= len(vetor) or y < 0 or y >= len(vetor):
        print("Posições inválidas. As posições devem estar entre 0 e 7.")
        return

    # Calcula a soma dos valores nas posições X e Y
    soma = vetor[x] + vetor[y]

    # Imprime a soma
    print("A soma dos valores nas posições X e Y é {}.".format(soma))

def gerar_cartela():
    numeros = set()
    cartela = []

    for _ in range(5):
        linha = []
        for _ in range(5):
            numero = random.randint(0, 99)
            while numero in numeros:
                numero = random.randint(0, 99)
            numeros.add(numero)
            linha.append(numero)
        cartela.append(linha)
    
    return cartela

def imprimir_cartela():
    cartela = gerar_cartela()
    print("Cartela de Bingo:")
    for linha in cartela:
        print(" | ".join(f"{num:>2}" for num in linha))
        print("-" * 29)

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
    return dados

def imprimir_agenda():
    """
    Função principal que coordena o fluxo do programa.
    """
    dados = coletar_dados()
    if dados:
        salvar_em_arquivo(dados, 'dados_pessoas.txt')
        print("Dados salvos no arquivo 'dados_pessoas.txt'.")
    else:
        print("Nenhum dado foi coletado.")
