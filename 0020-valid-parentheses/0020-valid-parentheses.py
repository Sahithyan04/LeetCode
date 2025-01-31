class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = list(s)
        stack1 = []
        opening = ['(','{','[']
        closing = [')','}',']']
        if len(s) < 2:
            return False
        for i in s:
            if i in opening :
                stack1.append(i)
            elif i in closing:
                if not stack1:
                    return False

                if closing.index(i) != opening.index(stack1[-1]):

                    return False
                else:
                    stack1.pop()   
        return len(stack1) == 0 