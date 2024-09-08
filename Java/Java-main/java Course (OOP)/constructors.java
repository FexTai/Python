public class constructors {
    public static void main(String[] args) {

        // constructor = special method, which is called, when an object is instantiated (created)

        Human human = new Human("Rick", 65, 60); //needs same amount of arguments as in the object
        Human human2 = new Human("Morty", 17, 50);
        System.out.println(human.Name);
        System.out.println(human2.Name);
        human.drink();
        human2.eat();

    }
}
