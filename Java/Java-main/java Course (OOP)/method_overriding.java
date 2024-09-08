public class method_overriding {
    public static void main(String[] args) {

        // method overriding = Declaring a method in a subclass,
        //                     which is already present in a parent class.
        //                     Done so that a child class can give its own implementation

        Animal animal = new Animal();

        Dog dog = new Dog();

        dog.speak();
        animal.speak();

    }
    //Parent class
    static class Animal{
        void speak(){
            System.out.println("The animal has spoken! ");
        }
    }

    //child class
    static class Dog extends Animal {
        @Override
        void speak(){  //method overriding from parent class in child class
            System.out.println("The dog goes bark! ");
        }
    }

}
