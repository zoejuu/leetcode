import java.util.ArrayList;
import java.util.List;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() <= 0) {
            return 0;
        }

        List<Integer> lengths = new ArrayList<>();
        lengths.add(s.length());
        int duplication = 0;

        for (int i=0; i<s.length(); i++) {

            for (int j=i+1; j<s.length(); j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    if (duplication == 0) {
                        lengths.set(0, s.length()-(s.length()-i));
                        lengths.add(0);
                        duplication++;
                    }
                    int len = j-i;
                    lengths.set(duplication, len);
                    lengths.add(s.length() - j);
                    duplication++;
                    break;
                }
            }
        }

        System.out.println(lengths.toString());
        int longest = lengths.get(0);

        for (int len : lengths) {
            if (longest < len) {
                longest = len;
            }
        }
        return longest;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.lengthOfLongestSubstring(""));
    }
}
