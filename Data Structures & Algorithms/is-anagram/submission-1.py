from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = Counter(s)

        for char in t:
            if char not in letters or letters[char] <=0:
                return False
            
            letters[char]-=1
        
        res = [x for x in letters if letters[x]>0]

        return len(res) == 0