import java.util.Scanner;
public class J4A {
    public static void main(String[] args) {
        //Initialisierungen
        Scanner scanner = new Scanner(System.in);
        int anz;

        //Array definieren
        System.out.println("Wie viele Namen willst du eingeben?: ");
        anz = scanner.nextInt();
        scanner.nextLine();
        String[] namen = new String[anz];

        //Eingabeschleife für arrays
        for(int i = 0; i<anz; i++){
            System.out.println("gib den " + (i+1) + ". Namen ein: ");
            namen[i] = scanner.nextLine();
        }

        //Ausgabe dopplungen
        for(int i = 0; i<anz; i++){
            for(int j = 0; j<anz; j++){
                if(namen[i].equals(namen[j])){
                    namen[j] = " ";
                }
            }
        }
    }
}
