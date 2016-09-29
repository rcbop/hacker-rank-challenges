import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int[][] m = new int[6][6];
        for (int i=0;i<6;i++){
            for (int j=0;j<6;j++){
                m[i][j] = scan.nextInt();
            }
        }
        int finalSum,sum;
        finalSum = sum = -99999;
        for (int i=0;i<6;i++){
            for (int j=0;j<6;j++){
                if(j+2 < 6 && i+2 <6){
                    sum = m[i][j] + m[i][j+1] + m[i][j+2] +
                           m[i+1][j+1] +
                           m[i+2][j] + m[i+2][j+1] + m[i+2][j+2];
                    if (sum > finalSum){
                        finalSum = sum;
                    }
                }
            }
        }
        System.out.println(finalSum);

    }
}
