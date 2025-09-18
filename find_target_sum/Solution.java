package find_target_sum;
import java.util.Arrays;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] results = new int[2];

        for (int i = 0; i<nums.length; i++) {
            for (int j = i+1; j<nums.length; j++) {
                if (nums[i] + nums[j] == target){
                    results[0] = i;
                    results[1] = j;
                    return results;
                }
            }
        }
        return results;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        int[] nums = {1,2,3,4,5};
        int target = 5;
        int[] sum = s.twoSum(nums, target);
        
        System.out.println(Arrays.toString(sum));
    }
}