// Questão 1, 2 e 6
package main

import (
	"fmt"
)

// Motor representa o motor de um carro
type Motor struct {
	Tipo     string
	Potencia int
}

func (m Motor) String() string {
	return fmt.Sprintf("%s - %d cv", m.Tipo, m.Potencia)
}

// Carro representa um carro
type Carro struct {
	Marca      string
	Modelo     string
	Ano        int
	Velocidade int
	Motor      Motor
}

// NovoMotor cria um novo motor para o carro
func (c *Carro) NovoMotor(tipoMotor string) {
	fmt.Printf("🔧 Motor do %s: %s\n", c.Modelo, tipoMotor)
}

// Bateria exibe informações sobre a bateria do carro
func (c *Carro) Bateria(capacidadeBateria int) {
	fmt.Printf("🔋 Bateria do %s: %d kWh\n", c.Modelo, capacidadeBateria)
}

// Pneus exibe informações sobre os pneus do carro
func (c *Carro) Pneus(tipoPneu string) {
	fmt.Printf("🛞 Pneus do %s: %s\n", c.Modelo, tipoPneu)
}

// Sobre exibe informações gerais sobre o carro
func (c *Carro) Sobre() {
	fmt.Printf("🚗 %s %s (%d)\n", c.Marca, c.Modelo, c.Ano)
	fmt.Printf("🔧 Motor: %s\n", c.Motor)
}

// Acelerar aumenta a velocidade do carro
func (c *Carro) Acelerar(incremento int) {
	c.Velocidade += incremento
	fmt.Printf("🚀 %s acelerou para %d km/h\n", c.Modelo, c.Velocidade)
}

// Frear diminui a velocidade do carro
func (c *Carro) Frear(decremento int) {
	if c.Velocidade-decremento < 0 {
		c.Velocidade = 0
	} else {
		c.Velocidade -= decremento
	}
	fmt.Printf("🛑 %s freou para %d km/h\n", c.Modelo, c.Velocidade)
}

// ExibirVelocidade mostra a velocidade atual do carro
func (c *Carro) ExibirVelocidade() {
	fmt.Printf("🏁 Velocidade do %s: %d km/h\n", c.Modelo, c.Velocidade)
}

func imprimirSeparador() {
	fmt.Println("========================================")
}

func main() {
	carro1 := &Carro{Marca: "Toyota", Modelo: "Corolla", Ano: 2020, Motor: Motor{Tipo: "V6", Potencia: 200}}
	carro2 := &Carro{Marca: "Honda", Modelo: "Civic", Ano: 2018, Motor: Motor{Tipo: "V4", Potencia: 180}}
	carro3 := &Carro{Marca: "Ford", Modelo: "Mustang", Ano: 2022, Motor: Motor{Tipo: "V8", Potencia: 450}}

	carros := []*Carro{carro1, carro2, carro3}

	for _, carro := range carros {
		imprimirSeparador()
		carro.Sobre()
		if carro.Marca == "Toyota" {
			carro.Bateria(12)
			carro.Pneus("Radiais")
		} else if carro.Marca == "Honda" {
			carro.Bateria(14)
			carro.Pneus("Esportivos")
		} else {
			carro.Bateria(15)
			carro.Pneus("Off-road")
		}
	}

	imprimirSeparador()
	fmt.Println("\n📊 Teste de aceleração e frenagem (Toyota Corolla):")
	imprimirSeparador()

	carro1.Acelerar(50)
	carro1.ExibirVelocidade()
	carro1.Acelerar(30)
	carro1.ExibirVelocidade()
	carro1.Frear(20)
	carro1.ExibirVelocidade()
	carro1.Frear(100)
	carro1.ExibirVelocidade()

	imprimirSeparador()
}