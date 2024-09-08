import java.util.Scanner;

public class while_loops {
    public static void main(String[] args) {
        Scanner generator = new Scanner(System.in);
        String name = "";


        //while loop evlt kein Durchlauf, da die Bedingung zu Beginn geprüft wird
        while(name.isBlank()){
            System.out.println("Enter your name");
            name = generator.nextLine();
        }
        System.out.println("Hello " + name);


        //do while loop mindestens 1 Durchlauf, da die Bedingung am Ende geprüft wird
        do {
            System.out.println("Enter your name");
            name = generator.nextLine();
        }while(name.isBlank());
        System.out.println("Hello " + name);
    }
}
