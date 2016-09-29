import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        char[] arr = s.toLowerCase().replace(" ","").toCharArray();

        final Set set = new HashSet();

        for (char c: arr){
            set.add(c);
        }

        String msg;
        if(set.size() == 26){
            msg = "pangram";
        } else {
            msg = "not pangram";
        }
        System.out.println(msg);
    }
}
