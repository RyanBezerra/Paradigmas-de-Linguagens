// Questão 7
package main

import (
	"fmt"
)

// Escola representa uma instituição de ensino
type Escola struct {
	Nome        string
	Professores []*Professor
}

// AdicionarProfessor adiciona um professor à escola
func (e *Escola) AdicionarProfessor(professor *Professor) {
	for _, p := range e.Professores {
		if p == professor {
			return
		}
	}
	e.Professores = append(e.Professores, professor)
	professor.AdicionarEscola(e)
}

// RemoverProfessor remove um professor da escola
func (e *Escola) RemoverProfessor(professor *Professor) {
	for i, p := range e.Professores {
		if p == professor {
			e.Professores = append(e.Professores[:i], e.Professores[i+1:]...)
			professor.RemoverEscola(e)
			return
		}
	}
}

// ListarProfessores retorna uma lista com os nomes dos professores
func (e *Escola) ListarProfessores() []string {
	nomes := make([]string, len(e.Professores))
	for i, p := range e.Professores {
		nomes[i] = p.Nome
	}
	return nomes
}

// Professor representa um professor
type Professor struct {
	Nome    string
	Escolas []*Escola
}

// AdicionarEscola adiciona uma escola ao professor
func (p *Professor) AdicionarEscola(escola *Escola) {
	for _, e := range p.Escolas {
		if e == escola {
			return
		}
	}
	p.Escolas = append(p.Escolas, escola)
}

// RemoverEscola remove uma escola do professor
func (p *Professor) RemoverEscola(escola *Escola) {
	for i, e := range p.Escolas {
		if e == escola {
			p.Escolas = append(p.Escolas[:i], p.Escolas[i+1:]...)
			return
		}
	}
}

// ListarEscolas retorna uma lista com os nomes das escolas
func (p *Professor) ListarEscolas() []string {
	nomes := make([]string, len(p.Escolas))
	for i, e := range p.Escolas {
		nomes[i] = e.Nome
	}
	return nomes
}

func main() {
	escola1 := &Escola{Nome: "Escola A"}
	escola2 := &Escola{Nome: "Escola B"}

	prof1 := &Professor{Nome: "João"}
	prof2 := &Professor{Nome: "Maria"}

	escola1.AdicionarProfessor(prof1)
	escola1.AdicionarProfessor(prof2)
	escola2.AdicionarProfessor(prof1)

	fmt.Printf("Professores da %s: %v\n", escola1.Nome, escola1.ListarProfessores())
	fmt.Printf("Professores da %s: %v\n", escola2.Nome, escola2.ListarProfessores())
	fmt.Printf("Escolas onde %s leciona: %v\n", prof1.Nome, prof1.ListarEscolas())
	fmt.Printf("Escolas onde %s leciona: %v\n", prof2.Nome, prof2.ListarEscolas())
}

