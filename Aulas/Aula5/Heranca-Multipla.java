// Interface Animal
abstract class Animal {
    protected String nome;

    public Animal(String nome) {
        this.nome = nome;
    }

    abstract void emitirSom();
}

// Classe Mamifero que estende Animal
class Mamifero extends Animal {
    public Mamifero(String nome) {
        super(nome);
    }

    public void amamentar() {
        System.out.println(nome + " está amamentando.");
    }

    @Override
    void emitirSom() {
        // Método abstrato pode ser implementado nas subclasses
    }
}

// Interface Ave com o comportamento de voar
interface Ave {
    void voar();
}

// Classe Morcego que estende Mamifero e implementa a interface Ave
class Morcego extends Mamifero implements Ave {
    public Morcego(String nome) {
        super(nome);
    }

    @Override
    public void emitirSom() {
        System.out.println("Morcego fazendo ruídos noturnos.");
    }

    @Override
    public void voar() {
        System.out.println(nome + " está voando.");
    }

    public static void main(String[] args) {
        Morcego morcego = new Morcego("Batemane");
        morcego.emitirSom();    // Método da classe Morcego
        morcego.amamentar();    // Método da classe Mamifero
        morcego.voar();         // Método da interface Ave
    }
}
