class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        p = len(nums) -1
        ptr1 =0
        ptr2 = len(nums) -1
        while ptr1 <= ptr2:
            if nums[ptr2] ** 2 > nums[ptr1] ** 2:
                ans[p] = nums[ptr2] ** 2
                p -= 1
                ptr2 -= 1 
            else:
                ans[p] = nums[ptr1] ** 2
                ptr1 += 1
                p -= 1

        return ans


        