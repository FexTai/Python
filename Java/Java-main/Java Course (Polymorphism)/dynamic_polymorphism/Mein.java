package dynamic_polymorphism;

import java.util.Scanner;

public class Mein {
    public static void main(String[] args) {

        // polymorphism = many shapes/forms
        // dynamic = after compilation (during runtime)

        // ex. a Corvette is a car, a vehicle but also an object (OOP)
        // simply said dynamic polymorphism is the ability of an object to take many shapes and forms after compilation

        Animal_1 animal;

        Scanner scanner = new Scanner(System.in);
        System.out.println("What animal do you want?");
        System.out.println("(1 = dog, 2 = cat)");

        int choice = scanner.nextInt();

        switch (choice){
            case 1:
                animal = new Dog_2();
                animal.speak();
                break;
            case 2:
                animal = new Cat_2();
                animal.speak();
                break;
            default:
                animal = new Animal_1();
                System.out.println("Your chose is invalid! ");
                animal.speak();
        }


    }
}
