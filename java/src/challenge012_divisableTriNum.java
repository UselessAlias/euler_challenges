public class challenge012_divisableTriNum {
    public static int countDividors (long num) {
        double d = num;
        double root = Math.sqrt(d);
        int divisorCount = 0;
        for (double i = 1; i < root + 1; i++) {
            if (d % i == 0) {
                divisorCount += 1;
            }
        }
        return divisorCount * 2;
    }

    public static void main(String args[]) {

        final long startTime = System.currentTimeMillis();

        int divisorCount;
        long num = 1;
        long triNum = 0;
        do {
            triNum += num;
            num++;

        } while (countDividors(triNum) <= 500);
        System.out.println(triNum);

        final long endTime = System.currentTimeMillis();

        System.out.println("Total execution time: " + (endTime - startTime) );
    }
}
