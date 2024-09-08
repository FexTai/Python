import java.util.Scanner;

public class j4c {
    public static void main(String[] args){
        Scanner guthab = new Scanner(System.in);
        Scanner zinstz = new Scanner(System.in);

        System.out.print("Gebe dein Startguhaben an: ");
        double guthaben = guthab.nextDouble();

        double zielguthaben = 2*guthaben;

        System.out.print("gebe den zinssatz in % an: ");
        double zinssatz = (zinstz.nextDouble()) / 100 + 1;

        int i = 1;
        while(guthaben < zielguthaben){
            i++;
            guthaben = guthaben * zinssatz;
            System.out.println("Nach " + i + " Jahren " + " erreichst du den Betrag: " + guthaben + " euro ");
        }
    }
}