import java.net.SocketOption;

public class challenge2_EvenFibonacci {

    public static void main (String args[]) {

        final long startTime = System.currentTimeMillis();

        int sumo = 0;

        int x = 1, y = 2;
        while (y < 4000000) {
            if (y % 2 == 0) {
                sumo += y;
            }
            int z = x + y;
            x = y;
            y = z;
            System.out.println(y);
        }

        System.out.println(sumo);

        final long endTime = System.currentTimeMillis();

        System.out.println("Total execution time: " + (endTime - startTime) );
    }

}
