class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        min_len = min(len(word1), len(word2))
        char = 0

        while char < min_len:
            res+=word1[char] 
            res+=word2[char]
            char+=1

        p,q = char,char
        while p < len(word1):
            res+=word1[p]
            p+=1
        
        while q < len(word2):
            res+=word2[q]
            q+=1
        
        return res