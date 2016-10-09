import java.io.*;
import java.util.*;

public class Solution {

    static int numberOfSwaps;

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        int[] arr = new int[size];
        numberOfSwaps = 0;
        for (int i=0;i<size;i++){
            arr[i] = scan.nextInt();
        }
        sort(arr);
        System.out.println("Array is sorted in " + numberOfSwaps + " swaps.");
        System.out.println("First Element: " + arr[0]);
        System.out.println("Last Element: " + arr[arr.length-1]);
    }

    public static int[] sort(int[] arr){
        for (int i = 0; i < arr.length; i++) {

            for (int j = 0; j < arr.length - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1);
                    numberOfSwaps++;
                }
            }

            if (numberOfSwaps == 0) {
                break;
            }
        }

        return arr;
    }

    private static void swap(int[] arr, int x, int y){
        int temp = arr[y];
        arr[y] = arr[x];
        arr[x] = temp;
    }
}
