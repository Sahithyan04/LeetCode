class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        r = len(nums) - 1  
        l = 0 
        j = 0
        # k = len(nums) - nums.count(val)
        if len(nums) == 0  :
            return -1
        if val not in nums:
            return len(nums)
        while l < r:
            if nums[r] == val :
                r -= 1
            elif nums[l] == val:
                nums[l],nums[r] = nums[r],nums[l]
                j += 1
                l += 1
                r -= 1
            else:
                l+=1
            
        id = nums.index(val)
        j = len(nums[:id])
        return j