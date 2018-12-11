public class eulerChallenges {

    public static boolean prime(int num) {
        double root = Math.sqrt(num);
        int lim = (int) Math.ceil(root);
        for (int i = 2; i <= lim; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static boolean prime(long num) {
        double root = Math.sqrt(num);
        int lim = (int) Math.ceil(root);
        for (int i = 2; i <= lim; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static long arrayProduct(int[] arr) {
        long total = 1;
        for (int num: arr) {
            total = total * num;
        }
        return total;
    }
}
