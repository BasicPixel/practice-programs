/* Question 1:
A) Write a java class called Product. This class has:
● Three private instance field variables: name of type String, quantity of type integer and
price of type double.
● A constructor with three parameters that sets the values of the field variables to those
passed as arguments.
● set and get methods for the name field
● A method displayInfo with no parameters and returns a String representation of the
Product information (name, quantity and price)
● A method checkPrice with no parameters and return a String. It will check the price. If
the price is greater than 10, the method returns “high price” else returns “low price”.

B) In a main method
● Create an object of class Product. Name this object p1 and initialize it with name=
“P123”, quantity =10 and price =3.5.
● Print the name field variable of p1 object using a get method.
● Call the displayInfo method using p1 object.
● Call the method checkPrice method using p1 object. */

public class Product {
    private String name;
    private Integer quantity;
    private double price;

    public Product(String n, Integer q, double p) {
        name = n;
        quantity = q;
        price = p;
    }

    public String getName() {
        return name;
    }

    public void setName(String n) {
        name = n;
    }

    public String displayInfo() {
        return String.format("Name: %s\nQuantity: %d\nPrice: %f.2", name, quantity, price);
    }

    public String checkPrice() {
        return (price > 10) ? "High price" : "Low price";
    }

    public static void main(String[] args) {
        Product p1 = new Product("P123", 10, 3.5);

        System.out.printf("Name of p1: %s\n\n", p1.getName());
        p1.displayInfo();
        p1.checkPrice();
    }
}
