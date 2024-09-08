import java.util.Scanner;

public class math_class {
    public static void main(String[] args) {

        double x = 3.14;
        double y = -10;

        double z = Math.max(x, y);
        double a = Math.min(x, y);

        // Math.floor is round down, Math.ceil is round up, Math.round is mathematical rounding

        double wurzel = Math.sqrt(x); //Wurzel

        double k1, k2, hy;

        Scanner eingabe = new Scanner(System.in);

        System.out.println("Gib die erste Kathete an: ");
        k1 = eingabe.nextDouble();

        System.out.println("Gib die zweite Kathete an: ");
        k2 = eingabe.nextDouble();

        hy = Math.sqrt(k1*k1 + k2*k2);
        System.out.println("Die hypothenuse ist: " + hy);

        eingabe.close();
    }
}
