class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lenA = len(word1)
        lenB = len(word2)
        res = ""
        i, j = 0,0
        while i<lenA or j<lenB:
            if i<lenA:
                res+=word1[i]
                i+=1
            if j<lenB:
                res+=word2[j]
                j+=1
        
        return res