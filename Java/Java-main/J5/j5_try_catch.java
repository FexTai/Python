import java.util.Scanner;

public class j5_try_catch {

    public static void main(String[] args) {
        Scanner eingabe = new Scanner(System.in);
        Scanner einh = new Scanner(System.in);
        double laenge_m;
        int umrechnungsArt;
        // \n für einen Zeilenumbruch
        System.out.println("\n Gib für die Länge 0 ein, um das Programm zu beenden! \n");
        do {
            try {
                System.out.println("Gib die Länge an (in m): ");
                laenge_m = eingabe.nextDouble();
                if (laenge_m == 0) {    //Vermeiden unnötiger Berechnungen
                    System.exit(0);
                }
                System.out.println("\nUmrechnungart?: ");
                System.out.println("1: mm, 2: cm, 3: dm, 4: km, 5: Meilen, 6: Zoll, 7: Fuß");
                umrechnungsArt = einh.nextInt();
            }
            catch (Exception b) {
                System.out.println("\n Ungültige Eingabe! \n");
                eingabe.nextLine();    //Falsche Eingabe entfernen, um eine Endlosschleife zu vermeiden
                einh.nextLine();
                continue;              //Neustart der Schleife
            }

            //Fortsetzung der Berechnungen
            switch(umrechnungsArt) {
                case 1:
                    System.out.println(laenge_m + " m = " + laenge_m * 1000 + " mm\n");
                    break;
                case 2:
                    System.out.println(laenge_m + " m = " + laenge_m * 100 + " cm\n");
                    break;
                case 3:
                    System.out.println(laenge_m + " m = " + laenge_m * 10 + " dm\n");
                    break;
                case 4:
                    System.out.println(laenge_m + " m = " + laenge_m / 1000 + " km\n");
                    break;
                case 5:
                    System.out.println(laenge_m + " m = " + laenge_m / 1609 + " mi\n");
                    break;
                case 6:
                    System.out.println(laenge_m + " m = " + laenge_m / 39.37 + " Zoll\n");
                    break;
                case 7:
                    System.out.println(laenge_m + " m = " + laenge_m * 3.281 + " ft\n");
                    break;
                default:
                    System.out.println("falsche Eingabe\n");
            }
        } while(true); //Unendliche Schleife bis Eingabe = 0 ist
    }

}