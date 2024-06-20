public class Main {

    public class Member {
        private String name, id;
        private double amountDue;

        // fill in the blanks to initialize all the field variables
        public Member(String name, String id, double amountDue) {
            this.name = name;
            this.id = id;
            this.amountDue = amountDue;
        }

        public String getName() {
            return name;
        }

        public String getId() {
            return id;
        }

        public double getAmount() {
            return amountDue;
        }

        public void display() {
            System.out.println("In class Member");
        }

        public String toString() {
            return String.format("name is: %s , id is : %s , amountDue is %d\n:", name, id, amountDue);
        }
    }

    public class Student extends Member {
        private String course;

        // fill in the blanks to initialize the field variable.
        public Student(String n, String i, double m, String c) {
            super(n, i, m);
            this.course = c;
        }

        public String getCourse() {
            return course;
        }

        // Write the missing part needed to call the toString method declared in the
        // superclass and to return the value of the course field.
        public String toString() {
            return super.toString() + String.format("course is: %s\n", course);
        }
    }

    public static void main(String[] args) {

    }
}
