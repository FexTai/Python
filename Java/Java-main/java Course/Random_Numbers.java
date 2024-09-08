import java.util.Random;

public class Random_Numbers {
    public static void main(String[] args) {

        Random generator = new Random(); //not really random numbers, pseudo random
        int x = generator.nextInt(6) + 1; // counting from 0 to 5 + 1 makes it from 1 to 6
        double y = generator.nextDouble();
        boolean z = generator.nextBoolean();

        System.out.println(x);
        System.out.println(y);
        System.out.println(z);

    }
}
