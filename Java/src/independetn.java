public class independetn {
    public static void main(String[] args) {
        byte x = 1;
        byte y = x;  // primitive types copies a value not references
        x = 2;
        System.out.println(y);
    }
}
