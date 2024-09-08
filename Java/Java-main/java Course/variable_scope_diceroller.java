import java.util.Random;

public class variable_scope_diceroller {

    Random generator;  //everything outside a method is global to that class
    int number;

    variable_scope_diceroller(){  //everything inside a method is local
        generator = new Random();
            roll();

        }
    void roll() {
        number = generator.nextInt(6) + 1;
        System.out.println(number);
    }

}
