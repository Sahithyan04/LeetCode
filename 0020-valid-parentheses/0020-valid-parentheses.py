class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        closevalue = {']':'[','}':'{',')':'('}
        for i in s:
            if i in closevalue:
                if stack and stack[-1] == closevalue[i]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(i)
        return True if not stack else False