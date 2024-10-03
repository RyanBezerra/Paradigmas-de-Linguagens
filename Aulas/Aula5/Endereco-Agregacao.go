package main

import "fmt"

// Estrutura Endereco
type Endereco struct {
    Rua    string
    Cidade string
    Estado string
    CEP    string
}

func (e Endereco) mostrarEndereco() {
    fmt.Printf("Rua: %s, Cidade: %s, Estado: %s, CEP: %s\n", e.Rua, e.Cidade, e.Estado, e.CEP)
}

// Estrutura Pessoa
type Pessoa struct {
    Nome     string
    Idade    int
    Endereco *Endereco
}

func (p *Pessoa) adicionarEndereco(endereco *Endereco) {
    p.Endereco = endereco
}

func (p Pessoa) mostrarInformacoes() {
    fmt.Printf("Nome: %s, Idade: %d\n", p.Nome, p.Idade)
    if p.Endereco != nil {
        fmt.Println("Endereço:")
        p.Endereco.mostrarEndereco()
    } else {
        fmt.Println("Endereço não disponível")
    }
}

// Estrutura Empresa
type Empresa struct {
    Nome         string
    CNPJ         string
    Funcionarios []Pessoa
}

func (e *Empresa) contratarFuncionario(funcionario Pessoa) {
    e.Funcionarios = append(e.Funcionarios, funcionario)
}

func (e Empresa) listarFuncionarios() {
    fmt.Printf("Funcionários da empresa %s:\n", e.Nome)
    for _, funcionario := range e.Funcionarios {
        fmt.Println(funcionario.Nome)
    }
}

// Exemplo de uso
func main() {
    endereco1 := Endereco{"Av. Principal", "Cidade A", "Estado X", "12345-678"}
    pessoa1 := Pessoa{"João", 30}
    pessoa1.adicionarEndereco(&endereco1)

    endereco2 := Endereco{"Rua Secundária", "Cidade B", "Estado Y", "98765-432"}
    pessoa2 := Pessoa{"Maria", 25}
    pessoa2.adicionarEndereco(&endereco2)

    empresa := Empresa{"Empresa ABC", "12345678901234", []Pessoa{}}
    empresa.contratarFuncionario(pessoa1)
    empresa.contratarFuncionario(pessoa2)

    empresa.listarFuncionarios()
}
