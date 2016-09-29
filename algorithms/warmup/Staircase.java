import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        for (int y=0; y<size; y++){
            for (int x=0; x<size; x++){
               if (x+y >= (size-1)){
                    System.out.print("#");
               } else {
                    System.out.print(" ");
               }
            }
            System.out.println();
        }
    }
}
