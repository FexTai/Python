public class super_keyword {
    public static void main(String[] args) {

        // super = refers to a superclass (parent) of an object
        //         very similar to the ".this" keyword

        Hero hero1 = new Hero("Batman", 42, "Money");
        System.out.println(hero1.name);
        System.out.println(hero1.age);
        System.out.println(hero1.power + "\n");

        Hero hero2 = new Hero("Superman", 52, "Everything");
        System.out.println(hero2.toString());
    }
    //Parent
    static public class Human{

        String name;
        int age;

        //constructor
        Human(String name, int age){
            this.name = name;
            this.age = age;
        }

        //overridden toString method
        public String toString(){
            return this.name + "\n" + this.age + "\n";
        }
    }


    //Child
    public static class Hero extends Human{

        String power;

        Hero(String name, int age, String power){
            super(name, age); //taking the name and age variables from the parent class "Human"
            this.power = power;
        }
        public String toString(){
            return super.toString() + this.power;
        }
    }

}
