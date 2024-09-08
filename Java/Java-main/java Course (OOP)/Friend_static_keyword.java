public class Friend_static_keyword {
    String name;
    static int numberOfFriends; //shared copy in the class instance
    Friend_static_keyword(String name){
        this.name = name;
        numberOfFriends++;
    }

    //static method
    static void displayFriends(){
        System.out.println("You have " + numberOfFriends + " Friends");
    }

}
