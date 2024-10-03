package main

import "fmt"

// Estrutura Animal
type Animal struct {
    nome string
}

func (a Animal) EmitirSom() {
    // Método que será sobrescrito
}

// Estrutura Mamifero
type Mamifero struct {
    Animal
}

func (m Mamifero) Amamentar() {
    fmt.Printf("%s está amamentando.\n", m.nome)
}

// Interface Ave com o comportamento voar
type Ave interface {
    Voar()
}

// Estrutura Morcego que compõe Mamifero e implementa Ave
type Morcego struct {
    Mamifero
}

func (m Morcego) EmitirSom() {
    fmt.Println("Morcego fazendo ruídos noturnos.")
}

func (m Morcego) Voar() {
    fmt.Printf("%s está voando.\n", m.nome)
}

func main() {
    morcego := Morcego{Mamifero{Animal{"Batemane"}}}
    morcego.EmitirSom()   // Método da estrutura Morcego
    morcego.Amamentar()   // Método da estrutura Mamifero
    morcego.Voar()        // Método implementado da interface Ave
}
