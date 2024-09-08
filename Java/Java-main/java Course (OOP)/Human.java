public class Human {

    String Name; int Age; double Weight;

    //constructor gets executed because it´s inside the class method
    Human(String Name, int Age, double Weight){ //constructor has the same name as the object
        this.Name = Name;
        this.Age = Age;
        this.Weight = Weight;
        System.out.println("constructers get executed on creation of an object");

        //or you can just use different variable names from parameters

        //name = Name;
        //age = Age;
        //weight = Weight;


    }
    void eat() {
        System.out.println(this.Name + " is eating");
    }
    void drink(){
        System.out.println(this.Name + " is drinking");
    }
}
