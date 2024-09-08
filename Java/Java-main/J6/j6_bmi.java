import java.util.Scanner;

public class j6_bmi {
    public static void main(String[] args) {
        Scanner eingabe_m = new Scanner(System.in);
        Scanner eingabe_g = new Scanner(System.in);

        System.out.println("Gib dein Gewicht in kg an\nKommazahlen mit \",\" trennen: ");
        double gewicht = eingabe_m.nextDouble();

        System.out.println("Gib deine Größe in Meter an: ");
        double groesse = eingabe_g.nextDouble();

        double bmi = Math.round(gewicht/(groesse*groesse)*10)/10.0;
        String klasse = "";
        if(bmi < 18.5) {
            klasse = "untergewichtig";
        }
        else if(bmi > 18.5 && bmi <= 24.9) {
            klasse = "normalgewichtig";
        }
        else if(bmi > 24.9 && bmi <= 29) {
            klasse = "übergewichtig";
        }
        else if(bmi > 29.9 && bmi <= 34.9) {
            klasse = "fettleibig";
        }
        else if(bmi > 34.9){
            klasse = "stark übergewichtig";
        }

        System.out.println("Dein bmi ist " + bmi + " und du bist " + klasse);
    }
}
