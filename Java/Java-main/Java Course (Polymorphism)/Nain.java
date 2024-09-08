public class Nain {
    public static void main(String[] args) {
        // polymorphism = greek word for poly (many), morph (form)
        //                The ability of an object to identify as more than one type

        Car_1 car = new Car_1();
        Bicycle bicycle = new Bicycle();
        Boat boat = new Boat();

        Fahrzeug[] racers = {car, bicycle, boat};
        // can only be stored in this object, because all the children classes also identify as the parent object
        // basically only the "Fahrzeug" class can store all the children classes

        for(Fahrzeug x : racers){ //von Anfang des Arrays von Fahrzeug(x) bis zur anzahl der Array mitglieder
            x.go();
        }
    }

}
