import java.util.ArrayList;

public class manager {

    //Löschfunktion (Wort)
    static String loeschen(String wort, ArrayList<String> liste) {
        for (String i : liste) {
            if (i.equals(wort)) {
                liste.remove(wort);
                return liste.toString();
            }
        }
        System.out.println("Aufgabe nicht gefunden! ");
        return liste.toString();
    }

    //Löschfunktion (Zahl)
    static String loeschen(int zahl, ArrayList<String> liste) {
        for (String i : liste) {
            if (i.equals(wort)) {
                liste.remove(wort);
                return liste.toString();
            }
        }
        System.out.println("Aufgabe nicht gefunden! ");
        return liste.toString();
    }

    //Hinzufügen Funktion
    static String hinzufuegen(String wort, ArrayList<String> liste) {
        String counter = String.valueOf(liste.size() + 1);
        for (String i : liste) {
            if (i.equals(wort)) {
                System.out.println("Diese Aufgabe existiert bereits!");
                return liste.toString();
            }
        }
        liste.add(counter + ". " + wort + "\n");
        return liste.toString().substring(1, liste.toString().length() -1).replace(", ", "");
    }

    //leeren Funktion
    static String leeren(ArrayList<String> liste){
        if(liste.toString().equals("[]")){
            System.out.println("Die liste ist bereits Leer!");
            return liste.toString();
        }
        liste.clear();
        return liste.toString();

    }
}