class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        L = 0
        R = len(s)-1

        while L<R:
            if s[L]!=s[R]:
                if count < 1:
                    count+=1
                else:
                    return False
            
            L+=1
            R-=1
        
        return True