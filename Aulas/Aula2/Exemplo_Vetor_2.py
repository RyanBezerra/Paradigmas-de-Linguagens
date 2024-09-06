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

def main():
    vetor = ler_vetor()
    calcular_maior_menor_soma(vetor)
    

main()
