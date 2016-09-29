import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        int neg, pos, zer;
        neg = pos = zer = 0;
        for (int i=0;i<size;i++) {
            int value = scan.nextInt();
            if (value < 0){
                neg++;
            } else if (value > 0){
                pos++;
            } else {
                zer++;
            }
        }
        System.out.println(String.format("%.6f",(double)pos/size));
        System.out.println(String.format("%.6f",(double)neg/size));
        System.out.println(String.format("%.6f",(double)zer/size));
    }
}
