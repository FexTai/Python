import java.util.Scanner;

public class nested_loops {
    public static void main(String[] args) {
        // nested loops = a loop inside a loop

        Scanner generator = new Scanner(System.in);
        int rows;
        int columns;
        String symbol;

        System.out.println("Enter the amount of rows: ");
        rows = generator.nextInt();

        System.out.println("Enter the amount of columns: ");
        columns = generator.nextInt();

        System.out.println("Which character to use for fill? ");
        symbol = generator.next();

        for (int i = 1; i <= rows; i++) { //Outer loop finishes after the inner loop
            System.out.println();
            for (int j = 1; j <= columns; j++){ //Inner loop finishes only after full incrimentation
                System.out.print(symbol);
            }
        }
    }
}
