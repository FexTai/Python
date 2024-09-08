public class encapsulation {
    public static void main(String[] args) {

        // Encapsulation = attributes of a class will be hidden or private,
        //                 can be accessed only through methods (getters & setters)
        //                 you should make attributes private if you have no reason to make them public/protected


        Machine car = new Machine("Chervolet", "Camaro", 2021);

        System.out.println(car.getMake());
        System.out.println(car.getModel());
        System.out.println(car.getYear());

        car.setYear(2022);
        car.setMake("Unknown");

        System.out.println("\n" + car.getYear() + "\n" + car.getMake());

    }
}
