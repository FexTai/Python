import java.util.Arrays;

public class arrays {
    public static void main(String[] args) {
        int[] numbers = new int[5];  //primitive type needs a new statement to create an array, number in int gives the
                                    // amount of list items
        numbers[1] = 1;             //giving index 1 the value of 1
        System.out.println(numbers);  //only printing the ADRESS of the array
        System.out.println(Arrays.toString(numbers));
        //newer way to initialise array
        int[] list = {2, 3, 4, 2, 1};
        Arrays.sort(list);
        System.out.println(list.length); //arrays have fixed length so no items can be added rn
        System.out.println(Arrays.toString(list));
    }
}
