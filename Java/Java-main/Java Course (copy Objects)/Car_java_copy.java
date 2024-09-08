public class Car_java_copy {

    private String make;
    private String model;
    private int year;

    //constructor
    Car_java_copy(String make, String model, int year){
        this.setMake(make);
        this.setModel(model);
        this.setYear(year);
    }

    //overloaded constructor
    Car_java_copy(Car_java_copy x){
        this.copy(x);
    }


    //creating "getters" to return private variables inside a class to another class
    public String getMake(){
        return make;
    }

    public String getModel(){
        return model;
    }

    public int getYear(){
        return year;
    }

    //creating "setters"
    public void setMake(String make){
        this.make = make;
    }

    public void setModel(String model){
        this.model = model;
    }

    public void setYear(int year){
        this.year = year;
    }

    public void copy(Car_java_copy x){ //x is a reference to an undefined object
        this.setMake(x.getMake()); //set is taking the value of attribute class and is replacing it with the get of the other class
        this.setModel(x.getModel());
        this.setYear(x.getYear());
    }
    //by using this method instead of simply writing car1 = car2; we keep the individual addresses but change the values

}

