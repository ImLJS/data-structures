class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res = ''
        short = strs[0]
        long = strs[-1]

        for i in range(len(short)):
            if short[i] != long[i]:
                return res
            res+=short[i]
        
        return res