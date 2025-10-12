import java.util.ArrayList;
import java.util.List;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        // if s length = 0, return 0
        if (s.length() <= 0) {
            return 0;
        }

        // declare ArrayList to store substrings + initialise with the whole string
        List<String> substrings = new ArrayList<>();
        substrings.add(s);

        // make substring starting with each char in s
        for (int i=0; i<s.length(); i++) {
            String sub = s.substring(i);
            int a = -1;

            for (int j=s.length()-1; j>=i; j--) {
                for (int k=j-1; k>=i; k--) {
                    if (s.charAt(j) == s.charAt(k)) {
                        a = j;
                    }
                }
            }
            if (a != -1) {
                sub = s.substring(i, a);
            }
            substrings.add(sub);
        }

        if (substrings.size() > 1) {
            substrings.remove(0);
        }
        System.out.println(substrings.toString());

        // given the arraylist of substrings, find the longgest length & return
        int longgest = substrings.get(0).length();
        for (String string : substrings) {
            if (longgest < string.length()) {
                longgest = string.length();
            }
        }

        return longgest;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.lengthOfLongestSubstring("abba"));
    }
}
