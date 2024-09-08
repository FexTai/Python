public class overloaded_constructors {
    public static void main(String[] args) {
        // overloaded constructor = multiple constructors within a class with the same name
        //                          but have different parameters
        //                          name + parameter = signature

        Pizza pizza = new Pizza("thick crust", "tomato", "mozzarella", "peperoni");
        System.out.println("The ingredients of your Pizza: ");
        System.out.println(pizza.Bread);
        System.out.println(pizza.Sauce);
        System.out.println(pizza.Cheese);
        System.out.println(pizza.Topping);

        Pizza pizza2 = new Pizza("crust", "Pizza sauce", "Gouda");
        System.out.println("\nThe ingredients of your Pizza: ");
        System.out.println(pizza2.Bread);
        System.out.println(pizza2.Sauce);
        System.out.println(pizza2.Cheese);

        Pizza pizza3 = new Pizza("thick crust", "tomato");
        System.out.println("\nThe ingredients of your Pizza: ");
        System.out.println(pizza3.Bread);
        System.out.println(pizza3.Sauce);
        System.out.println(pizza3.Cheese);
        System.out.println(pizza3.Topping);
    }
}
