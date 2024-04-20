public class MultiplicationTable {
    public static void main(String[] args) {

        System.out.println("\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10");
        System.out.println("------------------------------------------------------------------------------------");

        for (int i = 1; i <= 10; i++) {
            System.out.printf("%d\t|", i);

            for (int j = 1; j <= 10; j++) {
                System.out.printf("%d\t", i * j);
            }
            
            System.out.println();
        }
    }
}
