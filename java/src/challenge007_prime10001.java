public class challenge007_prime10001 {
    public static void main (String args[]) {

        final long startTime = System.currentTimeMillis();

        int count = 1;

        for (int i = 3; ; i++) {
            if (eulerChallenges.prime(i)) {
                count++;
                if (count == 10001) {
                    System.out.println(i);
                    break;
                }
            }
        }

        final long endTime = System.currentTimeMillis();

        System.out.println("Total execution time: " + (endTime - startTime) );
    }

}
