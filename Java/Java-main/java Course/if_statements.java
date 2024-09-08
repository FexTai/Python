public class if_statements {
    public static void main(String[] args) {
        int age = 80;

        if (age >= 75){                     //wenn diese bedingung erfuellt ist, werden alle anderen ignoriert
            System.out.println("Too old!");
        }
        else if(age >= 18) {
            System.out.println("you are an adult!");
        }
        else{
            System.out.println("you are not an adult!");
        }
    }
}
