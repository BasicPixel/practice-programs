abstract class Animal {
    String name;

    abstract void eat();

    public Animal(String name) {
        this.name = name;
        System.err.println("Animal: " + this.name);
    }
}

public class Dog extends Animal {
    void eat() {
        System.err.println("Eating...");
    }

    public Dog(String name) {
        super(name);
        System.err.println("Dog: " + this.name);
    }

    public static void main(String[] args) {
        Dog dog1 = new Dog("Bashar");

        for (int i = 1; i < 3; i++) {
            for (int j = 0; j <= 1; j++)
                System.out.print(j);
            if (i == 1)
                continue;
        }
    }
}
