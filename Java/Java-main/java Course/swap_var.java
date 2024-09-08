public class swap_var {
    public static void main(String[] args) {
        String x = "water";
        String y = "kool-aid";
        String temp;

        temp = x;
        x = y;
        y = temp;

        System.out.println("x: " + x + "\ny: " + y);
    }
}
