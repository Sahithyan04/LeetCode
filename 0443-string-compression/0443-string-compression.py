class Solution:
    def compress(self, chars: List[str]) -> int:
        left ,right = 0 , 0
        s = ""
        n = len(chars)
        while right < n:
            if right + 1 == n:
                length = right - left +1
                char = chars[left]
                if length > 1 :
                    s += char+str(length)
                else:
                    s += char
                right += 1
                left = right
            elif chars[left] == chars[right+1]:
                right += 1
            else:
                length = right - left +1
                char = chars[left]
                if length > 1 :
                    s += char+str(length)
                else:
                    s += char
                right += 1
                left = right
        size = len(s)
        for i in range(size):
            chars[i] = s[i]
        return size


