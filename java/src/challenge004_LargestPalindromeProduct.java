public class challenge004_LargestPalindromeProduct {

    private static int reverse(int num) {
        int reversedNum = 0;
        while (num != 0) {
            reversedNum *= 10;
            reversedNum += num % 10;
            num /= 10;
        }
        return reversedNum;
    }

    public static void main(String args[]) {

        final long startTime = System.currentTimeMillis();

        int answer = 0;

        for (int num1 = 100; num1 < 1000; num1++) {
            for (int num2 = 100; num2 < 1000; num2++) {
                int mult = num1 * num2;
                if (mult == reverse(mult)) {
                    if (answer < mult) {
                        answer = mult;
                    }
                }
            }
        }

        System.out.println(answer);

        final long endTime = System.currentTimeMillis();

        System.out.println("Total execution time: " + (endTime - startTime) );

    }
}
