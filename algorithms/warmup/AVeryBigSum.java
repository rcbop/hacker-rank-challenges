import java.io.*;
import java.util.*;
import java.math.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        BigInteger sum = scan.nextBigInteger();
        for (int i=0; i < size-1; i++) {
            sum =sum.add(scan.nextBigInteger());
        }
        System.out.println(sum);

    }
}
