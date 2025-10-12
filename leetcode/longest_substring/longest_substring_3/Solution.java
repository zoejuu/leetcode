import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Edge case: empty string
        if (s == null || s.isEmpty()) return 0;

        // Map from character -> its last seen index in the string
        Map<Character, Integer> last = new HashMap<>();

        int best = 0;   // best (max) window length seen so far
        int left = 0;   // left index of current window [left..right]

        // Iterate right pointer across the string
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);   // current character

            // If we've seen 'c' before, its previous index is last.get(c).
            // Only shrink the window if that previous occurrence lies inside the current window.
            Integer prev = last.get(c);
            if (prev != null && prev >= left) {
                // Move 'left' to one past the previous index of 'c'
                // This removes the duplicate from the window.
                left = prev + 1;
            }

            // Update last seen index of 'c' to the current index 'right'
            last.put(c, right);

            // Window is [left..right], so its length is right - left + 1
            int len = right - left + 1;
            if (len > best) {
                best = len;
            }
        }

        return best;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.lengthOfLongestSubstring("ohomm"));
    }
}
