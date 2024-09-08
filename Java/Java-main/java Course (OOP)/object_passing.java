public class object_passing {
    public static void main(String[] args) {

        garage_passing garage = new garage_passing();

        Car_passing car1 = new Car_passing("BMW");
        Car_passing car2 = new Car_passing("Tesla");
        Car_passing car3 = new Car_passing("Ferrari");

        garage.park(car1); //can only be used at the objects from Car_passing class!
        garage.park(car2); //Because the argument of the function park was declared as
        garage.park(car3); //the objects of the class Car_passing
    }
}
