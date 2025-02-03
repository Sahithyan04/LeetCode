class Solution:
    def reverse(self, x: int) -> int:
        signed = 1
        rev = 0 
        if x < 0:
            signed = 0
            x = - x
        while x != 0 and x % 10 == 0:
            x = x // 10
        while x !=0:
            r = x % 10
            rev = rev*10 + r 
            x = x // 10
        
        if  rev > (2**31)-1:
            return 0
        if signed == 0:
            rev = (-rev)
            return rev
        else: 
            return rev
        
            


