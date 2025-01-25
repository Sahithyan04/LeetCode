class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i , value in enumerate(nums):
            dff = target - value
            if dff in hash:
                return [i,hash[dff]]
            hash[value] = i
        return []
       
