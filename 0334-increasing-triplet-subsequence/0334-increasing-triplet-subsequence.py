import math
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = math.inf
        second = math.inf

        for i in nums:
            if i <= first:
                first = i
            elif i <= second :
                second = i
            else:
                return True
        return False
        
