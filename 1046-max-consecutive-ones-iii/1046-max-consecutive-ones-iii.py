class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        max_val = 0 
        left = 0 
        right = 0
        z_count = 0 #nums[:k].count(0)
        max_val = 0 #len(nums[left:right])
        while right < len(nums):
            if nums[right] == 0:
                z_count += 1

            # if z_count <= k:
            #     if nums[right] == 0:
            #         z_count +=1
            #     right += 1

            while z_count > k:
                if nums[left] == 0:
                    z_count -= 1
                left +=1
            length = right - left +1
            max_val = max_val if max_val>length else length
            right += 1
        return max_val
       