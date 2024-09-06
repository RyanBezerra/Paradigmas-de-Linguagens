public class Retangulo {
    private double comprimento;
    private double largura;

    // Construtor
    public Retangulo(double comprimento, double largura) {
        this.comprimento = comprimento;
        this.largura = largura;
    }

    // Método para calcular a área
    public double calcularArea() {
        return comprimento * largura;
    }

    // Método para calcular o perímetro
    public double calcularPerimetro() {
        return 2 * (comprimento + largura);
    }

    public static void main(String[] args) {
        // Criando uma instância da classe Retangulo
        Retangulo ret = new Retangulo(200, 300);
        System.out.println("Área: " + ret.calcularArea());
        System.out.println("Perímetro: " + ret.calcularPerimetro());
    }
}

