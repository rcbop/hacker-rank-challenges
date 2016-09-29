import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        String line = new Scanner(System.in).next();
        String ind = line.substring(line.length()-2, line.length());
        int hour = Integer.valueOf(line.substring(0,2));
        String rtn;
        boolean isAM = ind.startsWith("A");
        if (hour == 12){
            if (isAM){
                rtn = "00";
            } else {
                rtn = hour + "";
            }
        } else {
            if (isAM){
                rtn = String.format("%02d",hour);
            } else {
                rtn = hour + 12 +"";
            }

        }
        System.out.println(rtn + line.substring(2, line.length()-2));
    }
}
