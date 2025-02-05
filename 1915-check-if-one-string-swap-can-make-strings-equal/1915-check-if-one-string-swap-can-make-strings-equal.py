class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        freq1 = {}
        freq2 = {}
        count = 0 

        for c in s1:
            if c in freq1:
                freq1[c] += 1
            else:
                freq1[c] = 1
        for d in s2:
            if d in freq2:
                freq2[d] +=1
            else:
                freq2[d] = 1
        print(freq1)
        print(freq2)
        if freq1 != freq2:
            return False  
        for j in range(len(s1)):
            if s1[j] == s2[j]:
                continue
            else:
                count += 1
        if count < 3:
            return True
        else:
            return False
        # if len(freq1) != len(freq2):
        #     return False
        # else:
        
        #     for key in freq1:
        #         if key not in freq2 or freq1[key] != freq2[key]:
        #             return False
        #             break
        #     else:
            
        #         return True
        