public class j4b {
    public static void main(String[] args){
        double guthaben = 2000;
        double zielguthaben = 2 * guthaben;
        double zinssatz = 1.03;
        int i = 1;
        while(guthaben < zielguthaben){
            i++;
            guthaben = guthaben * zinssatz;
            System.out.println("Nach " + i + " Jahren " + " erreichst du den Betrag: " + guthaben + " euro ");
        }
    }
}