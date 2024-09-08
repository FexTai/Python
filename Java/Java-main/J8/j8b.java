import java.util.Scanner;
import java.util.Random;

public class j8b {
	public static void main(String[] args) {
		Random gen = new Random();
		int runde = 0;
		int zaehler = 1;
		int summe = 0;
		
		Scanner eingabe = new Scanner(System.in);
		System.out.println("Gib die Anzahl der Durchgänge an: ");
		int durchgaenge = eingabe.nextInt();
		
		for(int i = 0; i != durchgaenge; i++) {
			runde ++;
			System.out.println("\nRunde: " + runde + "\n");
			
			int zahl = gen.nextInt(6) + 1;
			System.out.println("Zahl: " + zahl);
			while(zahl != 6){
				zahl = gen.nextInt(6) + 1;
				System.out.println("Zahl: " + zahl);
				zaehler ++;
			}
			summe += zaehler;
			System.out.println("Würfe bis zur 6 in Runde " + runde + ": " + zaehler);
			zaehler = 1;
		}
		
		System.out.println("\nDurchschnittle Würfe pro Runde: " + summe/durchgaenge);
	}
}