public class Arrays2 {
    public static void main(String[] args) {
        int array1[][] = { { 2, 1, 3 }, { 4, 5, 6 } };
        int array2[][] = { { 1, 2 }, { 3 }, { 4, 5, 6 } };

        // Find minimum element in array1
        int min1 = array1[0][0];
        for (int[] i : array1) {
            for (int j : i) {
                if (j < min1)
                    min1 = j;
            }
        }

        // Find maximum element in array2
        int max2 = 0;
        for (int[] i : array2) {
            for (int j : i) {
                if (j > max2)
                    max2 = j;
            }
        }

        // Find sum of both arrays combined
        int sum = 0;
        for (int[] i : array1) {
            for (int j : i)
                sum += j;
        }
        for (int[] i : array2) {
            for (int j : i)
                sum += j;
        }

        System.out.printf("Minimum element in array1: %d\n"
                + "Maximum element in array2: %d\n"
                + "Sum of all elements in both arrays: %d\n", min1, max2, sum);
    }
}
