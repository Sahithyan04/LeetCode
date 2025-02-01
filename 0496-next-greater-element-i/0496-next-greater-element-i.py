class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1index = {n:i for i,n in enumerate(nums1)}
        res = [-1]*len(nums1)
        stack =[]
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                var =stack.pop()
                idx = num1index[var]
                res[idx] = nums2[i]

            if nums2[i] in num1index :
                stack.append(nums2[i])
            


        return res