package Lista de Exercícios.Java;

import java.util.Objects;

// Questão 10, 11, 12 e 13
class Calculadora {
    public int somarDois(int a, int b) {
        return a + b;
    }
    
    public int somarTres(int a, int b, int c) {
        return a + b + c;
    }
}

abstract class Funcionario {
    protected String nome;

    public Funcionario(String nome) {
        this.nome = nome;
    }

    public abstract double calcularSalario();
}

class FuncionarioHorista extends Funcionario {
    private int horasTrabalhadas;
    private double valorHora;

    public FuncionarioHorista(String nome, int horasTrabalhadas, double valorHora) {
        super(nome);
        this.horasTrabalhadas = horasTrabalhadas;
        this.valorHora = valorHora;
    }

    @Override
    public double calcularSalario() {
        return horasTrabalhadas * valorHora;
    }
}

class FuncionarioAssalariado extends Funcionario {
    private double salarioMensal;

    public FuncionarioAssalariado(String nome, double salarioMensal) {
        super(nome);
        this.salarioMensal = salarioMensal;
    }

    @Override
    public double calcularSalario() {
        return salarioMensal;
    }
}

class Produto {
    private String nome;
    private double preco;

    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    public Produto somar(Produto outro) {
        if (outro == null) {
            throw new IllegalArgumentException("Produto não pode ser nulo");
        }
        String novoNome = this.nome + " + " + outro.nome;
        double novoPreco = this.preco + outro.preco;
        return new Produto(novoNome, novoPreco);
    }

    @Override
    public String toString() {
        return String.format("%s: R$%.2f", nome, preco);
    }
}

class Matematica {
    public static long fatorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("O fatorial não está definido para números negativos");
        }
        if (n == 0 || n == 1) {
            return 1;
        }
        return n * fatorial(n - 1);
    }
}

public class Calculadora {
    public static void main(String[] args) {
        Calculadora calc = new Calculadora();
        System.out.println(calc.somarDois(5, 3));
        System.out.println(calc.somarTres(5, 3, 2));

        FuncionarioHorista horista = new FuncionarioHorista("João", 160, 20);
        FuncionarioAssalariado assalariado = new FuncionarioAssalariado("Maria", 3000);

        System.out.printf("Salário de %s: R$%.2f%n", horista.nome, horista.calcularSalario());
        System.out.printf("Salário de %s: R$%.2f%n", assalariado.nome, assalariado.calcularSalario());

        Produto produto1 = new Produto("Camiseta", 50.0);
        Produto produto2 = new Produto("Calça", 100.0);
        Produto produtoSoma = produto1.somar(produto2);

        System.out.println("Produto 1: " + produto1);
        System.out.println("Produto 2: " + produto2);
        System.out.println("Soma dos produtos: " + produtoSoma);

        System.out.println("Fatorial de 5: " + Matematica.fatorial(5));
        System.out.println("Fatorial de 0: " + Matematica.fatorial(0));
    }
}
