class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []
        i= 0 
        while i < n:
            j = i +1 
            k = n - 1
            target = 0 - nums[i]
            while j < k:
                if nums[j] + nums[k] > target :
                    k -= 1
                elif nums[j] + nums[k] < target :
                    j +=1
                elif  nums[j] + nums[k] == target :
                    output.append([nums[i],nums[j],nums[k]])
                    
                    j += 1
                    k -= 1

            i += 1
            
        unique_set = set()
        unique_list = []
        for sublist in output:
            tuple_sublist = tuple(sublist) 
            if tuple_sublist not in unique_set:
                unique_set.add(tuple_sublist)
                unique_list.append(sublist)

        return unique_list

        
