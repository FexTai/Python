public class Car {
    String make = "Honda";
    String model = "Civic Facelift";
    int year = 2024;
    double price = 38900;

    public String toString() { //overriding the actual toString method to replace the address with strings
        return make + "\n" + model + "\n" + year;
    }

    void drive() {
        System.out.println("You drive the car!");
    }
    void brake() {
        System.out.println("You step on the brakes!");
    }
}
