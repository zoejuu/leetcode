class Solution {
    public int myAtoi(String s) {
        // remove leading blanks
        int i = 0;
        int length = s.length();
        while (i < length && (s.charAt(i) == ' '))
            i++;
        if (i == length)
            return 0;

        // determine sign
        int sign = 1;
        if (s.charAt(i) == '+' || s.charAt(i) == '-') {
            sign = s.charAt(i) == '+' ? 1 : -1;
            i++;
        }
        
        int res = 0;
        int LIMIT = Integer.MAX_VALUE / 10;
        int LIMIT_DIGIT = sign == 1 ? 7 : 8;

        while (i < length && Character.isDigit(s.charAt(i))) {
            int digit = s.charAt(i) - '0';
            if (res < LIMIT || (res == LIMIT && digit < LIMIT_DIGIT)) {
                res *= 10;
                res += digit;
                i++;
            } else {
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            
        }

        return res*sign;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.myAtoi("-21474836482"));
    }
}