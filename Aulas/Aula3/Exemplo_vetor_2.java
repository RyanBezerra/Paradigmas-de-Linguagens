
//  Exemplo de Vetor 2 em Java - calculando a média dos elementos do vetor
//  Mais a o maior elemento do vetor e o menor elemento do vetor.


public class Main {
    public static void main(String[] args) {
        // Cria um vetor de 10 elementos inteiros
        int[] vetor = {5, 12, 7, 20, 15, 8, 3, 11, 6, 9};

        // Calcula a média, o maior valor e o menor valor
        int soma = 0;
        int maiorValor = vetor[0];
        int menorValor = vetor[0];

        for (int i = 0; i < vetor.length; i++) {
            soma += vetor[i];
            if (vetor[i] > maiorValor) {
                maiorValor = vetor[i];
            }
            if (vetor[i] < menorValor) {
                menorValor = vetor[i];
            }
        }

        double media = (double) soma / vetor.length;

        // Exibe os resultados
        System.out.println("Média: " + media);
        System.out.println("Maior valor: " + maiorValor);
        System.out.println("Menor valor: " + menorValor);
    }
}
