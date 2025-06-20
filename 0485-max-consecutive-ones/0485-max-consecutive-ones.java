class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count = 0;
        int maxi = 0;
        for (int i =0 ; i < nums.length ; i++){
            if (nums[i] == 1){
                count += 1;
            }else{
                maxi = (maxi > count) ? maxi : count ;
                count = 0;
            }
            
        }
        return (maxi>count) ? maxi : count;

        
    }
}