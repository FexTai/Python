package package1;
import package2.*;

public class A {
    protected String protectedMessage = "This message is protected!";
    //protected classes can only be accessed by subclasses in any package

    public static void main(String[] args) {
        B b = new B();
        //System.out.println(b.privateMessage);   cannot be accessed due to the private access modifier
    }

    }

