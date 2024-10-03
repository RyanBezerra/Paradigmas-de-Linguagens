from Funções import ler_vetor, calcular_maior_menor_soma, calcular_soma, imprimir_cartela, coletar_dados, salvar_em_arquivo, imprimir_agenda

def main():
    escolha = int(input("calcular_maior_menor_soma - 1 / calcular_soma - 2 / imprimir_cartela - 3 / coletar_dados - 4: "))
    
    if escolha == 1:
        vetor = ler_vetor()
        calcular_maior_menor_soma(vetor)
    elif escolha == 2:
        vetor = ler_vetor()
        calcular_soma(vetor)
    elif escolha == 3:
        imprimir_cartela()
    elif escolha == 4:
        coletar_dados()
        salvar_em_arquivo()
        imprimir_agenda()


main()
