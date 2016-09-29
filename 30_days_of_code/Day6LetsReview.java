import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int s = scan.nextInt();
        for (int j=0;j<s;j++) {
            String line = scan.next();

            String[] word = line.split("(?!^)");
            String even, odd;
            odd = even = "";
            for (int k=0;k<word.length;k++){
                if( k % 2 == 0) {
                    even += word[k];
                } else {
                    odd += word[k];
                }
            }
            System.out.println(even + " " + odd);
        }
    }
}
