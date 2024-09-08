import java.util.Scanner;

public class j4a {
	public static void main(String[] args){
		Scanner jahre = new Scanner(System.in);
        double guthaben = 2000;
		double zinssatz = 1.03;
		System.out.print("Wie lange dauert die Verzinsung(in Jahren)?: ");
		int n = jahre.nextInt();
		
		for(int i = 1; i <= n; i++) {
            guthaben = guthaben * zinssatz;
            System.out.println("Nach " + i + " Jahren " + " erreichst du den Betrag: " + guthaben + " euro ");
		}
	}
}