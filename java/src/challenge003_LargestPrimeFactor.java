import java.util.ArrayList;
import java.util.Collections;

public class challenge003_LargestPrimeFactor {

    public static boolean prime(int num) {
        double root = Math.sqrt(num);
        int lim = (int) Math.ceil(root);
        for (int i = 2; i < lim; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static boolean prime(long num) {
        double root = Math.sqrt(num);
        int lim = (int) Math.ceil(root);
        for (int i = 2; i < lim; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String args[]) {

        final long startTime = System.currentTimeMillis();

        long checkNum = 600851475143L;

        double root = Math.sqrt(checkNum);
        int lim = (int) Math.ceil(root);

        ArrayList<Integer> primeDivs = new ArrayList<Integer>();

        for (int div = 2; div < lim; div++) {
            if (prime(div) && checkNum % div == 0) {
                primeDivs.add(div);
            }
        }

        System.out.println(Collections.max(primeDivs));

        final long endTime = System.currentTimeMillis();

        System.out.println("Total execution time: " + (endTime - startTime) );
    }
}
