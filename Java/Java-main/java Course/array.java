public class array {
    public static void main(String[] args) {
        // array = used to store multiple values in one variable

        String[] cars = {"Toyota", "Tesla", "Hyundai"}; //arrays can only store one Datatype at once

        //alternative initialisation
        String[] car = new String[3];
        car[0] = "Toyota";

        cars[0] = "Mustang";
        System.out.println(cars[2] + car[0]);

        for (int i = 0; i<cars.length; i++) {
            System.out.println(cars[i]);
        }

    }
}
