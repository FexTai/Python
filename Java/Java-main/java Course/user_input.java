import java.util.Scanner;

public class user_input {
    public static void main(String[] args) {
        Scanner eingabe = new Scanner(System.in); //einmalige Erstellung von einem Eingabe Scanner

        System.out.println("whats ur name? ");
        String name = eingabe.nextLine(); //nextLine for String inputs and reading a whole line until the \n

        System.out.println("How old ru? ");
        int age = eingabe.nextInt(); //reading only until it meets an integer leaving the \n in the input

        eingabe.nextLine(); //clearing the input from the \n

        System.out.println("fav food? ");// without clearing it only reads until \n so it doesnt read user input
        String food = eingabe.nextLine();

        System.out.println("your name is " + name + ", you are " + age + "yrs old and you like " + food);

    }
}
