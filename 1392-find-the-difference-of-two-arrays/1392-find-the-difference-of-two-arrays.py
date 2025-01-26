class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        ns1 = set(nums1)
        ns2 = set(nums2)

        output_i = []
        output_j = []
        for  i in ns1:
            
            if i not in ns2:
                if i not in output_i:
                    output_i.append(i)
    
        for  j in ns2:
            
            if j not in ns1:
                if j not in output_j:
                    output_j.append(j)
            
        return [output_i,output_j]
