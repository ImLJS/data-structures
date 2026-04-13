class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:].zfill(32)[::-1]
        num = int(binary, 2)
        return num