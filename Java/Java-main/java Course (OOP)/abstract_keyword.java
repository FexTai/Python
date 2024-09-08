public class abstract_keyword {
    public static void main(String[] args) {
        // abstract = abstract classes cannot be instantiated, but they can have a subclass
        //            abstract methods are declared without an implementation

        //Vehicle vehicle = new Vehicle();    //can add an abstract keyword to class to prevent from creating unwanted objects
        Car car = new Car();
        car.go();


    }

    //Superclass
    public static abstract class Vehicle{  //abstract keyword prevents the class from instantiating so no objects can be created
        abstract void go();
    }

    //Subclass
    public static class Car extends Vehicle{
        @Override
        void go(){
            System.out.println("The person is driving the car!");
        }
    }

}
