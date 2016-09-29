import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int matrixSize = scan.nextInt();
        int[][] matrix = new int[matrixSize][matrixSize];
        for (int i = 0; i < matrix[0].length; i++){
            for (int j=0; j< matrix.length; j++){
                matrix[i][j]=scan.nextInt();
            }
        }

        int diag1 =0;
        int diag2 =0;
        for (int index=0; index < matrix.length; index++){
            diag1 += matrix[index][index];
            diag2 += matrix[matrix.length-index-1][index];
        }

        System.out.println(Math.abs(diag1 - diag2));


    }
}
