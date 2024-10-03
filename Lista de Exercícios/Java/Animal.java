package Lista_de_Exercícios.Java;

// Questão 4 e 5
public class Animal {
    private String nome;
    private int idade;

    // Construtor padrão
    public Animal() {}

    public Animal(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public void emitirSom() {
        System.out.println("O animal emite um som.");
    }

    // Getters e setters
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }
}

class Cachorro extends Animal {
    public Cachorro() {
        super();
    }

    @Override
    public void emitirSom() {
        System.out.println("O cachorro late: Au au!");
    }
}

class Gato extends Animal {
    public Gato() {
        super();
    }

    @Override
    public void emitirSom() {
        System.out.println("O gato mia: Miau!");
    }
}

class Vaca extends Animal {
    public Vaca() {
        super();
    }

    @Override
    public void emitirSom() {
        System.out.println("A vaca muge: Muuu!");
    }
}

public class Animal {
    public static void fazerBarulho(Animal[] animais) {
        for (Animal animal : animais) {
            System.out.println("O " + animal.tipo() + " faz: " + animal.som());
        }
    }

    public static void main(String[] args) {
        Animal cachorro = new Cachorro();
        Animal gato = new Gato();
        Animal vaca = new Vaca();

        Animal[] animais = {cachorro, gato, vaca};

        fazerBarulho(animais);
    }
}
