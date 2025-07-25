class NumArray {

    int[] pre ;

    public NumArray(int[] nums) {
        this.pre = prefix_sum(nums);
        
                
    }
    
    public int sumRange(int left, int right) {
        
        return (left ==0)? pre[right]:(pre[right] - pre[left - 1]);
        
    }
    public int[] prefix_sum(int[] nums){
        int pre[] = new int[nums.length];
        pre[0] = nums[0];

        for (int i =1 ; i<nums.length;i++){
            pre[i] = nums[i]+pre[i-1];
        }
        return pre;



    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */