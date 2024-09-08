public class inheritance {
    public static void main(String[] args) {

        // inheritance =    the process where one class acquires the attributes and methods of another
        // often used, when you have 2 or more classes to combine the same variables/methods in one

        car car = new car();
        bicycle bike = new bicycle();

        bike.stop();

        System.out.println(car.doors); //.doors unique to car class
        System.out.println(bike.pedals); //.pedals unique to bike class


    }


    //Parent class
    static class vehicle {
        double speed;
        void go(){
            System.out.println("this vehicle is moving");
        }
        void stop(){
            System.out.println("the vehicle has stopped");
        }
    }

    //child class of vehicle
    static class bicycle extends vehicle { //with the "extends" keyword the bicycle can now access the vehicle class
        int wheels = 2;
        int pedals = 2;
    }

    //child class of vehicle
    static class car extends vehicle{ //with the "extends" keyword the car can now access the vehicle class
        int wheels = 4;
        int doors = 4;
    }
}
