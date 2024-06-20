import java.util.Scanner;

public class TriangleArea {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the base of the triangle: ");
        float base = scanner.nextFloat();

        System.out.print("Enter the height of the triangle: ");
        float height = scanner.nextFloat();

        double area = 0.5 * base * height;

        System.out.printf("Triangle area: %f", area);

        scanner.close();
    }
}
