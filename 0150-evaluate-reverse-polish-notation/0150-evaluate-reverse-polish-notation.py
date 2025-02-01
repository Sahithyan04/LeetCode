class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for sym in tokens:
            if sym == '+':
                stack.append(stack.pop()+stack.pop())
            elif sym == '-':
                f = stack.pop()
                s = stack.pop()
                stack.append(s-f)
            elif sym == '*':
                stack.append(stack.pop() * stack.pop())
            elif sym == '/':
                f = stack.pop()
                s = stack.pop()
                stack.append(int(s/f))
            else:
                stack.append(int(sym))
        return int(stack[0])
        