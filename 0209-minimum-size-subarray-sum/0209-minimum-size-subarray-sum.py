class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sum_val = 0
        min_length = len(nums) + 1
        while right < len(nums):
            sum_val += nums[right]
            while sum_val >= target:
                length = right -left +1
                
                min_length = min_length if min_length < length else length
                sum_val -= nums[left]
                left +=1
            right += 1
        if min_length == len(nums)+1:
            return 0
        return min_length

