import java.util.Scanner;
public class bmi {
    public static void main(String[] args) {
        Scanner eingabe = new Scanner(System.in);
        System.out.println("Kommazahlen mit \",\" trennen!");
        System.out.println("Gib für den Namen \"q\" oder \"Q\" ein, um das Programm zu beenden\n");

        while(true) {
            System.out.println("Gib deinen Namen an: ");
            String name = eingabe.next();

            if (name.equalsIgnoreCase("q")) {
                System.out.println("Programm wird beendet!");
                break;
            }

            System.out.println("Gib deine Größe in Meter an: ");
            double groesse = eingabe.nextDouble();

            System.out.println("Gib dein Gewicht in kg an: ");
            double gewicht = eingabe.nextDouble();

            person nutzer1 = new person(name, groesse, gewicht);
            System.out.println("\n" + nutzer1.Name + ": " + nutzer1.Height + "m " + nutzer1.Weight + "kg\nerrechnetes Bmi: " +
                    nutzer1.Bmi + ", " + nutzer1.klasse + "\n");
        }

    }
}
