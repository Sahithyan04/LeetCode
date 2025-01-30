class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        def find_pos(nums,target,values):
            left ,right = 0 , len(nums) -1
            i = -1
            while left <=right:
                mid = (left + right) // 2 
                if nums[mid] < target :
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    i = mid
                    if values:
                        right = mid -1
                    else:
                        left = mid + 1
            return i


        res = [find_pos(nums,target,True),find_pos(nums,target,False)]
        return res
    
        