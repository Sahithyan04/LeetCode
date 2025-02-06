class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        freq = {}
        count_add = 0
        maxodd = 0
        for c in s:
            freq[c] = freq.get(c,0) + 1
        # return freq
        
        # for i in freq.values():
            if freq[c] %2 == 1  :
                count_add += 1
            else:
                count_add -= 1
                # maxodd = (maxodd if maxodd > i else i)
        if count_add > 0:
            return len(s) - count_add +1
        else:
            return len(s)