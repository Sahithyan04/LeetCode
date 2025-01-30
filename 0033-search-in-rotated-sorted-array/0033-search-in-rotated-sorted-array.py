class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = ( left + right ) // 2
            if nums[mid] == target :
                return mid
            #left
            elif nums[mid] >= nums[left]:
                if target > nums[mid] or nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            #right
            else:
                if target < nums[mid] or nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
