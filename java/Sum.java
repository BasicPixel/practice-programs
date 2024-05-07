import java.util.Scanner;

public class Sum {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		int num1, num2, sum;

		System.out.println("Enter num1: ");
		num1 = input.nextInt();

		System.out.println("Enter num2: ");
		num2 = input.nextInt();

		sum = num1 + num2;
		System.out.printf("Sum is %d\n", sum);

		input.close();
	}

}
