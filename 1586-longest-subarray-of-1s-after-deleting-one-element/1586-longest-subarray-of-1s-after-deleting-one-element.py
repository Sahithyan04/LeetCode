class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        max_value = 0 
        k = 1
        z_count = 0
        while right < len(nums):
            if nums[right] == 0:
                z_count += 1
            
            while z_count > k:
                if nums[left] == 0 :
                    z_count -= 1
                left += 1
            length = right - left + 1
            max_value = max_value if max_value > length else length
            right +=1
        return max_value -1

        