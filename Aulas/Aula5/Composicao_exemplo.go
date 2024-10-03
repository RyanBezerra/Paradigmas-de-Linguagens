package main

import "fmt"

// Struct Motor
type Motor struct {
    tipo    string
    potencia int
}

func (m Motor) Ligar() {
    fmt.Println("O motor está ligado.")
}

func (m Motor) Desligar() {
    fmt.Println("O motor está desligado.")
}

// Struct Pneu
type Pneu struct {
    marca  string
    tamanho int
}

func (p Pneu) Inflar() {
    fmt.Println("O pneu está inflado.")
}

func (p Pneu) Desinflar() {
    fmt.Println("O pneu está desinflado.")
}

// Struct Carro
type Carro struct {
    marca  string
    modelo string
    motor  Motor
    pneus  [4]Pneu
}

func NewCarro(marca, modelo string) Carro {
    motor := Motor{"Gasolina", 150}
    pneus := [4]Pneu{}
    for i := 0; i < 4; i++ {
        pneus[i] = Pneu{"Pirelli", 18}
    }
    return Carro{marca, modelo, motor, pneus}
}

func (c Carro) Ligar() {
    c.motor.Ligar()
    fmt.Println("O carro está pronto para rodar.")
}

func (c Carro) Desligar() {
    c.motor.Desligar()
    fmt.Println("O carro foi desligado.")
}

func (c *Carro) TrocarPneu(indice int, novoPneu Pneu) {
    if indice >= 0 && indice < 4 {
        c.pneus[indice] = novoPneu
        fmt.Printf("Pneu %d trocado.\n", indice+1)
    } else {
        fmt.Println("Índice de pneu inválido.")
    }
}

// Cliente
func main() {
    carro := NewCarro("Toyota", "Corolla")
    carro.Ligar()

    // Trocando o pneu da posição 2
    novoPneu := Pneu{"Michelin", 17}
    carro.TrocarPneu(2, novoPneu)

    carro.Desligar()
}
