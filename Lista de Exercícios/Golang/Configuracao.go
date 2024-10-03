// Questão 14
package main

import (
	"fmt"
	"sync"
)

// Configuracao representa as configurações do sistema
type Configuracao struct {
	tema   string
	idioma string
}

var (
	instancia *Configuracao
	once      sync.Once
)

// GetInstancia retorna a única instância de Configuracao
func GetInstancia() *Configuracao {
	once.Do(func() {
		instancia = &Configuracao{
			tema:   "claro",
			idioma: "português",
		}
	})
	return instancia
}

// SetTema define o tema da configuração
func (c *Configuracao) SetTema(tema string) {
	c.tema = tema
}

// SetIdioma define o idioma da configuração
func (c *Configuracao) SetIdioma(idioma string) {
	c.idioma = idioma
}

// GetConfiguracoes retorna as configurações atuais
func (c *Configuracao) GetConfiguracoes() string {
	return fmt.Sprintf("Tema: %s, Idioma: %s", c.tema, c.idioma)
}

func main() {
	config1 := GetInstancia()
	config1.SetTema("escuro")

	config2 := GetInstancia()
	config2.SetIdioma("inglês")

	fmt.Println(config1.GetConfiguracoes())
	fmt.Println(config2.GetConfiguracoes())
	fmt.Printf("config1 e config2 são a mesma instância: %v\n", config1 == config2)
}
