class Solution:
    def check(self, nums: List[int]) -> bool:
        srt = sorted(nums)
        nums1 = nums
        for i in range(0,len(nums)):
            if nums1 == srt:
                return True
            else:
                nums1.append(nums1.pop(0))
        return False
        