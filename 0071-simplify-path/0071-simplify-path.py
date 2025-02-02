class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directory = path.split("/")

        for i in directory :
            if i == "." or not i :
                continue
            elif i == "..": 
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/" + "/".join(stack)

        