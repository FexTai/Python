import java.util.Scanner;

public class temperatur {
	public static void main(String[] args){
		Scanner eingabe = new Scanner(System.in);
		
		Double tp;
        int umr;
		
		System.out.print("Temperatur?: ");
		tp = eingabe.nextDouble();
		System.out.print("Umrechnung? (1: Celsius ->Fahrenheit, 2: Fahrenheit ->Celsius): ");
		umr = eingabe.nextInt();
		
		if (umr == 1) {
			System.out.println(tp*1.8 + 32 + "°");
			}
		else {
			System.out.println((tp - 32) * 5/9 + "F");
			}	
		
		}
		
	}
