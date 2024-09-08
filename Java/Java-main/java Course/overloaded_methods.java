public class overloaded_methods {
    public static void main(String[] args) {
        // overloaded methods = methods, which share the same name, but have different parameters
        //                      method name + parameters = method signature

        double x = sum1(1,2, 5, 8.3);
        System.out.println(x);

    }

    static int sum1(int a, int b) {
        System.out.println("Overloaded method nr1");
        return a + b;
    }
    static int sum1(int a, int b, int c) {
        System.out.println("Overloaded method nr2");
        return a + b + c;
    }
    static int sum1(int a, int b, int c, int d) {
        System.out.println("Overloaded method nr3");
        return a + b + c + d;
    }


    static double sum1(double a, double b) {
        System.out.println("Overloaded method nr4");
        return a + b;
    }
    static double sum1(double a, double b, double c) {
        System.out.println("Overloaded method nr5");
        return a + b + c;
    }
    static double sum1(double a, double b, double c, double d) {
        System.out.println("Overloaded method nr6");
        return a + b + c + d;
    }

}
