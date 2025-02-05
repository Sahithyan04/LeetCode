class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()

        left = 0
        right = 0

        max_len = 0
        while right < len(s):
            while s[right] in set1:
                set1.remove(s[left])
                left += 1
                            
            set1.add(s[right])
            curr = right - left + 1
            max_len = (max_len if max_len > curr else curr)  
            right += 1
        return max_len
        