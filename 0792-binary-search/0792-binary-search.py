class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left ,right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if target not in nums:
                return -1
            if nums[mid] < target:
                left +=1
            elif nums[mid] > target :
                right -=1
            elif nums[mid] == target :
                return mid 
            elif target not in nums:
                return -1
