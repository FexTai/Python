public class methods_return_types {
    public static void main(String[] args) {

        int x = 9;
        int y = -3;

        int z = sum(x,y); //local varible for main method
        System.out.println(z);

        //another way
        System.out.println(sum(x,y));

    }
    static int sum(int z1, int z2){ //creating a return method requires a return statement

        int z = z1 + z2; //local variable for sum method
        return z;
    }
}
