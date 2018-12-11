public class challenge009_specialPythagoreanTriple {
    public static void main(String args[]) {

        final long startTime = System.currentTimeMillis();

        answer();

        final long endTime = System.currentTimeMillis();

        System.out.println("Total execution time: " + (endTime - startTime) );
    }

    public static int answer() {
        for (int a = 1;a < 1000; a++) {
            for (int b = 1;b < 1000-a; b++) {
                int c = 1000 - a - b;
                if (a*a + b*b == c*c) {
                    System.out.println(a*b*c);
                    return a*b*c;
                }
            }
        }
        return 9999;
    }
}
