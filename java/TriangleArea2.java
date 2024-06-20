import javax.swing.JOptionPane;

public class TriangleArea2 {
    public static void main(String[] args) {
        float base = Float.parseFloat(JOptionPane.showInputDialog(null, "Enter the base of the triangle: "));

        float height = Float.parseFloat(JOptionPane.showInputDialog(null, "Enter the height of the triangle: "));

        double area = 0.5 * base * height;

        JOptionPane.showMessageDialog(null, String.format("Triangle area: %f", area));
    }
}
