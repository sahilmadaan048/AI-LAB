import java.util.*;

public class Main {
    public static void main(String[] args) {
        int a = 10;

        if (a < 9) {
            System.out.println(a);
            ++a;  // will not run 
            System.out.println(a);
        }

        System.out.println("after if block: " + a);
    }
}