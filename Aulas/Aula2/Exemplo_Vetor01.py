def ler_vetor():
    # Declara um vetor de 8 posições
    vetor = [0] * 8

    # Lê os valores do vetor
    for i in range(8):
        vetor[i] = int(input("Digite o valor da posição {}: ".format(i)))
    
    return vetor

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

def main():
    vetor = ler_vetor()
    calcular_soma(vetor)


main()
