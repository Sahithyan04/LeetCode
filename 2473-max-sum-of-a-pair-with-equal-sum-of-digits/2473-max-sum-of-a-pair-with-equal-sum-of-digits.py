class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))

        transformed = [digit_sum(num) for num in nums]
        hmap = {}  
        max_val = -1  

        for idx, val in enumerate(transformed):
            if val in hmap:  
                max_val = max(max_val, nums[idx] + hmap[val])  
                hmap[val] = max(hmap[val] , nums[idx])
            else:
                hmap[val] = nums[idx] 

        return max_val  

        