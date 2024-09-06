package main

import "fmt"

// Definindo a estrutura Retangulo
type Retangulo struct {
	comprimento, largura float64
}

// Função para calcular a área do retângulo
func (r Retangulo) calcularArea() float64 {
	return r.comprimento * r.largura
}

// Função para calcular o perímetro do retângulo
func (r Retangulo) calcularPerimetro() float64 {
	return 2 * (r.comprimento + r.largura)
}

func main() {
	// Criando uma instância da estrutura Retangulo
	ret := Retangulo{comprimento: 200, largura: 300}
	fmt.Printf("Área: %.2f\n", ret.calcularArea())
	fmt.Printf("Perímetro: %.2f\n", ret.calcularPerimetro())
}
