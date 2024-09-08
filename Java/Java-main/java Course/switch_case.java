public class switch_case {
    public static void main(String[] args) {

        //switch = statement, which allows a variable to be tested for equality against a list or value
        String day = "Montag";

        switch (day){ //in switch() kommt die variable, die überprüft werden soll
            case "Sonntag":
                System.out.println("es ist Sonntag");
                break;
            case "Samstag":
                System.out.println("Es ist Samstag");
                break;
            case "Freitag":
                System.out.println("Es ist Freitag");
                break;
            case "Donnerstag":
                System.out.println("Es ist Donnerstag");
                break;
            case "Mittwoch":
                System.out.println("Es ist Mittwoch");
                break;
            case "Dienstag":
                System.out.println("Es ist Diesntag");
                break;
            case "Montag":
                System.out.println("Es ist Montag");
                break;
            default:
                System.out.println("Es ist kein Wochentag! ");

        }

    }
}
