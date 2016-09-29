import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int number = scan.nextInt();
        for (int i = 1; i <= 10; i++) System.out.println(number + " x " + i + " = " + (number*i));
    }
}
