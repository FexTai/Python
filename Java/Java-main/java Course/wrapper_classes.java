public class wrapper_classes {
    public static void main(String[] args) {
        // wrapper class = provides a way to use primitive types as reference types
        //when converting into reference Datatype you the processing get slower,but you get some useful methods

        //autoboxing
        Boolean a = true;
        Character b = 'é';
        Integer c = 123;
        Double d = 3.14;
        String e = "FexTy"; //String is a reference datatype
        // all capital names created reference datatype

        a.booleanValue();
        b.charValue();
        c.byteValue();
        d.byteValue();
        e.isBlank();
        // not possible with primitive Values


        //unboxing (treting reference types as primitive types)
        if (a == true) {
            System.out.println("This is true!!");
        }
    }
}
