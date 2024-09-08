public class array_2D {
    public static void main(String[] args) {
        //2D arrays = an array of arrays (Wie eine Tabelle)

        String[][] cars = new String[3][3];

        cars[0][0] = "Camaro";
        cars[0][1] = "Corvette";
        cars[0][2] = "Bugatti";

        cars[1][0] = "Mustang";
        cars[1][1] = "Ferrari";
        cars[1][2] = "BMW";

        cars[2][0] = "Honda";
        cars[2][1] = "Toyota";
        cars[2][2] = "Ranger";

        for (int i = 0; i < cars.length; i++) {
            System.out.println();
            for (int j = 0; j < cars[i].length; j++) {
                System.out.print(cars[i][j] + " ");

        //alternative initialisation
        //String cars[][] = {
                // {x,y,z},
                // {a,b,c},
                // {d,e,f}
                // };
            }
        }
    }



}
