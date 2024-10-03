package main

import "fmt"

// Interface Animal
type Animal interface {
    EmitirSom() string
}

// Struct Cachorro (similar à subclasse em herança)
type Cachorro struct {
    nome string
}

func (c Cachorro) EmitirSom() string {
    return "Au Au"
}

// Struct Gato (similar à subclasse em herança)
type Gato struct {
    nome string
}

func (g Gato) EmitirSom() string {
    return "Miau"
}

// Função para exibir o som do animal
func mostrarSom(animal Animal) {
    fmt.Println(animal.EmitirSom())
}

// Cliente
func main() {
    cachorro := Cachorro{nome: "Rex"}
    gato := Gato{nome: "Mimi"}

    fmt.Printf("%s diz: ", cachorro.nome)
    mostrarSom(cachorro)

    fmt.Printf("%s diz: ", gato.nome)
    mostrarSom(gato)
}
