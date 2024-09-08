public class Pizza {

    String Bread;
    String Sauce;
    String Cheese;
    String Topping;

    Pizza(String bread, String sauce, String cheese, String topping){
        Bread = bread;
        Sauce = sauce;
        Cheese = cheese;
        Topping = topping;
    }

    Pizza(String bread, String sauce, String cheese) {
        Bread = bread;
        Sauce = sauce;
        Cheese = cheese;
    }

    Pizza(String bread, String sauce) {
        Bread = bread;
        Sauce = sauce;
    }

    Pizza(String bread) {
        Bread = bread;
    }

}
