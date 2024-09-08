import java.util.ArrayList;

public class ArrayLists {
    public static void main(String[] args) {
        // Arraylist = resizeable array
        //             elements can be added and removed after compilation phase
        //             store reference data types --> wrapper classes instead of primitive types must be used

        ArrayList<String> food = new ArrayList<String>();
        food.add("Pizza");
        food.add("Hot-Dog");
        food.add("Burger");

        //useful methods
        food.set(1, "Sushi");
        //food.remove(2);
        //food.clear(); //deletes all values

        for (int i = 0; i < food.size(); i++){
            System.out.println(food.get(i));
        }
    }
}
