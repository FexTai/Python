public class escdq {
    public static void main(String[] args) {
        String message = "Hallo \"Max\""; //escaping quotes with backslash
        String path = "c:\\Windows\\..."; //escaping backslash with a backslash
        String newline = "Hallo \n Welt!";
        System.out.println(message);
        System.out.println(path);
        System.out.println(newline);
    }
}
