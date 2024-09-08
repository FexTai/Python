import java.util.*;

public class ArrayLists_2D {
    public static void main(String[] args) {
        // 2D Array list = dynamic list of lists

        //single lists
        ArrayList<String> backery_list = new ArrayList<>();
        backery_list.add("pasta");
        backery_list.add("bread");
        backery_list.add("pizza");

        ArrayList<String> produce_list = new ArrayList<>();
        produce_list.add("tomatoes");
        produce_list.add("zucchini");
        produce_list.add("pepper");

        ArrayList<String> drinks_list = new ArrayList<>();
        drinks_list.add("Water");
        drinks_list.add("Sprite");

        //2D array
        ArrayList<ArrayList<String>> grocery_goods = new ArrayList<>();

        grocery_goods.add(backery_list);
        grocery_goods.add(produce_list);
        grocery_goods.add(drinks_list);

        System.out.println(grocery_goods.get(2).get(0));  // double get for "Coordinates"
    }
}
