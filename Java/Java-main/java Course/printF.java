public class printF {
    public static void main(String[] args) {
        // printf() = an optional method to control, format and display text to the console window
        //            requires 2 arguments = format string + (object/variable/value)
        //            % [flags] [precision] [width] [conversion-character]


        boolean a = true;
        char mychar = 'a';
        String myString = "FexTy";
        int myInt = 4;
        double myDouble = 1000;

        System.out.printf("the statement is %b\n", a); //%b for boolean
        System.out.printf("%c\n", mychar); //%c for char
        System.out.printf("%s\n", myString); //%s for String
        System.out.printf("%d\n", myInt); // %d for integer
        System.out.printf("%f\n", myDouble); //%f for double/float

        //[width]
        //minimum number of character to be written as output
        System.out.printf("Hello %10s\n", myString);
        //10 blank characters between string and statement will be created

        //[precision]
        //sets number of digits of precision when outputting floating-point values
        System.out.printf("You have %.2f money\n", myDouble); //%.2 will display the 2 first digits after comma

        //[flags]
        // adds an effect to output based on the flag added to format specifier

        // - : left justify
        System.out.printf("You have %-20f money\n", myDouble);

        // + : outputs a plus or a minus sign for a numeric value
        System.out.printf("You have %+f money\n", myDouble);

        // 0 : numeric values are zero-padded
        System.out.printf("You have %020f money\n", myDouble);

        // , : comma grouping separator if numbers > 1000
        System.out.printf("You have %,f money\n", myDouble);


    }
}
