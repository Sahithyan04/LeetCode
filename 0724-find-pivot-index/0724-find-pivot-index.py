class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = 0
        suffix = 0
        n = len(nums)
        pre_list =[0]*n
        suf_list = [0]*n

        for i in range(len(nums)):

            pre_list[i] = prefix

            prefix += nums[i]

        for j in range(len(nums)-1,-1,-1):
            suf_list[j] = suffix

            suffix +=nums[j]
        for i in range(n):
            if pre_list[i] == suf_list[i]:
                return i
        return -1
        





