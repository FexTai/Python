package package2;
import package1.*;

public class C {
    public String publicMessage = "This message is public!";
    //public modifier allows everyone and everywhere to access the class

    String defaultMessage = "This message is default"; //can only be accessed by classes within the package
    //no modifier = default modifier!
}
