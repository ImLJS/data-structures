from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strings = Counter(s)
        
        for word in t:
            if word not in strings or strings[word] <=0:
                return False
            
            strings[word]-=1
        
        ans = [x for x in strings if strings[x]>0]

        return True if len(ans)==0 else False