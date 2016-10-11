import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        for (int j=0; j<k; j++){
            if (a.length == k)
                break;
            int[] tmp = new int[n];
            System.arraycopy(a,1,tmp,0,a.length-1);
            tmp[tmp.length-1] = a[0];
            a = tmp;
        }
        System.out.println(Arrays.toString(a).replaceAll("[^.0-9\\s]",""));
    }
}
