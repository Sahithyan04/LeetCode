class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) -1 
        while left <= right:
            midd = (left + right) // 2
            if nums[midd] == target:
                return midd
            elif nums[midd]<target:
                left = midd +1
            else:
                right = midd -1
        return left
        