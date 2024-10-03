package main

import "fmt"

// Struct Endereco
type Endereco struct {
    rua    string
    cidade string
    estado string
    cep    string
}

func (e Endereco) MostrarEndereco() {
    fmt.Printf("Rua: %s, Cidade: %s, Estado: %s, CEP: %s\n", e.rua, e.cidade, e.estado, e.cep)
}

// Struct Pessoa
type Pessoa struct {
    nome     string
    idade    int
    endereco *Endereco
}

func NewPessoa(nome string, idade int) *Pessoa {
    return &Pessoa{nome: nome, idade: idade, endereco: nil}
}

func (p *Pessoa) AdicionarEndereco(endereco Endereco) {
    p.endereco = &endereco
}

func (p Pessoa) MostrarInformacoes() {
    fmt.Printf("Nome: %s, Idade: %d\n", p.nome, p.idade)
    if p.endereco != nil {
        fmt.Println("Endereço:")
        p.endereco.MostrarEndereco()
    } else {
        fmt.Println("Endereço não disponível")
    }
}

// Struct Empresa
type Empresa struct {
    nome        string
    cnpj        string
    funcionarios []*Pessoa
}

func NewEmpresa(nome string, cnpj string) *Empresa {
    return &Empresa{nome: nome, cnpj: cnpj, funcionarios: []*Pessoa{}}
}

func (e *Empresa) ContratarFuncionario(funcionario *Pessoa) {
    e.funcionarios = append(e.funcionarios, funcionario)
}

func (e Empresa) ListarFuncionarios() {
    fmt.Printf("Funcionários da empresa %s:\n", e.nome)
    for _, funcionario := range e.funcionarios {
        fmt.Println(funcionario.nome)
    }
}

// Cliente
func main() {
    endereco1 := Endereco{"Av. Principal", "Cidade A", "Estado X", "12345-678"}
    pessoa1 := NewPessoa("João", 30)
    pessoa1.AdicionarEndereco(endereco1)

    endereco2 := Endereco{"Rua Secundária", "Cidade B", "Estado Y", "98765-432"}
    pessoa2 := NewPessoa("Maria", 25)
    pessoa2.AdicionarEndereco(endereco2)

    empresa := NewEmpresa("Empresa ABC", "12345678901234")
    empresa.ContratarFuncionario(pessoa1)
    empresa.ContratarFuncionario(pessoa2)

    empresa.ListarFuncionarios()
}
