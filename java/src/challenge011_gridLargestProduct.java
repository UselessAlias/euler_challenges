import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class challenge011_gridLargestProduct {
    public static int leftToRight(HashMap<Key, Integer> m, int x, int y) {
        int increment = 0;
        int prod = 1;
        Key pos;
        while (increment < 4) {
            pos = new Key(x + increment, y);
            int v = m.get(pos);
            prod *= v;
            increment++;
        }
        return prod;
    }

    public static int upToDown(HashMap<Key, Integer> m, int x, int y) {
        int increment = 0;
        int prod = 1;
        Key pos;
        while (increment < 4) {
            pos = new Key(x, y +increment);
            int v = m.get(pos);
            prod *= v;
            increment++;
        }
        return prod;
    }

    public static int diagUpToDown(HashMap<Key, Integer> m, int x, int y) {
        int increment = 0;
        int prod = 1;
        Key pos;
        while (increment < 4) {
            pos = new Key(x + increment, y + increment);
            int v = m.get(pos);
            prod *= v;
            increment += 1;
        }
        return prod;
    }

    public static int diagDownToUp(HashMap<Key, Integer> m, int x, int y) {
        int increment = 0;
        int prod = 1;
        Key pos;
        while (increment < 4) {
            pos = new Key(x + increment, y - increment);
            int v = m.get(pos);
            prod *= v;
            increment += 1;
        }
        return prod;
    }

    public static void main (String args[]) {

        final long startTime = System.currentTimeMillis();

        File file = new File("/Users/masond/Documents/Personal Docs/git/euler_challenges/java/files/c_11.txt");

        HashMap<Key, Integer> matrix = new HashMap<>();
        int x = 0;
        int y = 0;

        if (file.exists()) {
            try {
                Scanner sc = new Scanner(file);
                Key k;
                while (sc.hasNext()) {
                    k = new Key(x, y);
                    matrix.put(k, sc.nextInt());
                    x++;
                    if (x == 20) {
                        x = 0;
                        y++;
                    }
                }
            }
            catch (FileNotFoundException nope) {
                System.out.println("Error!");
            }
        }

        int a = 0;
        int b = 0;

        int maxProd = 1;
        int prod = 1;

        while (b < 20) {
            try {
                prod = leftToRight(matrix, a, b);
            }
            catch (NullPointerException lTRE) {
                prod = 1;
            }
            if (maxProd < prod) {
                maxProd = prod;
            }
            try {
                prod = upToDown(matrix, a, b);
            }
            catch (NullPointerException uTDE) {
                prod = 1;
            }
            if (maxProd < prod) {
                maxProd = prod;
            }
            try {
                prod = diagDownToUp(matrix, a, b);
            }
            catch (NullPointerException dDTUE) {
                prod = 1;
            }
            if (maxProd < prod) {
                maxProd = prod;
            }
            try {
                prod = diagUpToDown(matrix, a, b);
            }
            catch (NullPointerException dUTDE) {
                prod = 1;
            }
            if (maxProd < prod) {
                maxProd = prod;
            }
            a++;
            if (a == 20) {
                a = 0;
                b++;
            }
        }

        System.out.println(maxProd);

        final long endTime = System.currentTimeMillis();

        System.out.println("Total execution time: " + (endTime - startTime) );
    }

}
