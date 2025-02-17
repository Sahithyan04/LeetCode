class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        seq =set()
        used = [False] * len(tiles)
        self.gen_seq(tiles,"", used, seq)
        return len(seq) -1
    def gen_seq(self, tiles, current, used, seq):
        seq.add(current)
        for pos, char in enumerate(tiles):
            if not used[pos]:
                used[pos] = True
                self.gen_seq(tiles, current + char, used, seq)
                used[pos] = False