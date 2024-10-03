// Questão 4 e 5
package main

import (
	"fmt"
)

// Animal é uma interface que define o comportamento comum dos animais
type Animal interface {
	Som() string
	Tipo() string
}

// Cachorro representa um cachorro
type Cachorro struct{}

func (c Cachorro) Som() string {
	return "Au au!"
}

func (c Cachorro) Tipo() string {
	return "Cachorro"
}

// Gato representa um gato
type Gato struct{}

func (g Gato) Som() string {
	return "Miau!"
}

func (g Gato) Tipo() string {
	return "Gato"
}

// Vaca representa uma vaca
type Vaca struct{}

func (v Vaca) Som() string {
	return "Muuu!"
}

func (v Vaca) Tipo() string {
	return "Vaca"
}

// FazerBarulho faz com que todos os animais emitam seus sons
func FazerBarulho(animais []Animal) {
	for _, animal := range animais {
		fmt.Printf("O %s faz: %s\n", animal.Tipo(), animal.Som())
	}
}

func main() {
	cachorro := Cachorro{}
	gato := Gato{}
	vaca := Vaca{}

	animais := []Animal{cachorro, gato, vaca}

	FazerBarulho(animais)
}