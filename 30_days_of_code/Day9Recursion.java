import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        System.out.println(factorial(n));
    }

    private static int factorial(int n){
        if (n == 1)
            return 1;
        else
            return n * factorial(n-1);
    }
}
