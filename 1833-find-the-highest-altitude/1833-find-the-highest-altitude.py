class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_val = 0

        current = 0

        for i in gain:
            current = current + i
            if current > max_val :
                max_val = current
        return max_val
