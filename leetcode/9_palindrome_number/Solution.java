class Solution {
    // public boolean isPalindrome(int x) {
    //     // edge case - if x is negative (never be palindrome)
    //     if (x<0) {
    //         return false;
    //     }

    //     boolean res = false;

    //     // convert x to string
    //     String original = x+"";
    //     String reversed = "";

    //     // make string x to reverse order
    //     for (int i=original.length()-1; i>=0; i--) {
    //         reversed += original.charAt(i);
    //     }

    //     // compare x and reversed x
    //     long y = Long.parseLong(reversed);

    //     if (x==y) {
    //         res = true;
    //     }

    //     return res;
    // }

    public boolean isPalindrome(int x) {
        // edge case - if x is negative (never be palindrome)
        if (x<0) {
            return false;
        }

        boolean res = true;

        // convert x to string
        String s = Integer.toString(x);
        int len = s.length();

        // compare each char from back and forth
        int i = 0;
        for (int j=len-1; j>=(double)len/2; j--) {
            if (s.charAt(i) != s.charAt(j)) {
                res = false;
                break;
            }
            i++;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.isPalindrome(1001));
    }
}