public class challenge1_Sumof3and5 {

    public static void main (String args[]) {

        final long startTime = System.currentTimeMillis();

        int sum = 0;

        for (int x = 1; x < 1000; x++) {
            if (x % 3 == 0 || x % 5 == 0) {
                sum += x;
            }
        }

        System.out.println(sum);

        final long endTime = System.currentTimeMillis();

        System.out.println("Total execution time: " + (endTime - startTime) );
    }

}
