//# Faça um programa em Python que receba 6 numeros inteiros e mostre: ´
//#  • Os numeros pares digitados; 
//#  • A soma dos numeros pares digitados; 
//#  • Os numeros   ımpares digitados;
//#  • A quantidade de numeros  ımpares 

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] numbers = new int[6];
        int sumEven = 0;
        int countOdd = 0;

        System.out.println("Digite 6 números inteiros:");

        // Receber os números do usuário
        for (int i = 0; i < 6; i++) {
            numbers[i] = scanner.nextInt();
        }

        System.out.print("Números pares digitados: ");
        for (int num : numbers) {
            if (num % 2 == 0) {
                System.out.print(num + " ");
                sumEven += num;
            }
        }
        System.out.println();

        System.out.println("Soma dos números pares: " + sumEven);

        System.out.print("Números ímpares digitados: ");
        for (int num : numbers) {
            if (num % 2 != 0) {
                System.out.print(num + " ");
                countOdd++;
            }
        }
        System.out.println();

        System.out.println("Quantidade de números ímpares: " + countOdd);
    }
}

