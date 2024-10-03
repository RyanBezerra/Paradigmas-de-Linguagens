import java.ArrayList;

// Classe Endereco
class Endereco {
    private String rua;
    private String cidade;
    private String estado;
    private String cep;

    public Endereco(String rua, String cidade, String estado, String cep) {
        this.rua = rua;
        this.cidade = cidade;
        this.estado = estado;
        this.cep = cep;
    }

    public void mostrarEndereco() {
        System.out.println("Rua: " + rua + ", Cidade: " + cidade + ", Estado: " + estado + ", CEP: " + cep);
    }
}

// Classe Pessoa
class Pessoa {
    private String nome;
    private int idade;
    private Endereco endereco;

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
        this.endereco = null;  // Inicialmente sem endereço
    }

    public void adicionarEndereco(Endereco endereco) {
        this.endereco = endereco;
    }

    public void mostrarInformacoes() {
        System.out.println("Nome: " + nome + ", Idade: " + idade);
        if (endereco != null) {
            System.out.println("Endereço:");
            endereco.mostrarEndereco();
        } else {
            System.out.println("Endereço não disponível");
        }
    }

    public String getNome() {
        return nome;
    }
}

// Classe Empresa
class Empresa {
    private String nome;
    private String cnpj;
    private List<Pessoa> funcionarios;

    public Empresa(String nome, String cnpj) {
        this.nome = nome;
        this.cnpj = cnpj;
        this.funcionarios = new ArrayList<>();
    }

    public void contratarFuncionario(Pessoa funcionario) {
        funcionarios.add(funcionario);
    }

    public void listarFuncionarios() {
        System.out.println("Funcionários da empresa " + nome + ":");
        for (Pessoa funcionario : funcionarios) {
            System.out.println(funcionario.getNome());
        }
    }
}

// Cliente
public class Agregacao_exemplo {
    public static void main(String[] args) {
        Endereco endereco1 = new Endereco("Av. Principal", "Cidade A", "Estado X", "12345-678");
        Pessoa pessoa1 = new Pessoa("João", 30);
        pessoa1.adicionarEndereco(endereco1);

        Endereco endereco2 = new Endereco("Rua Secundária", "Cidade B", "Estado Y", "98765-432");
        Pessoa pessoa2 = new Pessoa("Maria", 25);
        pessoa2.adicionarEndereco(endereco2);

        Empresa empresa = new Empresa("Empresa ABC", "12345678901234");
        empresa.contratarFuncionario(pessoa1);
        empresa.contratarFuncionario(pessoa2);

        empresa.listarFuncionarios();
    }
}
