/* Write a Java program that prompts the user to enter an integer consisting of 3 digits, then display on the screen the sum of its individual digits.

Examples:
- If the user enters 431, the message should be: The sum of the individual digits of 431 is 8 (4+3+1 = 8).
- If the user enters 591, the message should be: The sum of the individual digits of 591 is 15 (5+9+1 = 15). */

import javax.swing.JOptionPane;

public class DigitsSum {
    public static void main(String[] args) {
        String numberStr = "";

        while (numberStr.length() != 3) {
            numberStr = JOptionPane.showInputDialog(null, "Enter an integer of 3 digits: ");
        }

        Integer sum = 0;

        for (int i = 0; i < 3; i++) {
            sum += Character.getNumericValue(numberStr.charAt(i));
        }

        JOptionPane.showMessageDialog(null, String.format("Sum: %d", sum));
    }
}
