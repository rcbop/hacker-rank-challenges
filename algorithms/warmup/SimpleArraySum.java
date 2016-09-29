import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int arraySize = Integer.valueOf(scan.nextLine());
        String arrayStr = scan.nextLine();
        String[] strArray = arrayStr.split("\\s+");
        int sum = 0;
        for (int i= 0; i< arraySize; i++){
            sum += Integer.parseInt(strArray[i]);
        }
        System.out.println(sum);
    }
}
