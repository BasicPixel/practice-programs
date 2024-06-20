public class Arrays {
    public static void main(String[] args) {
        int p[][] = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8 } };

        for (int[] i : p) {
            for (int j : i) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }
}
