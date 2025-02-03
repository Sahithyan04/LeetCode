class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_count = 1
        left = 0 
        if len(nums)== 1:
            return 1
        
        for right in range(1,len(nums)):
            if nums[right-1] >= nums[right]:
                left = right
            else:
                max_count = max(max_count,right - left + 1)
        left = 0
        for right in range(1,len(nums)):                   
            if nums[right - 1] <= nums[right]:
                left = right
            else:
                max_count =max(max_count , right - left +1)
                
            

                
        return max_count