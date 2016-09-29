import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        int[] s = new int[size];
        int count = 0;
        while (scan.hasNextInt()) s[count++] = scan.nextInt();
        for (int i=0; i<size; i++){
            System.out.print(s[size - i -1]+" ");
        }
    }
}
