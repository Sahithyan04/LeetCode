class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # rev_str = []
        # fin_str = []
        # word = list(word)
        # left = 0
        # for right in range(len(word)-1):
        #     if word[right] == ch:
        #         rev_str = word[:right+1][::-1]
        #         fin_str = rev_str + word[right +1:]

        #         return "".join(fin_str)
        
        # return "".join(word)
        word = list(word)
        if ch in word:
            idx = word.index(ch)
        else:
            return ''.join(word)

        right = 0 
        while right <= idx:
            word[right] , word[idx] = word[idx] , word[right]
            right = right + 1
            idx -= 1
        return ''.join(word) 



        

              