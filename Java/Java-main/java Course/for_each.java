import java.util.ArrayList;

public class for_each {
    public static void main(String[] args) {
        //for each loop = traversing technique to iterate through the elements in an array/collection
        //                less steps, more readable
        //                less flexible

        String[] animals = {"cat", "dog", "rat", "bird"};
        ArrayList<String> animals1 = new ArrayList<>();
        animals1.add("mammal");
        animals1.add("weasel");
        animals1.add("rabbit");
        animals1.add("snake");

        for(String i : animals) { //read out: for every String index in animals do...
            System.out.println(i);//List element gets stored in the index, so you don´t need to print the index of list
        }
    }
}
