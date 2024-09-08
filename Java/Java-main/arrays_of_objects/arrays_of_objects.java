public class arrays_of_objects {
    public static void main(String[] args) {

        int[] numbers = new int[3];
        char[] characters = new char[4];
        String[] strings = new String[5];

        //food[] refrigirator = new food[5];

        food food1 = new food("chicken");
        food food2 = new food("Pizza");
        food food3 = new food("Burger");

        food[] refrigirator = {food1, food2, food3};

        //refrigirator[0] = food1;
        //refrigirator[1] = food2;
        //refrigirator[2] = food3;

        System.out.println(refrigirator[0].name);
        System.out.println(refrigirator[1].name);
        System.out.println(refrigirator[2].name);
    }
}
