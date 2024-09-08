public class person {
    String klasse;
    String Name; double Height; double Weight; double Bmi;

    //Constructor (wird bei Erstellung des Objektes ausgeführt)
    person(String name, double height, double weight) {
        //Variablen zuweisen, um sicherzustellen, dass sie innerhalb der Klasse person abrufbar sind
        Name = name;
        Height = height;
        Weight = weight;

        double bmi = Math.round(weight/(height*height)*10)/10.0;
        Bmi = bmi;
        if(bmi < 18.5) {
            klasse = "untergewichtig";
        }
        else if(bmi > 18.5 && bmi <= 24.9) {
            klasse = "normalgewichtig";
        }
        else if(bmi > 24.9 && bmi <= 29) {
            klasse = "übergewichtig";
        }
        else if(bmi > 29.9 && bmi <= 34.9) {
            klasse = "fettleibig";
        }
        else if(bmi > 34.9){
            klasse = "stark übergewichtig";
        }
    }

}

