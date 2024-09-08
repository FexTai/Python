public class static_keyword {
    public static void main(String[] args) {

        // static = modifier. A single copy of a variable/method is created and shared
        //          the class "owns" the static member

        Friend_static_keyword friend1 = new Friend_static_keyword("Spongebob");
        Friend_static_keyword friend2 = new Friend_static_keyword("Patrick");
        Friend_static_keyword friend3 = new Friend_static_keyword("Jenny");
        Friend_static_keyword friend4 = new Friend_static_keyword("Sandy");

        Friend_static_keyword.displayFriends(); //now able to access class functions/variables directly without
                                                //accessing the different instances (friend1, friend2 ...)
                                                //accessing the different instances (friend1, friend2 ...)

        //Math.round(); is also a library class with static methods shared crossover

    }
}
