class Solution {
    public int subarraySum(int[] nums, int k) {

        HashMap<Integer,Integer> hash = new HashMap<>();

        hash.put(0,1);

        var count = 0;
        var pre = 0;

        for(int i : nums){
            pre += i;

            if(hash.containsKey(pre-k)){
                count += hash.get(pre-k);
            }
            hash.put(pre,hash.getOrDefault(pre, 0)+1);

        }return count;
        
        
    }
}