import javax.xml.transform.SourceLocator;

public class challenge005_SmallestMultiple {

    public static void main (String args[]) {

        final long startTime = System.currentTimeMillis();

        for (int num = 10; ; num++) {
            boolean done = false;
            for (int div = 1; div <= 20; div++) {
                if (num % div != 0) {
                    break;
                }
                if (div == 20) {
                    done = true;
                }
            }
            if (done) {
                System.out.println(num);
                break;
            }

        }

        final long endTime = System.currentTimeMillis();

        System.out.println("Total execution time: " + (endTime - startTime) );
    }

}
