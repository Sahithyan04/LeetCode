class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_val = sum(nums[:k])
        max_avg = sum_val /k
        for i in range(k,len(nums)):
            sum_val += nums[i]
            sum_val -= nums[i-k]
            max_avg = (max_avg if max_avg>(sum_val/k) else sum_val/k)
        return max_avg
