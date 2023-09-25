import java.util.Arrays;

public class Day12 {
    public static int findDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                return nums[i];
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] array = {1, 3, 4, 2, 2};
        int duplicate = findDuplicate(array);
        System.out.println("The duplicate element is: " + duplicate);
    }
}
