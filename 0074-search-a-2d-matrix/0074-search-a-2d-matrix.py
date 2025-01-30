class Solution:

    def BinarySearch(self ,arr ,target):
        left = 0
        right = len(arr) -1
        while  left <= right:
            mid = (left + right) // 2
            if arr[mid] < target :
                left = mid + 1
            elif arr[mid] > target :
                right = mid -1
            elif arr[mid] == target:
                return True
        return False                

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:

            if self.BinarySearch(i,target):
                return True
        return False