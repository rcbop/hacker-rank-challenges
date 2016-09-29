public class Solution {
    public static void main(String[] args) {
        /* Declare second integer, double, and String variables. */
        int i2; double d2; String s2;

        /* Read and save an integer, double, and String to your variables.*/
        i2 = Integer.valueOf(scan.nextLine());
        d2 = Double.valueOf(scan.nextLine());
        s2 = scan.nextLine();

        /* Print the sum of both integer variables on a new line. */
        System.out.println(i + i2);

        /* Print the sum of the double variables on a new line. */
        System.out.println(d+d2);

        /* Concatenate and print the String variables on a new line;
            the 's' variable above should be printed first. */
        System.out.println(s + s2);
    }
}
