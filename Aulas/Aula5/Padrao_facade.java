// Subsistema para fazer café
class Cafeteira {
    public void moerGraos() {
        System.out.println("Moendo grãos de café");
    }

    public void fazerCafe() {
        System.out.println("Fazendo café");
    }
}

// Subsistema para fazer chá
class Chaleira {
    public void ferverAgua() {
        System.out.println("Fervendo água");
    }

    public void fazerCha() {
        System.out.println("Fazendo chá");
    }
}

// Fachada
class BebidasFacade {
    private Cafeteira cafeteira;
    private Chaleira chaleira;

    public BebidasFacade() {
        this.cafeteira = new Cafeteira();
        this.chaleira = new Chaleira();
    }

    public void prepararCafe() {
        System.out.println("\nPreparando café...");
        cafeteira.moerGraos();
        cafeteira.fazerCafe();
    }

    public void prepararCha() {
        System.out.println("\nPreparando chá...");
        chaleira.ferverAgua();
        chaleira.fazerCha();
    }
}

// Cliente
public class Padrao_facade {
    public static void main(String[] args) {
        BebidasFacade facade = new BebidasFacade();
        facade.prepararCafe();
        facade.prepararCha();
    }
}

