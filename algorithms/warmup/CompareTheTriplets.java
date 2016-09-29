import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int[] a = fillArray(in);
        int[] b = fillArray(in);

        int sumA = 0;
        int sumB = 0;

        for (int i = 0; i < 3; i++){
            if (a[i] != b[i] ) {
                if (a[i] > b[i]){
                    sumA +=1;
                } else {
                    sumB +=1;
                }
            }
        }
        System.out.println(sumA + " " + sumB);
    }

    public static int[] fillArray(Scanner in){
        return Arrays.stream(in.nextLine().split("\\s+")).mapToInt(Integer::parseInt).toArray();
    }
}
