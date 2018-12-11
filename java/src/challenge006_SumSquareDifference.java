public class challenge006_SumSquareDifference {

    public static void main (String args[]) {

        final long startTime = System.currentTimeMillis();

        int sumSquares = 0;
        int sumSquared = 0;

        for (int i = 1; i <= 100; i++) {
            sumSquares += (i*i);
            sumSquared += i;
        }

        sumSquared *= sumSquared;

        int answer = sumSquared - sumSquares;

        System.out.println(answer);

        final long endTime = System.currentTimeMillis();

        System.out.println("Total execution time: " + (endTime - startTime) );
    }

}
