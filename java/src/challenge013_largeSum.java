import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class challenge013_largeSum {
    public static void main (String args[]) {

        final long startTime = System.currentTimeMillis();

        File file = new File("/Users/masond/Documents/Personal Docs/git/euler_challenges/java/files/c_13.txt");

        char c;
        int d;
        long sum = 0;
        HashMap<Integer, Integer> calc = new HashMap<>();
        try {
            Scanner sc = new Scanner(file);
            while (sc.hasNext()) {
                String word = sc.next();
                for (Integer i = word.length() - 1; i < 0; i--) {
                    c = word.charAt(i);
                    d = Character.getNumericValue(c);
                    Integer add = calc.get(i);
                    

                }
            }
            System.out.println(sum);
        }
        catch (FileNotFoundException noFile) {
            System.out.println("Didn't find file.");
        }

        final long endTime = System.currentTimeMillis();

        System.out.println("Total execution time: " + (endTime - startTime) );
    }

}
