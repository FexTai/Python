public class String_Methods {
    public static void main(String[] args) {

        String name = "FexTy";
        boolean result = name.equals("FexTy"); //Compares String to another String and returns boolean value, true or false
        boolean result2 = name.equalsIgnoreCase("fexty"); //ignores lower and uppercase spelling
        System.out.println(result + " " + result2);

        //lenght method
        int x = name.length();
        System.out.println("Länge des Names: " + x); //Starts at 1, not at 0

        //char method
        char y = name.charAt(3); // Starts at 0, not 1
        System.out.println("Buchstabe an stelle 3: " + y);

        //index method
        int a = name.indexOf("e"); //Sucht die Stelle des Buchstabens e
        System.out.println("Buchstabe e ist an stelle " + a);

        //isEmpty method
        boolean b = name.isEmpty();
        System.out.println(b);

        //uppercase/lowercase method
        String c = name.toUpperCase();
        String d = name.toLowerCase();
        System.out.println(c + " " + d);

        //trimming blank spaces
        String name1 = "   FexTy   ";
        System.out.println(name1);
        String trim = name1.trim();
        System.out.println(trim);

        //replace method (Replacing character in a string)
        String rep = name.replace("y", "ai");
        System.out.println(rep);

    }
}
