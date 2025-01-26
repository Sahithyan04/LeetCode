class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        

        output_i = []
        output_j = []
        for  i in nums1:
            
            if i not in nums2:
                if i not in output_i:
                    output_i.append(i)
    
        for  j in nums2:
            
            if j not in nums1:
                if j not in output_j:
                    output_j.append(j)
            
        return [output_i,output_j]
