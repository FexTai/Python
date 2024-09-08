import java.util.Random;

public class j8a_for_loop {
    public static void main(String[] args) {
        Random rand = new Random();
        int zahler = 0;

        int wurf_1 = rand.nextInt(6) + 1;
        System.out.println("Zuffalszahl: " + wurf_1);

        for (int wurf = wurf_1; wurf != 6; wurf = rand.nextInt(6) + 1) {
            System.out.println("Zuffalszahl: " + wurf);
            zahler++;
        }

        zahler++; // Für den letzten Wurf der 6

        System.out.println("Anzahl der Würfe bis zur 6: " + zahler);
    }
}