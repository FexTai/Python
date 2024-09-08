import java.util.Scanner;
import java.util.Random;

public class j7 {
    public static void main(String[] args) {
        Scanner eingabe = new Scanner(System.in);

        System.out.println("gib die Anzahl der Zufallszahlen an: ");
        int n = eingabe.nextInt();
        double summe = 0;

        for(int i = 1; i <= n; i++) {
            Random generator = new Random();
            int zuf = generator.nextInt(6) + 1;
            summe += zuf;
            System.out.println("Zufallszahl: " + zuf);
        }
        System.out.println("Summe: " + summe + ", Durchschnitt: " + Math.round(summe/n));
    }

}
