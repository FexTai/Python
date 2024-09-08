import java.awt.*;

public class test {
    public static void main(String[] args) {
        Point point1 = new Point(1,2);
        Point point2 = point1;
        point1.x = 3;  // reference types copied by references
        System.out.println(point2);

        String message = "Hallo Welt!"; //Strings are reference types but can be shortened to declare like a primitve type
        System.out.println(message + "!!");
        System.out.println(message.replace("Hallo", "Was geht"));
    }
}
