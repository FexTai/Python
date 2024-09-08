import java.util.Scanner;
import java.util.ArrayList;

public class toDo {
    public static void main(String[] args) {
        // Initialisierungen
        Scanner scanner = new Scanner(System.in);
        int auswahl = 0; String td;

        // Hauptliste
        ArrayList<String> toDo = new ArrayList<>();

        // Schleife
        do {
            // Abfrage
            System.out.println("\nHinzufügen(1), Löschen(2), Liste leeren(3), beenden(4)");
            try {
                auswahl = scanner.nextInt();
                scanner.nextLine();  // Leerzeile nach nextInt() einlesen1

                // Verarbeitung
                switch (auswahl) {
                    case 1:
                        System.out.println("\nWas soll hinzugefügt werden?");
                        td = scanner.nextLine();
                        System.out.println(manager.hinzufuegen(td, toDo));
                        break;
                    case 2:
                        System.out.println("\nWas soll gelöscht werden?");
                        td = scanner.nextLine();
                        System.out.println(manager.loeschen(td, toDo));
                        break;
                    case 3:
                        System.out.println("\nLeeren...");
                        System.out.println(manager.leeren(toDo));
                        break;
                    case 4:
                        System.out.println("\nBeenden...");
                        break;
                    default:
                        System.out.println("\nFehler! Versuche es erneut");
                }
            } catch (Exception a){
                System.out.println("gib bitte eine ganze Zahl ein!");
                scanner.nextLine(); //Falsche eingabe entfernen
            }
        } while (auswahl != 4); // Schleife beenden, wenn 3 ausgewählt wird

        scanner.close();  // Scanner schließen
    }

}
