public class methods {
    public static void main(String[] args) {
        //method = a block of code, which gets executed, when called upon
        //needs to be created outside the main method

        String name = "FexTy";
        int age = 17;

        hello();
        hello1(name, age); //arguments and parameters must be matching


    }

    static void hello() {               //main method is static so in order to call other methods those must be static too
        System.out.println("Hello! ");  //void returns no value
    }

    static void hello1(String title, int year) {       //void is a return type and main method is static so in order to call other methods those
        System.out.println("Hello " + title + " you are " + year + " years old");  // must be static too
    }

}
