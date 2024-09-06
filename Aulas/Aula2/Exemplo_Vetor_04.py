# Faça um programa em Python que receba 6 numeros inteiros e mostre: ´
#  • Os numeros pares digitados; 
#  • A soma dos numeros pares digitados; 
#  • Os numeros   ımpares digitados;
#  • A quantidade de numeros  ımpares 

def main():
    numeros = []
    numeros_pares = []
    numeros_impares = []
    soma_pares = 0

    for i in range(6):
        numeros.append(int(input("Digite um número: ")))

    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
            soma_pares += numero
        else:
            numeros_impares.append(numero)

    print("Os números pares digitados são:")
    for numero in numeros_pares:
        print(numero)

    print("A soma dos números pares digitados é:", soma_pares)

    print("Os números ímpares digitados são:")
    for numero in numeros_impares:
        print(numero)

    print("A quantidade de números ímpares digitados é:", len(numeros_impares))


if __name__ == "__main__":
    main()
