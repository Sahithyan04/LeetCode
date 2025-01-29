class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        output = []
        n = len(potions)
        for i in range(0,len(spells)) :
            
            left = 0
            right = len(potions)

            
            while left < right:
            
                midd = (left + right) >> 1
                new_poi = spells[i] * potions[midd]
                if new_poi >= success:

                    right = midd
               
                else:
                    left = midd +1
            output.append(n - left)

        return output

            