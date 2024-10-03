package Lista de Exercícios.Java;

public class Configuracao {
    private static Configuracao instancia;
    private String tema;
    private String idioma;

    private Configuracao() {
        inicializar();
    }

    public static Configuracao getInstance() {
        if (instancia == null) {
            instancia = new Configuracao();
        }
        return instancia;
    }

    private void inicializar() {
        this.tema = "claro";
        this.idioma = "português";
    }

    public void setTema(String tema) {
        this.tema = tema;
    }

    public void setIdioma(String idioma) {
        this.idioma = idioma;
    }

    public String getConfiguracoes() {
        return String.format("Tema: %s, Idioma: %s", tema, idioma);
    }

    public static void main(String[] args) {
        Configuracao config1 = Configuracao.getInstance();
        config1.setTema("escuro");

        Configuracao config2 = Configuracao.getInstance();
        config2.setIdioma("inglês");

        System.out.println(config1.getConfiguracoes());
        System.out.println(config2.getConfiguracoes());
        System.out.println(config1 == config2);
    }
}
