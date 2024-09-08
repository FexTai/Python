import java.util.Random;

public class j8a {
    public static void main(String[] args) {
        int i = 0;
        int zuf;

        do {
            i++;
            Random generator = new Random();
            zuf = generator.nextInt(6) + 1;
            System.out.println("Zuffalszahl: " + zuf);
        }while(zuf != 6); //Mindestens 1 Durchgang nötig, daher do... while

        System.out.println("Anzahl der Würfe : " + i);
    }
}
