import java.util.InputMismatchException;
import java.util.Scanner;

public class exception_handling {
    public static void main(String[] args) {

        // exception = an event that occurs during the execution of a program, that
        // disrupts the normal flow of instructions

        try (Scanner scanner = new Scanner(System.in)) { // the files/scanners in the () will be automatically closed after finishing the block
            System.out.println("Enter a whole number to divide: ");
            int x = scanner.nextInt();

            System.out.println("Enter a whole number to divide by: ");
            int y = scanner.nextInt();

            int z = x / y;

            System.out.println("Result: " + z);
        } catch (
                ArithmeticException ex) {  //in a catch statement you have 2 args The type of exception and the variable to store
            System.out.println("You can´t divide by zero...");
        } catch (InputMismatchException inp) {
            System.out.println("Please enter a number!");
        } catch (Exception ext) {
            System.out.println("Something went wrong...");
        } finally {
            System.out.println("This will always print");
            // good practice to close any open scanners or files to clean up
        }

    }
}
