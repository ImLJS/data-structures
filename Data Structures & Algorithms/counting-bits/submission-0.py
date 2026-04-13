class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            binary = bin(i)
            countOne = str(binary).count("1")
            res.append(int(countOne))
        return res