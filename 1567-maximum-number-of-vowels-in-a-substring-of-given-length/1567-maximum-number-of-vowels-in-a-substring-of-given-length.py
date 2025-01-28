class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count      
        for j in range(k, len(s)):
            if s[j] in vowels:
                count += 1
            if s[j-k] in vowels:
                count -=1
            max_count = max_count if max_count > count else count
        return max_count
