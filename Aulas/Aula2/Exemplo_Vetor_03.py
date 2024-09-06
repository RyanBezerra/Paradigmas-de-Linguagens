# Faça um programa em Python que receba do usuario dois vetores, ´ A e B, 
# com 10 numeros inteiros cada. Crie um novo vetor denominado C 
# calculando C = A - B. Mostre na tela os dados
# do vetor C.
def main():
    vetor_a = []
    vetor_b = []
    vetor_c = []
    for i in range(10):
        vetor_a.append(int(input("Digite o elemento %d do vetor A: " % i)))
        vetor_b.append(int(input("Digite o elemento %d do vetor B: " % i)))

    for i in range(10):
        vetor_c.append(vetor_a[i] + vetor_b[i])

    print("Vetor C:")
    for i in range(10):
        print(vetor_c[i])

if __name__ == "__main__":
    main()
