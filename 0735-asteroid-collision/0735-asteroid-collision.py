class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] 
        for astro in asteroids:
            if astro > 0 :
                stack.append(astro)
                
            elif astro < 0:
                pos_astro = - astro
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(astro)
                else:
                    if pos_astro == stack[-1]:
                        stack.pop()
                    else:
                        while stack and stack[-1] > 0 and pos_astro > stack[-1]:
                            stack.pop()

                        if len(stack) != 0 and pos_astro == stack[-1]:
                            stack.pop()                       
                        elif len(stack) != 0 and stack[-1] < 0:
                            stack.append(astro)
                        elif len(stack) == 0:
                            stack.append(astro)

                    
                
                
        return stack

        