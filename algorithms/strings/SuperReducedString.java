import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String rtn = findCharPairs(scan.nextLine());
        rtn = findCharPairs(rtn);

        if (rtn.length()==0) rtn = "Empty String";
        System.out.println(rtn);
    }

    private static String findCharPairs(String s){
        StringBuilder sb = new StringBuilder(s);
        for (int i=1;i<sb.length();i++){
            if(sb.charAt(i) == sb.charAt(i-1)){
                sb.delete(i-1,i+1);
                i=0;
            }
        }
        return sb.toString();
    }
}
