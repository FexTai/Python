import java.util.Random;
import java.util.Scanner;

public class j9 {
	public static void main(String[] args) {
		Random gen = new Random();
		Scanner eingabe = new Scanner(System.in);
		int zahl;
		int versuche = 0;	
		zahl = gen.nextInt(100) +1;	
		int antwort = 0;
		
		while(antwort != zahl){
			versuche ++;
			System.out.println("Rate eine Zahl zwischen 1 und 100");
			antwort = eingabe.nextInt();
			if(antwort > zahl){
				System.out.println("niedriger");		
			}
			if(antwort < zahl){
				System.out.println("höher");
			}
		}
	System.out.println("\nDu hast die Zahl erraten!\nDu hast " + versuche + " Versuche gebraucht");
	}
}
