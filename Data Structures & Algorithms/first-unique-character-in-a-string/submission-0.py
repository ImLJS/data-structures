class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)

        char = [x for x in freq if freq[x] == 1]

        if char:
            return s.index(char[0])
        return -1