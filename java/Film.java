/* Question 2:
A) Write a java class called Film. This class has:
● Three private instance field variables:
title, which is a String representing the title of the film
studio, which is a String representing the studio that made the film
rating, which is a String representing the rating of the film (i.e. PG13, R, etc)
● Two constructors:
o The first constructor has three parameters t1, s1 and r1 that will initialize the
field variables title, studio and rating respectively.
o The second constructor has two parameters t2 and s2 that will initialize the field
variables title and studio respectively. Set the variable rating with the value “R”.
● A method named checkRating which has no parameters, and the return type is void.
The method displays the message “You are not allowed to watch the film” if the rating is
equal to R. The method displays the message “Enjoy watching the film” if the rating is
equal to PG-13. (Use Dialog Boxes to display the messages)
B) In the main method
● Create an object of class Film. Name this object f1 and initialize it with the title “Royale”,
the studio “Eon Productions”, and the rating “PG13”. (Use the first constructor).
● Create an object of class Film. Name this object f2 and initialize it with the title “Mestry”
and the studio “Abc Productions”. (Use the second constructor)
● Call the mehod checkRating using f1 object. */

import javax.swing.JOptionPane;

public class Film {
    private String title;
    private String studio;
    private String rating;

    public Film(String t1, String s1, String r1) {
        title = t1;
        studio = s1;
        rating = r1;
    }

    public Film(String t2, String s2) {
        title = t2;
        studio = s2;
        rating = "R";
    }

    public void checkRating() {
        if (rating == "R") {
            JOptionPane.showMessageDialog(null, "You are not allowed to watch the film");
        } else if (rating == "PG-13") {
            JOptionPane.showMessageDialog(null, "Enjoy watching the film");
        }
    }

    public static void main(String[] args) {
        Film f1 = new Film("Royale", "Eon Productions", "PG13");
        // Film f2 = new Film("Mestry", "Abc Productions");

        f1.checkRating();
    }
}
