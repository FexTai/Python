import java.util.Arrays;

public class multidim_arrays {
    public static void main (String[] args) {
        int[][] numbers = new int[2][2];
        numbers[0][0] = 1;
        System.out.println(Arrays.deepToString(numbers));
        //newer way
        int[][] list = { { 1, 2, 3, 4 }, { 1,2,3,4,5 } };
        System.out.println(Arrays.deepToString(list));
    }
}
