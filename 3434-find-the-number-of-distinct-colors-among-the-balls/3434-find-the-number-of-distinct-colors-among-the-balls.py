class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_map = {}
        colour_map = {}
        result = []

        for ball , col in queries:
            if ball in ball_map :
                pre = ball_map[ball]
                colour_map[pre] -= 1
                if colour_map[pre] == 0:
                    del colour_map[pre]
            ball_map[ball] = col
            colour_map[col] = colour_map.get(col,0) + 1
            result.append(len(colour_map))
        return result

