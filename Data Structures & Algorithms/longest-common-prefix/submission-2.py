class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        short = strs[0]
        long = strs[-1]

        ans = ""

        for i in range(len(short)):
            if short[i] != long[i]:
                return ans
            
            ans+=short[i]
        
        return ans