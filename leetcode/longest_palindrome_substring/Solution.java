import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public boolean isPalindrome(String s) {
        boolean res = true;
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

    public String longestPalindrome(String s) {
        List<String> palindromeStrings = new ArrayList<>();
        Set<Character> chars = new HashSet<>();

        for (int i=0; i<s.length(); i++) {
            chars.add(s.charAt(i));
        }
        System.out.println(chars.toString());

        for (char target : chars) {
            List<Integer> mapped = new ArrayList<>();
            for (int i=0; i<s.length(); i++) {
                if (target == s.charAt(i)) {
                    mapped.add(i);
                }
            }

            if (mapped.size() >= 2) {
                for (int j=0; j<mapped.size(); j++) {
                    for (int k=j+1; k<mapped.size(); k++) {
                        int start = mapped.get(j);
                        int end = mapped.get(k);
                        // retrieve a substring starting and ending with the same char
                        String sub = s.substring(start, end+1);
                        // check if the substring is palindrome
                        if (isPalindrome(sub)) {
                            palindromeStrings.add(sub);
                        }
                    }
                }
            }
        }

        String longgest = s.charAt(0)+"";
        for (String palindrom : palindromeStrings) {
            if (palindrom.length() > longgest.length()) {
                longgest = palindrom;
            }
        }

        return longgest;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.longestPalindrome("aacabdkacaa"));
    }
}