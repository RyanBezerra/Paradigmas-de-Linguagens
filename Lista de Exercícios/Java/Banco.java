package Lista de Exercícios.Java;

// Questão 3 e 15
class ContaBancaria {
    private String titular;
    private double saldo;

    public ContaBancaria(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    public String getTitular() {
        return titular;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double valor) {
        throw new IllegalArgumentException("Não é possível modificar o saldo diretamente. Use os métodos depositar() ou sacar().");
    }

    public boolean depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
            return true;
        }
        return false;
    }

    public boolean sacar(double valor) throws SaldoInsuficienteException {
        if (valor > 0) {
            if (saldo >= valor) {
                saldo -= valor;
                return true;
            } else {
                throw new SaldoInsuficienteException(saldo, valor);
            }
        }
        return false;
    }
}

class SaldoInsuficienteException extends Exception {
    public SaldoInsuficienteException(double saldoAtual, double valorSaque) {
        super(String.format("Saldo insuficiente. Saldo atual: R$%.2f, Valor do saque: R$%.2f", saldoAtual, valorSaque));
    }
}

public class Banco {
    public static void main(String[] args) {
        ContaBancaria contaMaria = new ContaBancaria("Maria", 1000);

        System.out.printf("Titular: %s%n", contaMaria.getTitular());
        System.out.printf("Saldo inicial: R$%.2f%n", contaMaria.getSaldo());

        if (contaMaria.depositar(500)) {
            System.out.printf("Depósito realizado. Novo saldo: R$%.2f%n", contaMaria.getSaldo());
        } else {
            System.out.println("Falha no depósito.");
        }

        try {
            if (contaMaria.sacar(200)) {
                System.out.printf("Saque realizado. Novo saldo: R$%.2f%n", contaMaria.getSaldo());
            }
        } catch (SaldoInsuficienteException e) {
            System.out.printf("Falha no saque: %s%n", e.getMessage());
        }

        try {
            contaMaria.sacar(2000);
        } catch (SaldoInsuficienteException e) {
            System.out.printf("Falha no saque: %s%n", e.getMessage());
        }

        try {
            contaMaria.setSaldo(5000);
        } catch (IllegalArgumentException e) {
            System.out.printf("Erro ao tentar modificar o saldo: %s%n", e.getMessage());
        }
    }
}
