class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current = nums[0]
        max_sum = 0
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                current += nums[i]
                
            else:
                max_sum  = max_sum if max_sum > current else current
                current = nums[i]
        return max_sum if max_sum > current else current