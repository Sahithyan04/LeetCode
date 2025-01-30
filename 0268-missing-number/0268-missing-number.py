class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # lenght = n   , Last Element = n 

        n = len(nums) 
        natural = (n*(n+1)) // 2
        sum_val = sum(nums)
        return (- sum_val + natural)