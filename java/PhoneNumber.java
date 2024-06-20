/* A) Write a class PhoneNumber that has:
● Two private instance field variables: areaCode of type integer and localNumber of type
String.
● A constructor with two parameters that sets the values of both field variables to those
passed as parameters.
● A set and get method for the areaCode field
● A static method named info with no parameters and does not return a value. The
method prints the string “Amman” if area code is 6 else prints “another area”
B) In the main method
● Create an object of class PhoneNumber. Name this object n1 and initialize it with
areaCode= 5, and localNumbre= 67744822.
● Print the areaCode of n1 object using a get method.
● Call the info method using n1 object. */

public class PhoneNumber {
    private Integer areaCode;
    private String localNumber;

    public PhoneNumber(Integer ac, String ln) {
        areaCode = ac;
        localNumber = ln;
    }

    public Integer getAreaCode() {
        return areaCode;
    }

    public void setAreaCode(Integer ac) {
        areaCode = ac;
    }

    public void info() {
        System.out.println(areaCode == 6 ? "Amman" : "Another area");
    }

    public static void main(String[] args) {
        PhoneNumber n1 = new PhoneNumber(5, "67744822");

        System.out.println(n1.getAreaCode());

        n1.info();
    }
}
