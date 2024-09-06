# Programa em Python para gerenciar uma agenda telefônica:

# Valida Dados de Contato: Recebe e valida nomes e números de telefone.
# Armazena Dados em um Dicionário: Usa um dicionário para armazenar contatos, onde a chave é o nome e o valor é o número de telefone.
# Salva e Carrega Dados em Arquivo .json: Grava e lê os dados em um arquivo JSON.
# Estrutura do Programa
# Coletar e Validar Dados:

# Receber nome e número de telefone do usuário.
# Validar o formato do número de telefone.
# Manipular Dados:

# Adicionar, editar e excluir contatos no dicionário.
# Salvar e Carregar Dados:

# Gravar e ler dados em um arquivo JSON.

import json
import re

def validar_numero(numero):
    """
    Valida se o número de telefone está no formato correto.
    Exemplo de formato: (11) 12345-6789
    """
    padrao = re.compile(r"^\(\d{2}\) \d{5}-\d{4}$")
    return bool(padrao.match(numero))

def coletar_dados():
    """
    Coleta nome e número de telefone do usuário e os valida.
    """
    contatos = {}
    while True:
        nome = input("Digite o nome do contato (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break

        numero = input("Digite o número de telefone (formato: (11) 12345-6789): ")
        if not validar_numero(numero):
            print("Número de telefone inválido. Tente novamente.")
            continue

        contatos[nome] = numero
    return contatos

def salvar_em_arquivo(contatos, nome_arquivo):
    """
    Salva o dicionário de contatos em um arquivo JSON.
    """
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(contatos, arquivo, indent=4)

def carregar_do_arquivo(nome_arquivo):
    """
    Carrega o dicionário de contatos de um arquivo JSON.
    """
    try:
        with open(nome_arquivo, 'r') as arquivo:
            contatos = json.load(arquivo)
    except FileNotFoundError:
        contatos = {}
    return contatos

def exibir_contatos(contatos):
    """
    Exibe todos os contatos no dicionário.
    """
    if contatos:
        for nome, numero in contatos.items():
            print(f"Nome: {nome}, Telefone: {numero}")
    else:
        print("Nenhum contato encontrado.")

def main():
    """
    Função principal que coordena o fluxo do programa.
    """
    nome_arquivo = 'agenda_telefonica.json'
    contatos = carregar_do_arquivo(nome_arquivo)
    
    while True:
        print("\nMenu:")
        print("1. Adicionar/Editar Contato")
        print("2. Exibir Contatos")
        print("3. Salvar e Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            novos_contatos = coletar_dados()
            contatos.update(novos_contatos)
        elif escolha == '2':
            exibir_contatos(contatos)
        elif escolha == '3':
            salvar_em_arquivo(contatos, nome_arquivo)
            print(f"Dados salvos em '{nome_arquivo}'.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()




