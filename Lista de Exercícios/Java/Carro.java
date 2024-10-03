package Lista de Exercícios.Java;

// Questão 1, 2 e 6
class Motor {
    private String tipo;
    private int potencia;

    public Motor(String tipo, int potencia) {
        this.tipo = tipo;
        this.potencia = potencia;
    }

    @Override
    public String toString() {
        return tipo + " - " + potencia + " cv";
    }
}

public class Carro {
    private String marca;
    private String modelo;
    private int ano;
    private int velocidade;
    private Motor motor;

    public Carro(String marca, String modelo, int ano, String tipoMotor, int potenciaMotor) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.velocidade = 0;
        this.motor = new Motor(tipoMotor, potenciaMotor);
    }

    public void motor(String tipoMotor) {
        System.out.println("🔧 Motor do " + modelo + ": " + tipoMotor);
    }

    public void bateria(int capacidadeBateria) {
        System.out.println("🔋 Bateria do " + modelo + ": " + capacidadeBateria + " kWh");
    }

    public void pneus(String tipoPneu) {
        System.out.println("🛞 Pneus do " + modelo + ": " + tipoPneu);
    }

    public void sobre() {
        System.out.println("🚗 " + marca + " " + modelo + " (" + ano + ")");
        System.out.println("🔧 Motor: " + motor);
    }

    public void acelerar(int incremento) {
        velocidade += incremento;
        System.out.println("🚀 " + modelo + " acelerou para " + velocidade + " km/h");
    }

    public void frear(int decremento) {
        velocidade = Math.max(0, velocidade - decremento);
        System.out.println("🛑 " + modelo + " freou para " + velocidade + " km/h");
    }

    public void exibirVelocidade() {
        System.out.println("🏁 Velocidade do " + modelo + ": " + velocidade + " km/h");
    }

    private static void imprimirSeparador() {
        System.out.println("========================================");
    }

    public static void main(String[] args) {
        Carro carro1 = new Carro("Toyota", "Corolla", 2020, "V6", 200);
        Carro carro2 = new Carro("Honda", "Civic", 2018, "V4", 180);
        Carro carro3 = new Carro("Ford", "Mustang", 2022, "V8", 450);

        Carro[] carros = {carro1, carro2, carro3};

        for (Carro carro : carros) {
            imprimirSeparador();
            carro.sobre();
            carro.bateria(carro.marca.equals("Toyota") ? 12 : carro.marca.equals("Honda") ? 14 : 15);
            carro.pneus(carro.marca.equals("Toyota") ? "Radiais" : carro.marca.equals("Honda") ? "Esportivos" : "Off-road");
        }

        imprimirSeparador();
        System.out.println("\n📊 Teste de aceleração e frenagem (Toyota Corolla):");
        imprimirSeparador();

        carro1.acelerar(50);
        carro1.exibirVelocidade();
        carro1.acelerar(30);
        carro1.exibirVelocidade();
        carro1.frear(20);
        carro1.exibirVelocidade();
        carro1.frear(100);
        carro1.exibirVelocidade();

        imprimirSeparador();
    }
}
