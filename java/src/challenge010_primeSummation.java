public class challenge010_primeSummation {
    public static void main (String args[]) {

        final long startTime = System.currentTimeMillis();

        long sum = 2;

        for (long num = 3; num < 2000000; num = num + 2) {
            if (eulerChallenges.prime(num)) {
                sum += num;
            }
        }

        System.out.println(sum);

        final long endTime = System.currentTimeMillis();

        System.out.println("Total execution time: " + (endTime - startTime) );
    }

}

