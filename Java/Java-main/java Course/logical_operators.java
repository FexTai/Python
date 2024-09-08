import java.util.Scanner;

public class logical_operators {
    public static void main(String[] args) {
        // logical operators used to connect two or more expressions


        // && = (AND) both conditions must be true
        int temp = 22;
        if(temp > 30) {
            System.out.println("it is hot outside");
        }
        else if (temp >= 20 && temp <= 30) {
            System.out.println("It is warm outside");
        }
        else {
            System.out.println("It is cold outside");
        }


        // || = (OR) either condition must be true
        Scanner generator = new Scanner(System.in);
        System.out.println("Press q or Q to quit");
        String response = generator.next();

        if(response.equals("Q") || response.equals("q")) {  //To check strings for value use the .equals operator instead of ==
            System.out.println("you quit the game");
        }
        else {
            System.out.println("you are still playing");
        }


        // ! = (NOT) reverse boolean value of condition
        if(!response.equals("Q") && !response.equals("q")) {  // not equals q and not equals Q
            System.out.println("you are still playing");
        }
        else {
            System.out.println("you quit the game");
        }
    }
}
