import java.util.Random;
import java.util.Scanner;

public class j10{
	public static void main(String[] args){
		Scanner eingabe = new Scanner(System.in);
		Random gen = new Random();
		int pasch = 0;
		int kpasch = 0;
		int runde = 0;
		String dg;
		
		System.out.println("Anzahl der Durchgänge?: ");		
		int durchgange = eingabe.nextInt();
		
		for(int i = 0; i != durchgange; i++){
			runde++;
			System.out.println(runde + ".Durchgang\n");
			int zahl1 = gen.nextInt(6) + 1;
			System.out.println("Wurf1: " + zahl1);
			int zahl2 = gen.nextInt(6) + 1;
			System.out.println("Wurf2: " + zahl2);
			
			if(zahl1 == zahl2){
				pasch++;
				System.out.println("Pasch!\n\n");
			}
			else{
				kpasch++;
				System.out.println("Kein Pasch!\n\n");
			}
		}
		if(durchgange == 1) {
			dg = "Durchgang";
		}
		else{
			dg = "Durchgängen";
		}

		System.out.println("In den " + durchgange + " " + dg + " hast du " + pasch + " mal Pasch gehabt und " + kpasch + " mal kein Pasch");
	}
}