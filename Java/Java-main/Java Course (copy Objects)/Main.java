public class Main {
    public static void main(String[] args) {

        Car_java_copy car1 = new Car_java_copy("Chevrolet", "Camaro", 2021);
        //Car_java_copy car2 = new Car_java_copy("Ford", "Mustang", 2022);


        //car2 = car1;  its does not copy the attributes of the object rather it replaces the objects itself making the
        //address of those objects the same, so its more of cloning rather than copying


        //car2.copy(car1);


        //copying the attributes on instantiation
        Car_java_copy car2 = new Car_java_copy(car1);//requires an overloaded constructor in the Main Car class

        //addresses
        System.out.println(car1);
        System.out.println(car2);
        System.out.println();

        //car1 attributes
        System.out.println(car1.getMake());
        System.out.println(car1.getModel());
        System.out.println(car1.getYear());
        System.out.println();

        //car2 attributes
        System.out.println(car2.getMake());
        System.out.println(car2.getModel());
        System.out.println(car2.getYear());
    }
}
