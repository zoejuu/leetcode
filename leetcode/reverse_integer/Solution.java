/**
 * Given a signed 32-bit integer x, return x with its digits reversed.
 * If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
 */

class Solution {
    /*
     * Attempt 1
     * - All test cases passed, but took 9ms runtime
     * - Discarded to find a more efficient way
     */
    public int reverse_(int x) {
        // convert to string
        String s = Integer.toString(x);
        String sign = "";
        String reversed = "";

        // if it starts with a sign (e.g. -) store it separately
        if (!Character.isDigit(s.charAt(0))) {
            sign = s.substring(0,1);
            s = s.substring(1);
        }

        // perform reverse
        for (int i=s.length()-1; i>=0; i--) {
            reversed += s.charAt(i);
        }
        // System.out.println(reversed);

        // if it is out of bound, return 0
        int res;
        try {
            res = Integer.parseInt(sign+reversed);
        } catch (Exception e) {
            res = 0;
        }

        return res;
    }
    
    /**
     * Attemp 2
     * - All test case passed with efficient runtime (<1ms)
     */
    public int reverse(int x) {
        int reversed = 0;

        while (x != 0){
            // using modulo (%) to get the last digit
            int a = x%10;
            // use division (/) to point to the next digit
            x = x/10;
            
            // check if overflow
            if ((reversed > Integer.MAX_VALUE / 10) || ((reversed == Integer.MAX_VALUE) && a > 7))
                return 0;
            if ((reversed < Integer.MIN_VALUE / 10) || ((reversed == Integer.MIN_VALUE) && a < -8))
                return 0;

            reversed = reversed * 10 + a;

            // System.out.println(reversed);

        }

        return reversed;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.reverse(-2147483419));
    }
}