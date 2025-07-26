class Solution {
    public int numberOfSubarrays(int[] nums, int k) {

        HashMap<Integer, Integer> hmap = new HashMap<>();
        
        hmap.put(0,1);
        for(int i =0;i< nums.length; i++){
            if(nums[i]%2 == 0){
                nums[i] = 0;
            }else{
                nums[i] = 1;
            }
        }

        int presum = 0;
        int count = 0;

        for (int i: nums){
            presum += i;
            if(hmap.containsKey(presum-k)){
                count +=hmap.get(presum-k);
            } 
            hmap.put(presum, hmap.getOrDefault(presum, 0)+1);
        }
        return count;
        
    }
}