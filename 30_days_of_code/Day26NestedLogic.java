import java.io.*;
import java.util.*;
import java.time.*;

public class Solution {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        Calendar c = Calendar.getInstance();

        int actualDay = scan.nextInt();
        int actualMonth = scan.nextInt();
        int actualYear = scan.nextInt();
        Date actualDate = new Date(actualYear, actualMonth, actualDay);

        int expDay = scan.nextInt();
        int expMonth = scan.nextInt();
        int expYear = scan.nextInt();

        Date expDate = new Date(expYear, expMonth, expDay);


        if (actualDate.getTime() > expDate.getTime()){
            int fine = 0;
            int diff;
            int fineFactor;
            if (actualYear > expYear){
                fine = 10000;
            } else if (actualMonth == expMonth){
                fineFactor = 15;
                diff = (int) ( (actualDate.getTime()-expDate.getTime()) / (1000 * 60 * 60 * 24) );
                fine = diff * fineFactor;
            } else {
                fineFactor = 500;
                diff = actualMonth - expMonth;
                fine = diff * fineFactor;
            }

            System.out.println(fine);

        } else {
            System.out.println(0);
        }

    }
}
