import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();

        int[] sticks = new int[size];

        for (int i=0;i<size;i++){
            sticks[i] = scan.nextInt();
        }

        Arrays.sort(sticks);

        int a,b,c;
        for (a=size-3, b=size-2, c=size-1; sticks[a]+sticks[b]<=sticks[c];a--,b--,c--){
            if (a == 0) {
                System.out.println(-1);
                return;
            }
        }
        System.out.println(sticks[a] + " " + sticks[b] + " " + sticks[c]);
    }
}
