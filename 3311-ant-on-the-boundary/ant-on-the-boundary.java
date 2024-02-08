class Solution {
    static int[] prefix(int[] nums){
            int list[] = new int[nums.length];
            list[0] = nums[0];

            for (int i = 1; i < nums.length; ++i){
                list[i] = list[i-1] + nums[i];
            }

            return list;
        }

    public int returnToBoundaryCount(int[] nums) {
        int[] op = prefix(nums);
        int zeros = 0;

        for (int i : op){
            if (i == 0){
                ++zeros;
            }
        }
        return zeros;

    }
}