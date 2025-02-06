# from itertools import permutations
from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # hmap = {}
        # count = 0
        # per = permutations(nums,4)
        # for item in list(per):
        #     if item in hmap:
        #         if item[0] * item [1] == item[2] * item[3] :
        #             count += 1
        #     else:
        #         hmap[item] = 1
        product_count = defaultdict(int)
        count = 0

        # Check all pairs (i, j) and store the product counts
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                count += product_count[product] * 8  # Each pair can form 8 valid permutations
                product_count[product] += 1

        return count

        return count
        