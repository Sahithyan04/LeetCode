class Solution {
    public int pivotIndex(int[] nums) {
        var pre = 0;
        
        var count =0;
        var sum = 0;
        for(int num:nums){
            sum += num;
        }
        for(int i = 0;i<nums.length;i++){
            
            int r_sum = sum - pre - nums[i];
            if(r_sum == pre){
                return i;
            }            
            pre += nums[i];
        }return -1;

    }
}