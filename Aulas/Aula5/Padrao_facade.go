package main

import "fmt"

// Subsistema para fazer café
type Cafeteira struct{}

func (c Cafeteira) MoerGraos() {
    fmt.Println("Moendo grãos de café")
}

func (c Cafeteira) FazerCafe() {
    fmt.Println("Fazendo café")
}

// Subsistema para fazer chá
type Chaleira struct{}

func (c Chaleira) FerverAgua() {
    fmt.Println("Fervendo água")
}

func (c Chaleira) FazerCha() {
    fmt.Println("Fazendo chá")
}

// Fachada
type BebidasFacade struct {
    cafeteira Cafeteira
    chaleira  Chaleira
}

func NewBebidasFacade() BebidasFacade {
    return BebidasFacade{
        cafeteira: Cafeteira{},
        chaleira:  Chaleira{},
    }
}

func (b BebidasFacade) PrepararCafe() {
    fmt.Println("\nPreparando café...")
    b.cafeteira.MoerGraos()
    b.cafeteira.FazerCafe()
}

func (b BebidasFacade) PrepararCha() {
    fmt.Println("\nPreparando chá...")
    b.chaleira.FerverAgua()
    b.chaleira.FazerCha()
}

// Cliente
func main() {
    facade := NewBebidasFacade()
    facade.PrepararCafe()
    facade.PrepararCha()
}
